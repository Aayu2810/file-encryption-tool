# 🔐 Secure File Encryption Tool

**🌐 Live Demo:** [https://aayu2810.github.io/file-encryption-tool/](https://aayu2810.github.io/file-encryption-tool/)

A comprehensive file encryption tool with advanced security features including steganography, self-destruct mechanisms, and plausible deniability. Available as both a **web interface** and **Python CLI application**.

---

## 🎯 Features

### 🔒 **AES-256 Encryption**
- Military-grade encryption with HMAC authentication
- 256-bit key length for maximum security
- PBKDF2 key derivation (100,000 iterations)
- Protection against unauthorized access

### ⏰ **Self-Destruct Mechanisms**
- **View Counter** - Files auto-delete after N views
- **Expiry Date/Time** - Automatic deletion after specified date
- **Wrong Password Tracking** - Delete after failed attempts
- **Secure Deletion** - 3-pass overwrite before deletion

### 🎭 **Plausible Deniability**
- Dual-password system with fake and real data
- One encrypted file accessible with two different passwords
- Each password reveals different content
- No way to prove second password exists
- Perfect for security under duress

### 🖼️ **Steganography**
- Hide encrypted data inside images
- LSB (Least Significant Bit) technique
- Invisible to the naked eye
- Supports PNG and JPG images
- Optional password protection for hidden data

### 🔒 **Additional Security**
- Password validation and strength checking
- HMAC-based authentication
- Secure file deletion (multi-pass overwriting)
- Metadata tracking for access control

---

## 🌐 Web Interface

Visit our **live web application**: [https://aayu2810.github.io/file-encryption-tool/](https://aayu2810.github.io/file-encryption-tool/)

### Features:
- 🎨 Beautiful, modern UI with gradient design
- 📱 Mobile-friendly responsive design
- 🖱️ Drag & drop file support
- 📊 Real-time progress indicators
- 🎯 Easy-to-use interface for all features
- ⚡ No installation required - runs in browser

### Available Pages:
1. **Home** - Feature overview and navigation
2. **AES Encryption** - Basic file encryption/decryption
3. **Self-Destruct** - Time-limited encryption
4. **Dual Password** - Plausible deniability mode
5. **Steganography** - Hide data in images

---

## 💻 Python CLI Application

For full features and advanced usage, use the command-line version.

### Installation
```bash
# Clone the repository
git clone https://github.com/Aayu2810/file-encryption-tool.git
cd file-encryption-tool

# Install dependencies
pip install -r requirements.txt

# Run the application
cd src
python main.py
```

### Requirements
```
cryptography==41.0.7
Pillow==10.1.0
```

### Usage Examples

#### Basic Encryption
```bash
python main.py
# Select option 1 (Encrypt)
# Follow prompts to encrypt your file
```

#### With Self-Destruct
```bash
# Enable self-destruct during encryption
# Set max views: 3
# Set expiry date: 2025-12-31 23:59:59
# File will auto-delete when conditions are met
```

#### Plausible Deniability
```bash
# Choose dual password option
# Provide real file (secret data)
# Provide fake file (decoy data)
# Set two different passwords
```

#### Steganography
```bash
# After encryption, choose to hide in image
# Provide a cover image (PNG/JPG)
# Encrypted data is hidden invisibly in the image
```

---

## 🏗️ Project Structure
```
file-encryption-tool/
├── index.html                     # Home page (web interface)
├── aes_encryption.html            # AES encryption interface
├── self_destruct.html             # Self-destruct mode
├── dual_password.html             # Dual password interface
├── steganography.html             # Steganography interface
├── src/
│   ├── main.py                    # Main CLI application
│   ├── encryption.py              # AES-256 encryption with HMAC
│   ├── self_destruct.py           # Self-destruct features
│   ├── steganography.py           # LSB steganography
│   ├── plausible_deniability.py   # Dual-password system
│   └── utils.py                   # Helper functions
├── requirements.txt               # Python dependencies
└── README.md                      # Documentation
```

---

## 🔬 Operating System Concepts Demonstrated

This project demonstrates various OS concepts learned in the Operating Systems course:

1. **File I/O Operations**
   - System calls for reading/writing files
   - Binary file handling
   - File descriptor management

2. **File Metadata Management**
   - Tracking access counts and timestamps
   - File attributes and permissions
   - Metadata persistence

3. **Secure File Deletion**
   - Multi-pass overwriting technique
   - Safe data destruction
   - File system operations

4. **Process Management**
   - Application lifecycle control
   - System resource management

5. **Memory Management**
   - Efficient data buffering
   - Large file handling
   - Memory optimization

6. **System Time APIs**
   - Date/time operations
   - Expiry checking
   - Timestamp management

---

## 📊 Technical Specifications

| Component | Technology |
|-----------|------------|
| **Encryption Algorithm** | AES-256-CBC |
| **Authentication** | HMAC-SHA256 |
| **Key Derivation** | PBKDF2 (100,000 iterations) |
| **Steganography** | LSB (Least Significant Bit) |
| **Programming Language** | Python 3.x |
| **Web Technologies** | HTML5, CSS3, JavaScript |
| **Crypto Library** | Python Cryptography, CryptoJS |

---

## 🧪 Testing

All features have been thoroughly tested:

✅ **Encryption/Decryption**
- Correct password acceptance
- Wrong password rejection
- File integrity verification

✅ **Self-Destruct Features**
- View counter tracking
- Expiry date validation
- Wrong attempt limits

✅ **Dual Password System**
- Both passwords work independently
- Different content revealed
- No cross-contamination

✅ **Steganography**
- Data hidden successfully
- Extraction without data loss
- Image quality preserved

---

## 🎓 Course Information

**Project:** Secure File Encryption Tool  
**Course:** Operating Systems  
**Institution:** RV College of Engineering  
**Academic Year:** 2024-2025  

### Team Member
- **Aayushi Priya** [1RV24IS005]

---

## 🚀 Quick Start Guide

### For Demo/Presentation (Web Interface)

1. Visit: [https://aayu2810.github.io/file-encryption-tool/](https://aayu2810.github.io/file-encryption-tool/)
2. Click on any feature card
3. Upload a test file
4. Follow the on-screen instructions
5. Download the encrypted/processed file

### For Development (Python CLI)
```bash
# Clone repository
git clone https://github.com/Aayu2810/file-encryption-tool.git
cd file-encryption-tool

# Install dependencies
pip install -r requirements.txt

# Run application
cd src
python main.py
```

---

## 🔮 Future Enhancements

- [ ] IoT integration for remote access control
- [ ] Mobile app (Android/iOS)
- [ ] Biometric authentication integration
- [ ] Cloud storage integration
- [ ] Multi-user access management
- [ ] Blockchain-based audit logging
- [ ] Real-time collaboration features
- [ ] Advanced file compression
- [ ] Database encryption support

---

## 📜 License

MIT License

---

## 🤝 Contributing

This is an academic project. For suggestions or improvements:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📧 Contact

**Aayushi Priya**  
RV College of Engineering  
GitHub: [@Aayu2810](https://github.com/Aayu2810)

---

## 🙏 Acknowledgments

- RV College of Engineering - Operating Systems Course
- Python Cryptography Library
- CryptoJS for web encryption
- Open source community

---

## ⭐ Show Your Support

If you find this project helpful, please consider giving it a star on GitHub!

---

**Made with ❤️ for Operating Systems | RV College of Engineering | 2024-25**
