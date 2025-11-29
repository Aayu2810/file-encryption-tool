from datetime import datetime
import utils

class SelfDestruct:
    def __init__(self, encrypted_file):
        self.encrypted_file = encrypted_file
        self.metadata_file = utils.create_metadata_filename(encrypted_file)
        self.metadata = self.load_or_create_metadata()
    
    def load_or_create_metadata(self):
        """Load existing metadata or create new"""
        metadata = utils.load_metadata(self.metadata_file)
        
        if metadata is None:
            # Create default metadata
            metadata = {
                "view_count": 0,
                "max_views": None,
                "expiry_date": None,
                "wrong_attempts": 0,
                "max_wrong_attempts": 3,
                "created_date": utils.get_current_datetime(),
                "is_active": True
            }
            utils.save_metadata(metadata, self.metadata_file)
        
        return metadata
    
    def set_max_views(self, max_views):
        """Set maximum number of views before self-destruct"""
        self.metadata["max_views"] = max_views
        utils.save_metadata(self.metadata, self.metadata_file)
    
    def set_expiry_date(self, expiry_date):
        """Set expiry date (format: YYYY-MM-DD HH:MM:SS)"""
        self.metadata["expiry_date"] = expiry_date
        utils.save_metadata(self.metadata, self.metadata_file)
    
    def set_max_wrong_attempts(self, max_attempts):
        """Set maximum wrong password attempts"""
        self.metadata["max_wrong_attempts"] = max_attempts
        utils.save_metadata(self.metadata, self.metadata_file)
    
    def check_expiry(self):
        """Check if file has expired"""
        if self.metadata["expiry_date"] is None:
            return False, "No expiry date set"
        
        expiry_date = utils.parse_datetime(self.metadata["expiry_date"])
        current_date = datetime.now()
        
        if current_date > expiry_date:
            return True, "File has expired"
        
        return False, "File is still valid"
    
    def check_view_limit(self):
        """Check if view limit has been reached"""
        if self.metadata["max_views"] is None:
            return False, "No view limit set"
        
        if self.metadata["view_count"] >= self.metadata["max_views"]:
            return True, "View limit reached"
        
        return False, f"Views remaining: {self.metadata['max_views'] - self.metadata['view_count']}"
    
    def increment_view_count(self):
        """Increment view counter after successful decryption"""
        self.metadata["view_count"] += 1
        utils.save_metadata(self.metadata, self.metadata_file)
        
        if self.metadata["max_views"]:
            remaining = self.metadata["max_views"] - self.metadata["view_count"]
            print(f"⚠️  Views remaining: {remaining}")
    
    def record_wrong_attempt(self):
        """Record a wrong password attempt"""
        self.metadata["wrong_attempts"] += 1
        utils.save_metadata(self.metadata, self.metadata_file)
        
        remaining = self.metadata["max_wrong_attempts"] - self.metadata["wrong_attempts"]
        
        if remaining <= 0:
            return True, "Maximum wrong attempts reached"
        
        return False, f"Wrong password! Attempts remaining: {remaining}"
    
    def reset_wrong_attempts(self):
        """Reset wrong attempt counter after successful decryption"""
        self.metadata["wrong_attempts"] = 0
        utils.save_metadata(self.metadata, self.metadata_file)
    
    def should_self_destruct(self):
        """Check all conditions and determine if file should self-destruct"""
        reasons = []
        
        # Check expiry
        expired, msg = self.check_expiry()
        if expired:
            reasons.append(msg)
        
        # Check view limit
        limit_reached, msg = self.check_view_limit()
        if limit_reached:
            reasons.append(msg)
        
        # Check wrong attempts
        if self.metadata["wrong_attempts"] >= self.metadata["max_wrong_attempts"]:
            reasons.append("Maximum wrong attempts reached")
        
        if reasons:
            return True, reasons
        
        return False, []
    
    def execute_self_destruct(self):
        """Execute self-destruct: securely delete encrypted file and metadata"""
        print("\n🔥 SELF-DESTRUCT INITIATED 🔥")
        
        # Delete encrypted file
        if utils.secure_delete_file(self.encrypted_file):
            print(f"✓ Securely deleted: {self.encrypted_file}")
        
        # Delete metadata file
        if utils.file_exists(self.metadata_file):
            utils.secure_delete_file(self.metadata_file)
            print(f"✓ Securely deleted: {self.metadata_file}")
        
        print("\n🔒 All files have been permanently destroyed")
    
    def get_status(self):
        """Get current status of the file"""
        status = {
            "Views": f"{self.metadata['view_count']}/{self.metadata['max_views'] or '∞'}",
            "Created": self.metadata["created_date"],
            "Expiry": self.metadata["expiry_date"] or "Never",
            "Wrong Attempts": f"{self.metadata['wrong_attempts']}/{self.metadata['max_wrong_attempts']}",
            "Active": self.metadata["is_active"]
        }
        return status
