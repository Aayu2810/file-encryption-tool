# 🔐 Secure File Encryption Tool

**🌐 Live Demo:** [https://aayu2810.github.io/file-encryption-tool/](https://aayu2810.github.io/file-encryption-tool/)

A comprehensive file encryption tool with advanced security features and Operating System concepts implementation. Available as both a **web interface** and **Python CLI application**.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OS Course](https://img.shields.io/badge/Course-Operating%20Systems-orange.svg)](https://rvce.edu.in)

---

## 🎯 Features Overview

| Feature | Description | OS Concept |
|---------|-------------|------------|
| 🔒 **AES-256 Encryption** | Military-grade encryption with HMAC | File I/O, Memory Management |
| ⏰ **Self-Destruct** | Auto-delete after views/time/attempts | Process Management, System Time |
| 🎭 **Dual Password** | Plausible deniability system | Resource Allocation |
| 🖼️ **Priority Steganography** | Hide data using scheduling algorithm | **Priority Queue, Heap Operations** |

---

## 🆕 **NEW: Priority Queue Implementation**

### What's New?

**We've enhanced steganography with OS scheduling concepts!**

Instead of hiding data sequentially (pixel 1, 2, 3...), we now use a **Priority Queue-based scheduling algorithm** similar to CPU process scheduling:
```
Traditional Method:        Priority-Based Method:
[1][2][3][4][5]...    →    [245][12][891][45][702]...
Sequential pattern         Intelligent, scattered pattern
```

### OS Concepts Demonstrated

✅ **Priority Queue (heapq)** - Binary min-heap data structure  
✅ **Scheduling Algorithm** - Highest priority first (like Priority Scheduling)  
✅ **Heap Operations** - O(log n) insert/extract efficiency  
✅ **Resource Allocation** - Optimal pixel selection strategy  

### Priority Calculation
```python
Priority = (Complexity × 0.4) + (Entropy × 0.3) + (Edge_Distance × 0.3)

Where:
- Complexity: Pixel variation from neighbors (0-1)
- Entropy: LSB randomness (0-1)
- Edge_Distance: Distance from image edges (0-1)

Higher priority = Better hiding location
```

**Read full documentation:** [PRIORITY_QUEUE_EXPLANATION.md](PRIORITY_QUEUE_EXPLANATION.md)

---

## 🔒 Core Features

### 1. AES-256 Encryption
- Industry-standard AES-256-CBC encryption
- HMAC-SHA256 authentication
- PBKDF2 key derivation (100,000 iterations)
- Password strength validation
- Instant wrong password detection

### 2. Self-Destruct Mechanisms
- **View Counter** - Delete after N successful decryptions
- **Expiry Date** - Time-based automatic deletion
- **Wrong Attempts** - Lock after failed password tries
- **Secure Deletion** - 3-pass overwrite before deletion

### 3. Plausible Deniability
- One file, two passwords, two different contents
- Real password → Real secret data
- Fake password → Innocent decoy data
- No way to prove second password exists
- Perfect for security under duress

### 4. Priority-Based Steganography ⭐ NEW
- Intelligent pixel selection using priority queue
- Data hidden in high-complexity image areas
- Harder to detect than sequential methods
- Demonstrates OS scheduling algorithms
- O(log n) pixel selection efficiency

---

## 🌐 Web Interface

### Live Application
Visit: **[https://aayu2810.github.io/file-encryption-tool/](https://aayu2810.github.io/file-encryption-tool/)**

### Features
- 🎨 Modern, responsive UI with gradient design
- 📱 Mobile-friendly
- 🖱️ Drag & drop file support
- 📊 Real-time progress indicators
- ⚡ No installation required
- 🔒 Client-side encryption (data never leaves your browser)

### Pages
1. **Home** - Feature overview
2. **AES Encryption** - Basic encryption/decryption
3. **Self-Destruct** - Time-limited files
4. **Dual Password** - Plausible deniability
5. **Steganography** - Hide in images

---

## 💻 Python CLI Application

### Installation
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

### Requirements
```
cryptography==41.0.7    # AES encryption
Pillow==10.1.0          # Image processing
numpy==1.24.3           # Priority calculations
```

### Quick Start
```bash
# Basic encryption
python main.py
# Choose option 1 → Enter file and password

# With all features
python main.py
# Choose option 1 → Enable dual password, self-destruct, steganography
```

---

## 🏗️ Project Structure
```
file-encryption-tool/
├── web/                           # Web interface
│   ├── index.html                 # Home page
│   ├── aes_encryption.html        # AES interface
│   ├── self_destruct.html         # Self-destruct mode
│   ├── dual_password.html         # Dual password interface
│   └── steganography.html         # Steganography interface
│
├── src/                           # Python CLI
│   ├── main.py                    # Main application
│   ├── encryption.py              # AES-256 + HMAC
│   ├── self_destruct.py           # Self-destruct logic
│   ├── steganography.py           # Priority-based steganography ⭐
│   ├── plausible_deniability.py   # Dual password system
│   ├── utils.py                   # Helper functions
│   └── test_priority_steganography.py  # Test script ⭐
│
├── PRIORITY_QUEUE_EXPLANATION.md  # Detailed documentation ⭐
├── requirements.txt               # Dependencies
└── README.md                      # This file
```

---

## 🔬 Operating System Concepts Demonstrated

### 1. File I/O Operations
- System calls: `open()`, `read()`, `write()`, `close()`
- Binary file handling
- File descriptor management
- Buffered I/O operations

### 2. File Metadata Management
- Tracking access counts and timestamps
- File attributes and permissions
- Metadata persistence (JSON storage)
- Atomic metadata updates

### 3. Secure File Deletion
- Multi-pass overwriting (DOD 5220.22-M standard)
- Safe data destruction
- File system operation optimization
- Prevents data recovery

### 4. Process Management
- Application lifecycle control
- Resource cleanup on exit
- System resource management
- Process state handling

### 5. Memory Management
- Efficient data buffering for large files
- Memory-mapped file operations (optional)
- Dynamic memory allocation
- Garbage collection optimization

### 6. System Time APIs
- Real-time clock access
- Date/time operations for expiry
- Timestamp management
- Timezone handling

### 7. **Priority Queue (Data Structure)** ⭐ NEW
- Binary heap implementation (Python heapq)
- Priority-based element selection
- O(log n) insert and extract operations
- Efficient for large datasets (millions of pixels)

### 8. **Scheduling Algorithms** ⭐ NEW
- Priority-based scheduling (Highest Priority First)
- Similar to CPU process scheduling
- Multi-factor priority calculation
- Resource allocation optimization
- Non-preemptive scheduling approach

### 9. **Heap Operations** ⭐ NEW
- Min-heap/max-heap data structure
- Heapify operation: O(n)
- Parent-child relationship maintenance
- Array-based tree representation

### 10. **Resource Allocation** ⭐ NEW
- Limited resource management (image pixels)
- Best-fit allocation strategy
- Priority-based resource distribution
- Efficient capacity utilization

---

## 📊 Technical Specifications

### Encryption
| Component | Technology | Details |
|-----------|------------|---------|
| **Algorithm** | AES-256-CBC | 256-bit key, Cipher Block Chaining |
| **Authentication** | HMAC-SHA256 | Message authentication code |
| **Key Derivation** | PBKDF2 | 100,000 iterations, SHA-256 |
| **Salt** | Random 16 bytes | Unique per encryption |
| **IV** | Random 16 bytes | Initialization vector |

### Steganography
| Component | Technology | Complexity |
|-----------|------------|------------|
| **Method** | LSB (Least Significant Bit) | Invisible to human eye |
| **Selection** | Priority Queue | O(log n) per pixel |
| **Queue Build** | Heap construction | O(n log n) |
| **Priority Factors** | Complexity, Entropy, Edge | Weighted scoring |
| **Capacity** | 3 bits per pixel (RGB) | ~12.5% of image size |

### Performance
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Build Priority Queue | O(n log n) | O(n) |
| Select Pixel | O(log n) | O(1) |
| Hide Data | O(m log n) | O(n) |
| Extract Data | O(n log n) | O(n) |

*Where n = total pixels, m = data bits*

---

## 🧪 Testing

### Run Priority Queue Tests
```bash
cd src
python test_priority_steganography.py
```

**Output:**
```
TEST 1: IMAGE PRIORITY ANALYSIS
  - Analyzes pixel complexity distribution
  - Shows high/medium/low priority percentages

TEST 2: HIDING DATA WITH PRIORITY QUEUE
  - Builds priority queue (O(n log n))
  - Hides data in optimal pixels
  - Reports selection statistics

TEST 3: EXTRACTING AND VERIFYING DATA
  - Rebuilds priority queue
  - Extracts hidden data
  - Verifies data integrity

✅ All tests passed
```

### Manual Testing

**Test Priority-Based Steganography:**
1. Create test image: `test_image.png`
2. Run: `python main.py`
3. Choose: Encrypt → Hide in image
4. Observe: Priority queue building process
5. Decrypt and verify data integrity

---

## 📚 Usage Examples

### Example 1: Basic Encryption
```bash
python main.py
# 1. Choose: 1 (Encrypt)
# 2. Dual password? n
# 3. File: document.pdf
# 4. Password: MySecure123
# 5. Self-destruct? n
# 6. Hide in image? n
# Result: document.pdf.enc
```

### Example 2: Complete Security Stack
```bash
python main.py
# 1. Choose: 1 (Encrypt)
# 2. Dual password? y
#    - Real file: secret.txt
#    - Fake file: homework.txt
#    - Real password: RealSecret999
#    - Fake password: FakeHomework123
# 3. Self-destruct? y
#    - Max views: 3
#    - Expiry: 2025-12-31 23:59:59
# 4. Hide in image? y
#    - Cover image: vacation.png
# Result: secret.txt.dual.enc hidden in vacation.png
```

### Example 3: Decryption
```bash
python main.py
# 1. Choose: 2 (Decrypt)
# 2. File: vacation.png
# 3. Is steganography? y
# 4. Password: FakeHomework123 (or RealSecret999)
# Result: Shows corresponding file content
```

---

## 📈 Performance Benchmarks

### Test Environment
- CPU: Intel i5 @ 2.5GHz
- RAM: 8GB
- OS: Windows 10 / Ubuntu 20.04

### Results

| Image Size | Pixels | Queue Build | Hide 10KB | Total Time |
|------------|--------|-------------|-----------|------------|
| 100×100 | 10,000 | 0.08s | 0.12s | 0.20s |
| 500×500 | 250,000 | 2.3s | 3.0s | 5.3s |
| 1000×1000 | 1M | 11.5s | 13.8s | 25.3s |
| 2000×2000 | 4M | 52.1s | 61.3s | 113.4s |

**Note:** Priority-based method is ~6× slower than sequential, but significantly more secure.

---

## 🎓 Educational Value

### For Students
- Practical implementation of OS concepts
- Real-world application of data structures
- Algorithm complexity analysis
- Security principles in practice

### For Instructors
- Demonstrable OS scheduling concepts
- Priority queue and heap operations
- Resource allocation strategies
- Performance vs. security trade-offs

---

## 🎓 Course Information

**Project Title:** Secure File Encryption Tool with Priority Queue Implementation  
**Course:** Operating Systems  
**Institution:** RV College of Engineering, Bengaluru  
**Academic Year:** 2024-2025  

### Team Member
- **Aayushi Priya** [1RV24IS005]

### Guidance
- **Course Instructor:** [Professor Name]
- **Department:** Computer Science & Engineering

---

## 🚀 Demo Instructions

### For Teacher Demonstration

**1. Show Web Interface (2 minutes)**
- Open: https://aayu2810.github.io/file-encryption-tool/
- Navigate through feature cards
- Demonstrate drag-and-drop encryption

**2. Show Priority Queue (5 minutes)**
```bash
cd src
python test_priority_steganography.py
```
- Explain priority calculation
- Show heap operations
- Compare to OS scheduling

**3. Show Complete Features (3 minutes)**
```bash
python main.py
```
- Encrypt with all features
- Decrypt with dual password
- Show self-destruct in action

---

## 📖 Documentation

### Detailed Explanations
- **[PRIORITY_QUEUE_EXPLANATION.md](PRIORITY_QUEUE_EXPLANATION.md)** - Complete OS concepts documentation
- **[Code Comments](src/)** - Inline documentation in all Python files
- **[README.md](README.md)** - This file (overview)

### Key Concepts Explained
1. How priority queue mimics OS scheduling
2. Heap operations and complexity
3. Priority calculation formula
4. Resource allocation strategy
5. Performance analysis

---

## 🔮 Future Enhancements

### Planned Features
- [ ] Multi-threading for faster image processing
- [ ] GPU acceleration for large images
- [ ] Advanced scheduling algorithms (Round Robin, MLFQ)
- [ ] Memory-mapped file I/O
- [ ] Process synchronization with semaphores
- [ ] Deadlock prevention mechanisms
- [ ] Real-time progress monitoring
- [ ] Batch processing support

### Advanced OS Concepts
- [ ] Inter-process communication (IPC)
- [ ] Shared memory implementation
- [ ] Mutex and semaphore usage
- [ ] Thread pool management
- [ ] Virtual memory concepts

---

## 🤝 Contributing

This is an academic project. For suggestions:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open Pull Request

---

## 📜 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 📧 Contact

**Aayushi Priya**  
RV College of Engineering  
Email: [Your Email]  
GitHub: [@Aayu2810](https://github.com/Aayu2810)  
LinkedIn: [Your LinkedIn]

---

## 🙏 Acknowledgments

- **RV College of Engineering** - Operating Systems Course
- **Python Cryptography Library** - Encryption implementation
- **Python heapq Module** - Priority queue implementation
- **Pillow (PIL)** - Image processing
- **NumPy** - Numerical computations
- **CryptoJS** - Web encryption
- **Open Source Community** - Various tools and libraries

---

## ⭐ Show Your Support

If you find this project helpful for learning OS concepts, please consider:
- ⭐ Starring the repository
- 🔄 Sharing with classmates
- 📝 Providing feedback
- 🐛 Reporting issues

---

## 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/Aayu2810/file-encryption-tool?style=social)
![GitHub forks](https://img.shields.io/github/forks/Aayu2810/file-encryption-tool?style=social)
![GitHub issues](https://img.shields.io/github/issues/Aayu2810/file-encryption-tool)
![Lines of code](https://img.shields.io/tokei/lines/github/Aayu2810/file-encryption-tool)

---

## 🎯 Key Takeaways

### What Makes This Project Unique?

✅ **Real OS Concepts** - Not just theory, practical implementation  
✅ **Priority Queue** - Similar to CPU scheduling algorithms  
✅ **Performance Analysis** - Time/space complexity measurements  
✅ **Security + Education** - Both practical and educational  
✅ **Multiple Interfaces** - Web and CLI versions  

### OS Concepts Connection
```
Priority Queue in CPU Scheduling    →    Priority Queue in Steganography
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ready Queue (processes)             →    Priority Queue (pixels)
Process Priority (burst time)       →    Pixel Priority (complexity)
CPU Time Allocation                 →    Data Bit Allocation
Scheduler Selects Process           →    Algorithm Selects Pixel
O(log n) Selection                  →    O(log n) Selection
Highest Priority First              →    Highest Priority First
```

---

**Made with ❤️ for Operating Systems Course**  
**RV College of Engineering | 2024-25**

---

**Last Updated:** November 2024  
**Version:** 2.0 (with Priority Queue Implementation)
