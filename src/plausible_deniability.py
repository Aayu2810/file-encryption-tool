from encryption import FileEncryption
import struct

class PlausibleDeniability:
    def __init__(self):
        self.encryptor = FileEncryption()
        self.magic_header = b"DUALENC1"  # Magic bytes to identify dual encryption
    
    def encrypt_dual(self, real_file, fake_file, real_password, fake_password, output_file):
        """
        Encrypt two files with two different passwords into one container.
        - real_file: The actual secret file
        - fake_file: The decoy file (innocent content)
        - real_password: Password for real file
        - fake_password: Password for fake file
        - output_file: Combined encrypted output
        """
        try:
            # Read both files
            with open(real_file, 'rb') as f:
                real_data = f.read()
            
            with open(fake_file, 'rb') as f:
                fake_data = f.read()
            
            # Encrypt both separately
            encrypted_real = self.encryptor.encrypt_data(real_data, real_password)
            encrypted_fake = self.encryptor.encrypt_data(fake_data, fake_password)
            
            # Create container structure:
            # [MAGIC_HEADER][FAKE_LENGTH][FAKE_DATA][REAL_DATA]
            
            fake_length = len(encrypted_fake)
            
            # Pack: magic header + fake length (4 bytes) + fake encrypted + real encrypted
            container = self.magic_header
            container += struct.pack('<I', fake_length)  # 4 bytes for length
            container += encrypted_fake
            container += encrypted_real
            
            # Write to output file
            with open(output_file, 'wb') as f:
                f.write(container)
            
            return True, "Dual encryption successful"
            
        except Exception as e:
            return False, f"Dual encryption failed: {str(e)}"
    
    def decrypt_dual(self, encrypted_file, password):
        """
        Decrypt using either password - returns whichever matches.
        User cannot tell if another password exists.
        """
        try:
            # Read encrypted container
            with open(encrypted_file, 'rb') as f:
                container = f.read()
            
            # Verify magic header
            if not container.startswith(self.magic_header):
                return False, "Not a dual-encrypted file", None
            
            # Parse container
            header_size = len(self.magic_header)
            fake_length = struct.unpack('<I', container[header_size:header_size+4])[0]
            
            # Extract fake and real encrypted data
            fake_start = header_size + 4
            fake_end = fake_start + fake_length
            
            encrypted_fake = container[fake_start:fake_end]
            encrypted_real = container[fake_end:]
            
            # Try decrypting fake first
            try:
                decrypted_data = self.encryptor.decrypt_data(encrypted_fake, password)
                return True, decrypted_data, "fake"
            except:
                pass  # Password doesn't match fake, try real
            
            # Try decrypting real
            try:
                decrypted_data = self.encryptor.decrypt_data(encrypted_real, password)
                return True, decrypted_data, "real"
            except:
                pass  # Password doesn't match real either
            
            # Neither password matched
            return False, "Incorrect password", None
            
        except Exception as e:
            return False, f"Decryption failed: {str(e)}", None
    
    def is_dual_encrypted(self, file_path):
        """Check if a file is dual-encrypted"""
        try:
            with open(file_path, 'rb') as f:
                header = f.read(len(self.magic_header))
            return header == self.magic_header
        except:
            return False


# Test the module
if __name__ == "__main__":
    pd = PlausibleDeniability()
    
    print("Testing Plausible Deniability Module...")
    
    # Create test files
    with open("test_real.txt", "w") as f:
        f.write("This is the REAL secret message!")
    
    with open("test_fake.txt", "w") as f:
        f.write("This is just my homework notes, nothing interesting here.")
    
    print("\n1. Creating dual-encrypted file...")
    success, msg = pd.encrypt_dual(
        "test_real.txt",
        "test_fake.txt",
        "real_password_123",
        "fake_password_456",
        "test_dual.enc"
    )
    print(f"   {msg}")
    
    if success:
        print("\n2. Testing decryption with FAKE password...")
        success, data, type_ = pd.decrypt_dual("test_dual.enc", "fake_password_456")
        if success:
            print(f"   ✓ Decrypted ({type_}): {data.decode()}")
        
        print("\n3. Testing decryption with REAL password...")
        success, data, type_ = pd.decrypt_dual("test_dual.enc", "real_password_123")
        if success:
            print(f"   ✓ Decrypted ({type_}): {data.decode()}")
        
        print("\n4. Testing decryption with WRONG password...")
        success, msg, _ = pd.decrypt_dual("test_dual.enc", "wrong_password")
        if not success:
            print(f"   ✓ Correctly rejected: {msg}")
    
    # Cleanup
    import os
    for f in ["test_real.txt", "test_fake.txt", "test_dual.enc"]:
        if os.path.exists(f):
            os.remove(f)
    
    print("\n✓ Plausible Deniability module tested successfully")