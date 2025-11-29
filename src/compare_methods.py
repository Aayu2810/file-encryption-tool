"""
Compare sequential vs priority-based steganography
Shows performance and security trade-offs
"""

import time
from steganography import SteganographyWithPriority

def benchmark_priority_method(image_path, data_size_kb):
    """Benchmark the priority-based method"""
    steg = SteganographyWithPriority()
    
    # Create test data
    test_data = b"X" * (data_size_kb * 1024)
    
    print(f"\n{'='*60}")
    print(f"PRIORITY-BASED METHOD - {data_size_kb}KB data")
    print('='*60)
    
    start = time.time()
    success, message = steg.encode_data_in_image(
        image_path,
        test_data,
        f'output_priority_{data_size_kb}kb.png'
    )
    end = time.time()
    
    if success:
        print(f"\n✓ Success in {end-start:.2f} seconds")
    else:
        print(f"\n✗ Failed: {message}")
    
    return end - start

if __name__ == "__main__":
    print("STEGANOGRAPHY PERFORMANCE COMPARISON")
    print("="*60)
    
    # Test with different data sizes
    for kb in [1, 5, 10]:
        benchmark_priority_method('../test_image.png', kb)
```

---

### 4. **Add LICENSE File**

Create: `LICENSE`
```
MIT License

Copyright (c) 2024 Aayushi Priya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
