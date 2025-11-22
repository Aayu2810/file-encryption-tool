from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os

class FileEncryption:
    def __init__(self):
        self.backend = default_backend()
    
    def derive_key(self, password, salt):
        """Derive encryption key from password using PBKDF2"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # 256 bits for AES-256
            salt=salt,
            iterations=100000,
            backend=self.backend
        )
        return kdf.derive(password.encode())
    
    def generate_hmac(self, key, data):
        """Generate HMAC for authentication"""
        h = hmac.HMAC(key, hashes.SHA256(), backend=self.backend)
        h.update(data)
        return h.finalize()
    
    def verify_hmac(self, key, data, expected_hmac):
        """Verify HMAC"""
        h = hmac.HMAC(key, hashes.SHA256(), backend=self.backend)
        h.update(data)
        try:
            h.verify(expected_hmac)
            return True
        except:
            return False
    
    def encrypt_data(self, data, password):
        """Encrypt data using AES-256-CBC with HMAC authentication"""
        # Generate random salt and IV
        salt = os.urandom(16)
        iv = os.urandom(16)
        
        # Derive key from password
        key = self.derive_key(password, salt)
        
        # Pad data to be multiple of 16 bytes (AES block size)
        padding_length = 16 - (len(data) % 16)
        padded_data = data + bytes([padding_length] * padding_length)
        
        # Create cipher and encrypt
        cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=self.backend
        )
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Generate HMAC for authentication (using salt + iv + encrypted_data)
        auth_data = salt + iv + encrypted_data
        mac = self.generate_hmac(key, auth_data)
        
        # Return salt + iv + encrypted_data + mac
        return salt + iv + encrypted_data + mac
    
    def decrypt_data(self, encrypted_data, password):
        """Decrypt data using AES-256-CBC with HMAC authentication"""
        # Check minimum length
        if len(encrypted_data) < 64:  # 16 (salt) + 16 (iv) + 32 (hmac) = 64 minimum
            raise ValueError("Invalid encrypted data - file may be corrupted")
        
        # Extract components
        salt = encrypted_data[:16]
        iv = encrypted_data[16:32]
        mac = encrypted_data[-32:]  # Last 32 bytes is HMAC
        ciphertext = encrypted_data[32:-32]  # Everything between IV and HMAC
        
        # Derive key from password
        key = self.derive_key(password, salt)
        
        # Verify HMAC FIRST - this confirms password is correct
        auth_data = salt + iv + ciphertext
        if not self.verify_hmac(key, auth_data, mac):
            raise ValueError("Authentication failed - incorrect password")
        
        # Now decrypt (we know password is correct)
        cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=self.backend
        )
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Remove padding
        if len(padded_data) == 0:
            raise ValueError("Decryption produced empty data")
        
        padding_length = padded_data[-1]
        
        # Validate padding
        if not isinstance(padding_length, int):
            padding_length = int(padding_length)
        
        if padding_length > 16 or padding_length < 1:
            raise ValueError("Invalid padding")
        
        data = padded_data[:-padding_length]
        
        return data
    
    def encrypt_file(self, input_file, output_file, password):
        """Encrypt a file"""
        try:
            # Read file content
            with open(input_file, 'rb') as f:
                data = f.read()
            
            # Encrypt data
            encrypted_data = self.encrypt_data(data, password)
            
            # Write encrypted data
            with open(output_file, 'wb') as f:
                f.write(encrypted_data)
            
            return True, "File encrypted successfully"
        except Exception as e:
            return False, f"Encryption failed: {str(e)}"
    
    def decrypt_file(self, input_file, output_file, password):
        """Decrypt a file"""
        try:
            # Read encrypted data
            with open(input_file, 'rb') as f:
                encrypted_data = f.read()
            
            # Decrypt data - this will raise ValueError if password is wrong
            decrypted_data = self.decrypt_data(encrypted_data, password)
            
            # Write decrypted data
            with open(output_file, 'wb') as f:
                f.write(decrypted_data)
            
            return True, "File decrypted successfully"
        except ValueError as e:
            return False, str(e)
        except Exception as e:
            return False, f"Decryption failed: {str(e)}"


# Test the module
if __name__ == "__main__":
    enc = FileEncryption()
    
    # Test encryption/decryption
    test_data = b"Hello, this is a secret message!"
    password = "mypassword123"
    
    print("Testing encryption...")
    encrypted = enc.encrypt_data(test_data, password)
    print(f"✓ Encrypted ({len(encrypted)} bytes)")
    
    print("\nTesting decryption with correct password...")
    try:
        decrypted = enc.decrypt_data(encrypted, password)
        print(f"✓ Decrypted: {decrypted}")
        
        if test_data == decrypted:
            print("✓ Encryption/Decryption test PASSED!")
    except Exception as e:
        print(f"✗ Test failed: {e}")
    
    print("\nTesting decryption with WRONG password...")
    try:
        decrypted = enc.decrypt_data(encrypted, "wrongpassword")
        print(f"✗ Should have failed but got: {decrypted}")
    except ValueError as e:
        print(f"✓ Correctly rejected wrong password: {e}")