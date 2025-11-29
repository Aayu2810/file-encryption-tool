import os
import sys
from encryption import FileEncryption
from self_destruct import SelfDestruct
from steganography import SteganographyWithPriority
from plausible_deniability import PlausibleDeniability
import utils

class FileEncryptionTool:
    def __init__(self):
        self.encryptor = FileEncryption()
        self.stego = SteganographyWithPriority()
        self.pd = PlausibleDeniability()
    
    def encrypt_menu(self):
        """Handle file encryption"""
        print("\n" + "="*50)
        print("FILE ENCRYPTION")
        print("="*50)
        
        # Ask about plausible deniability first
        use_dual = input("\nUse Plausible Deniability (dual password)? (y/n): ").lower()
        
        if use_dual == 'y':
            self.encrypt_with_deniability()
        else:
            self.encrypt_normal()
    
    def encrypt_normal(self):
        """Normal encryption (single file, single password)"""
        # Get input file
        input_file = input("\nEnter file path to encrypt: ").strip()
        
        if not utils.file_exists(input_file):
            print("❌ Error: File not found!")
            return
        
        # Get password
        password = input("Enter encryption password: ").strip()
        valid, msg = utils.validate_password(password)
        if not valid:
            print(f"❌ {msg}")
            return
        
        # Confirm password
        password_confirm = input("Confirm password: ").strip()
        if password != password_confirm:
            print("❌ Passwords do not match!")
            return
        
        # Output file
        output_file = input_file + ".enc"
        
        # Encrypt the file
        print("\n🔒 Encrypting file...")
        success, message = self.encryptor.encrypt_file(input_file, output_file, password)
        
        if not success:
            print(f"❌ {message}")
            return
        
        print(f"✓ {message}")
        print(f"✓ Encrypted file saved as: {output_file}")
        
        # Self-destruct options
        print("\n--- Self-Destruct Options ---")
        use_self_destruct = input("Enable self-destruct features? (y/n): ").lower()
        
        if use_self_destruct == 'y':
            self.setup_self_destruct(output_file)
        
        # Steganography option
        use_stego = input("\nHide encrypted file in an image? (y/n): ").lower()
        
        if use_stego == 'y':
            self.hide_in_image(output_file)
        
        # Ask if user wants to delete original
        delete_original = input("\nDelete original file? (y/n): ").lower()
        if delete_original == 'y':
            utils.secure_delete_file(input_file)
            print("✓ Original file securely deleted")
    
    def encrypt_with_deniability(self):
        """Encrypt with plausible deniability (two files, two passwords)"""
        print("\n--- PLAUSIBLE DENIABILITY MODE ---")
        print("You'll create ONE encrypted file with TWO passwords:")
        print("  • Fake password → shows innocent decoy content")
        print("  • Real password → shows actual secret content")
        print()
        
        # Get real file
        real_file = input("Enter REAL file path (secret): ").strip()
        if not utils.file_exists(real_file):
            print("❌ Error: Real file not found!")
            return
        
        # Get fake file
        fake_file = input("Enter FAKE file path (decoy): ").strip()
        if not utils.file_exists(fake_file):
            print("❌ Error: Fake file not found!")
            return
        
        # Get real password
        real_password = input("\nEnter REAL password (for secret): ").strip()
        valid, msg = utils.validate_password(real_password)
        if not valid:
            print(f"❌ {msg}")
            return
        real_password_confirm = input("Confirm REAL password: ").strip()
        if real_password != real_password_confirm:
            print("❌ Passwords do not match!")
            return
        
        # Get fake password
        fake_password = input("\nEnter FAKE password (for decoy): ").strip()
        valid, msg = utils.validate_password(fake_password)
        if not valid:
            print(f"❌ {msg}")
            return
        fake_password_confirm = input("Confirm FAKE password: ").strip()
        if fake_password != fake_password_confirm:
            print("❌ Passwords do not match!")
            return
        
        # Make sure passwords are different
        if real_password == fake_password:
            print("❌ Real and Fake passwords must be different!")
            return
        
        # Output file
        output_file = real_file + ".dual.enc"
        
        # Encrypt with dual passwords
        print("\n🔒 Creating dual-encrypted file...")
        success, message = self.pd.encrypt_dual(real_file, fake_file, real_password, fake_password, output_file)
        
        if success:
            print(f"✓ {message}")
            print(f"✓ Dual-encrypted file saved as: {output_file}")
            print(f"\n💡 TIP: Use fake password if someone forces you to decrypt!")
            
            # Self-destruct
            use_self_destruct = input("\nEnable self-destruct features? (y/n): ").lower()
            if use_self_destruct == 'y':
                self.setup_self_destruct(output_file)
            
            # Steganography
            use_stego = input("\nHide in an image? (y/n): ").lower()
            if use_stego == 'y':
                self.hide_in_image(output_file)
        else:
            print(f"❌ {message}")
    
    def hide_in_image(self, encrypted_file):
        """Hide encrypted file in an image"""
        cover_image = input("Enter cover image path (PNG/JPG): ").strip()
        
        if not utils.file_exists(cover_image):
            print("❌ Error: Cover image not found!")
            return
        
        # Check image capacity
        capacity = self.stego.get_image_capacity(cover_image)
        file_size = utils.get_file_size(encrypted_file)
        
        print(f"\nImage capacity: {capacity} bytes")
        print(f"File size: {file_size} bytes")
        
        if file_size > capacity:
            print("❌ Error: Image too small to hide this file!")
            return
        
        # Read encrypted data
        with open(encrypted_file, 'rb') as f:
            encrypted_data = f.read()
        
        # Output stego image
        output_image = encrypted_file + ".stego.png"
        
        print("\n🖼️  Hiding data in image...")
        success, message = self.stego.encode_data_in_image(cover_image, encrypted_data, output_image)
        
        if success:
            print(f"✓ {message}")
            
            # Ask to delete encrypted file
            delete_enc = input("\nDelete original encrypted file? (y/n): ").lower()
            if delete_enc == 'y':
                utils.secure_delete_file(encrypted_file)
                # Also delete metadata if exists
                meta_file = utils.create_metadata_filename(encrypted_file)
                if utils.file_exists(meta_file):
                    os.remove(meta_file)
                print("✓ Encrypted file deleted (data now hidden in image)")
        else:
            print(f"❌ {message}")
    
    def setup_self_destruct(self, encrypted_file):
        """Setup self-destruct parameters"""
        sd = SelfDestruct(encrypted_file)
        
        # Max views
        set_views = input("Set maximum views limit? (y/n): ").lower()
        if set_views == 'y':
            try:
                max_views = int(input("Enter maximum views (e.g., 5): "))
                sd.set_max_views(max_views)
                print(f"✓ View limit set to {max_views}")
            except ValueError:
                print("❌ Invalid number")
        
        # Expiry date
        set_expiry = input("Set expiry date? (y/n): ").lower()
        if set_expiry == 'y':
            expiry = input("Enter expiry date (YYYY-MM-DD HH:MM:SS): ").strip()
            sd.set_expiry_date(expiry)
            print(f"✓ Expiry date set to {expiry}")
        
        # Max wrong attempts
        set_attempts = input("Change max wrong attempts (default 3)? (y/n): ").lower()
        if set_attempts == 'y':
            try:
                max_attempts = int(input("Enter max wrong attempts: "))
                sd.set_max_wrong_attempts(max_attempts)
                print(f"✓ Max wrong attempts set to {max_attempts}")
            except ValueError:
                print("❌ Invalid number")
    
    def decrypt_menu(self):
        """Handle file decryption"""
        print("\n" + "="*50)
        print("FILE DECRYPTION")
        print("="*50)
        
        # Get file
        input_file = input("\nEnter encrypted file path: ").strip()
        
        if not utils.file_exists(input_file):
            print("❌ Error: File not found!")
            return
        
        # Check if it's a stego image
        is_stego = input("Is this a steganography image? (y/n): ").lower()
        
        if is_stego == 'y':
            self.decrypt_from_image(input_file)
        else:
            # Check if dual-encrypted
            if self.pd.is_dual_encrypted(input_file):
                self.decrypt_dual(input_file)
            else:
                self.decrypt_normal(input_file)
    
    def decrypt_from_image(self, image_file):
        """Extract and decrypt from steganography image"""
        print("\n🖼️  Extracting hidden data from image...")
        success, result = self.stego.decode_data_from_image(image_file)
        
        if not success:
            print(f"❌ {result}")
            return
        
        encrypted_data = result
        print(f"✓ Extracted {len(encrypted_data)} bytes of hidden data")
        
        # Check if dual-encrypted
        is_dual = encrypted_data.startswith(b"DUALENC1")
        
        if is_dual:
            # Save temporarily
            temp_file = "temp_extracted.dual.enc"
            with open(temp_file, 'wb') as f:
                f.write(encrypted_data)
            
            self.decrypt_dual(temp_file)
            
            # Cleanup
            if utils.file_exists(temp_file):
                os.remove(temp_file)
        else:
            # Normal encryption
            password = input("\nEnter decryption password: ").strip()
            
            print("\n🔓 Decrypting...")
            try:
                decrypted_data = self.encryptor.decrypt_data(encrypted_data, password)
                
                # Save decrypted file
                output_file = input("Save decrypted file as: ").strip()
                with open(output_file, 'wb') as f:
                    f.write(decrypted_data)
                
                print(f"✓ File decrypted and saved as: {output_file}")
            except Exception as e:
                print(f"❌ Decryption failed: {str(e)}")
    
    def decrypt_dual(self, encrypted_file):
        """Decrypt dual-encrypted file"""
        print("\n🎭 DUAL-ENCRYPTED FILE DETECTED")
        print("Enter your password (system cannot tell which password you use)")
        
        # Check self-destruct
        sd = SelfDestruct(encrypted_file)
        print("\n--- File Status ---")
        status = sd.get_status()
        for key, value in status.items():
            print(f"{key}: {value}")
        
        should_destruct, reasons = sd.should_self_destruct()
        if should_destruct:
            print(f"\n❌ File cannot be decrypted!")
            for reason in reasons:
                print(f"   - {reason}")
            
            confirm = input("\nExecute self-destruct? (yes/no): ").strip().lower()
            if confirm == "yes":
                sd.execute_self_destruct()
            return
        
        # Get password
        password = input("\nEnter password: ").strip()
        
        # Decrypt
        print("\n🔓 Decrypting...")
        success, result, file_type = self.pd.decrypt_dual(encrypted_file, password)
        
        if success:
            decrypted_data = result
            
            # Don't tell user which type they got!
            output_file = input("Save decrypted file as: ").strip()
            with open(output_file, 'wb') as f:
                f.write(decrypted_data)
            
            print(f"✓ File decrypted successfully")
            print(f"✓ Saved as: {output_file}")
            
            # Update counters
            sd.reset_wrong_attempts()
            sd.increment_view_count()
            
            # Check self-destruct after view
            should_destruct, reasons = sd.should_self_destruct()
            if should_destruct:
                print(f"\n⚠️  WARNING: Self-destruct conditions met!")
                for reason in reasons:
                    print(f"   - {reason}")
                
                confirm = input("\nExecute self-destruct? (yes/no): ").strip().lower()
                if confirm == "yes":
                    sd.execute_self_destruct()
        else:
            print(f"❌ {result}")
            
            should_destruct, msg = sd.record_wrong_attempt()
            print(f"⚠️  {msg}")
            
            if should_destruct:
                print("\n🔥 Maximum wrong attempts reached!")
                confirm = input("Execute self-destruct? (yes/no): ").strip().lower()
                if confirm == "yes":
                    sd.execute_self_destruct()
    
    def decrypt_normal(self, encrypted_file):
        """Decrypt normal encrypted file"""
        # Check self-destruct
        sd = SelfDestruct(encrypted_file)
        print("\n--- File Status ---")
        status = sd.get_status()
        for key, value in status.items():
            print(f"{key}: {value}")
        
        should_destruct, reasons = sd.should_self_destruct()
        if should_destruct:
            print(f"\n❌ File cannot be decrypted!")
            for reason in reasons:
                print(f"   - {reason}")
            
            confirm = input("\nExecute self-destruct? (yes/no): ").strip().lower()
            if confirm == "yes":
                sd.execute_self_destruct()
            return
        
        # Get password
        password = input("\nEnter decryption password: ").strip()
        
        # Output file
        if encrypted_file.endswith('.enc'):
            output_file = encrypted_file[:-4]
        else:
            output_file = encrypted_file + ".decrypted"
        
        # Decrypt
        print("\n🔓 Decrypting file...")
        success, message = self.encryptor.decrypt_file(encrypted_file, output_file, password)
        
        if success:
            print(f"✓ {message}")
            print(f"✓ Decrypted file saved as: {output_file}")
            
            sd.reset_wrong_attempts()
            sd.increment_view_count()
            
            should_destruct, reasons = sd.should_self_destruct()
            if should_destruct:
                print(f"\n⚠️  WARNING: Self-destruct conditions met!")
                for reason in reasons:
                    print(f"   - {reason}")
                
                confirm = input("\nExecute self-destruct? (yes/no): ").strip().lower()
                if confirm == "yes":
                    sd.execute_self_destruct()
        else:
            print(f"❌ {message}")
            
            should_destruct, msg = sd.record_wrong_attempt()
            print(f"⚠️  {msg}")
            
            if should_destruct:
                print("\n🔥 Maximum wrong attempts reached!")
                confirm = input("Execute self-destruct? (yes/no): ").strip().lower()
                if confirm == "yes":
                    sd.execute_self_destruct()
    
    def main_menu(self):
        """Display main menu"""
        while True:
            utils.print_banner()
            print("\n1. Encrypt File")
            print("2. Decrypt File")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                self.encrypt_menu()
            elif choice == '2':
                self.decrypt_menu()
            elif choice == '3':
                print("\n👋 Goodbye!")
                sys.exit(0)
            else:
                print("❌ Invalid choice! Please enter 1, 2, or 3.")
            
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    app = FileEncryptionTool()
    app.main_menu()
