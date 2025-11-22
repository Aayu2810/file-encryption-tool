import os
import json
from datetime import datetime

def get_file_size(file_path):
    """Get file size in bytes"""
    return os.path.getsize(file_path)

def file_exists(file_path):
    """Check if file exists"""
    return os.path.exists(file_path)

def create_metadata_filename(original_file):
    """Create metadata filename for encrypted file"""
    return original_file + ".meta"

def save_metadata(metadata, metadata_file):
    """Save metadata to JSON file"""
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=4)

def load_metadata(metadata_file):
    """Load metadata from JSON file"""
    if not file_exists(metadata_file):
        return None
    
    with open(metadata_file, 'r') as f:
        return json.load(f)

def get_current_datetime():
    """Get current date and time as string"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def parse_datetime(date_string):
    """Parse datetime string"""
    return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

def secure_delete_file(file_path):
    """Securely delete file by overwriting before deletion"""
    if not file_exists(file_path):
        return False
    
    try:
        # Get file size
        file_size = get_file_size(file_path)
        
        # Overwrite with random data (3 passes)
        with open(file_path, 'wb') as f:
            for _ in range(3):
                f.seek(0)
                f.write(os.urandom(file_size))
        
        # Delete the file
        os.remove(file_path)
        return True
    except Exception as e:
        print(f"Error in secure deletion: {e}")
        return False

def validate_password(password):
    """Basic password validation"""
    if len(password) < 6:
        return False, "Password must be at least 6 characters long"
    return True, "Valid"

def print_banner():
    """Print application banner"""
    banner = """
    ╔════════════════════════════════════════════╗
    ║   SECURE FILE ENCRYPTION TOOL              ║
    ║   With Steganography & Self-Destruct       ║
    ╚════════════════════════════════════════════╝
    """
    print(banner)