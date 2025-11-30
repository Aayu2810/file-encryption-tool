from PIL import Image
import os
import heapq
import numpy as np

class SteganographyWithPriority:
    def __init__(self):
        self.delimiter = b"<<<END_OF_DATA>>>"
    
    def calculate_pixel_priority(self, img_array, x, y, width, height):
        """
        Calculate priority for a pixel based on:
        1. Local complexity (difference from neighbors)
        2. LSB entropy (randomness)
        3. Distance from edges
        
        Returns: Priority score (0.0 to 1.0)
        Higher score = better for hiding data
        """
        # 1. COMPLEXITY: Average difference from 8 neighbors
        complexity = 0
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    neighbors.append(img_array[ny, nx])
        
        if neighbors:
            pixel_value = np.mean(img_array[y, x])
            neighbor_avg = [np.mean(n) for n in neighbors]
            complexity = np.mean([abs(int(neighbor_avg[i]) - int(pixel_value)) for i in range(len(neighbor_avg))])
            complexity = min(complexity / 255.0, 1.0)
        
        # 2. ENTROPY: Randomness of LSB
        r, g, b = img_array[y, x]
        lsb_sum = (r & 1) + (g & 1) + (b & 1)
        entropy = abs(lsb_sum - 1.5) / 1.5
        
        # 3. EDGE DISTANCE: Distance from image edges
        edge_x = min(x, width - x) / (width / 2)
        edge_y = min(y, height - y) / (height / 2)
        edge_distance = (edge_x + edge_y) / 2
        
        # CALCULATE FINAL PRIORITY (Weighted sum)
        priority = (complexity * 0.4) + (entropy * 0.3) + (edge_distance * 0.3)
        
        return priority
    
    def build_priority_queue(self, img):
        """
        Build a priority queue of all pixels
        Returns: Heap with (-priority, x, y) tuples
        """
        width, height = img.size
        img_array = np.array(img)
        
        priority_queue = []
        
        print("📊 Building priority queue (analyzing image complexity)...")
        
        for y in range(height):
            for x in range(width):
                priority = self.calculate_pixel_priority(img_array, x, y, width, height)
                # Use negative priority for max-heap behavior
                heapq.heappush(priority_queue, (-priority, x, y))
            
            if y % (height // 10) == 0:
                print(f"   Progress: {int(y/height*100)}%")
        
        print(f"✓ Priority queue built with {len(priority_queue)} pixels")
        return priority_queue
    
    def encode_data_in_image(self, image_path, data, output_path):
        """
        Hide encrypted data in image using PRIORITY-BASED pixel selection
        """
        try:
            print("\n🔒 PRIORITY-BASED STEGANOGRAPHY")
            print("="*50)
            
            img = Image.open(image_path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            width, height = img.size
            data_with_delimiter = data + self.delimiter
            
            max_bytes = (width * height * 3) // 8
            if len(data_with_delimiter) > max_bytes:
                return False, f"Image too small! Need {len(data_with_delimiter)} bytes, capacity {max_bytes} bytes"
            
            binary_data = ''.join(format(byte, '08b') for byte in data_with_delimiter)
            data_len = len(binary_data)
            
            print(f"📄 Data size: {len(data_with_delimiter)} bytes")
            print(f"🖼️ Image capacity: {max_bytes} bytes")
            print(f"📊 Usage: {len(data_with_delimiter)/max_bytes*100:.1f}%")
            
            priority_queue = self.build_priority_queue(img)
            
            pixels = list(img.getdata())
            new_pixels = list(pixels)
            
            print("\n🔐 Hiding data in high-priority pixels...")
            data_index = 0
            pixels_used = 0
            
            while data_index < data_len and priority_queue:
                neg_priority, x, y = heapq.heappop(priority_queue)
                pixel_index = y * width + x
                pixel = list(new_pixels[pixel_index])
                
                for i in range(3):
                    if data_index < data_len:
                        pixel[i] = (pixel[i] & 0xFE) | int(binary_data[data_index])
                        data_index += 1
                
                new_pixels[pixel_index] = tuple(pixel)
                pixels_used += 1
                
                if pixels_used % 1000 == 0:
                    print(f"   Hidden: {data_index}/{data_len} bits ({data_index/data_len*100:.1f}%)")
            
            print(f"✓ Data hidden in {pixels_used} pixels (priority-based selection)")
            
            stego_img = Image.new(img.mode, img.size)
            stego_img.putdata(new_pixels)
            
            if not output_path.lower().endswith('.png'):
                output_path += '.png'
            
            stego_img.save(output_path, 'PNG')
            
            return True, f"Data successfully hidden using priority queue in: {output_path}"
            
        except Exception as e:
            return False, f"Steganography encoding failed: {str(e)}"
    
    def decode_data_from_image(self, image_path):
        """
        Extract hidden data from image
        """
        try:
            print("\n🔍 EXTRACTING DATA FROM IMAGE")
            print("="*50)
            
            img = Image.open(image_path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            width, height = img.size
            
            print("📊 Rebuilding priority queue...")
            priority_queue = self.build_priority_queue(img)
            
            pixels = list(img.getdata())
            
            print("\n🔓 Extracting hidden bits...")
            binary_data = ''
            delimiter_binary = ''.join(format(byte, '08b') for byte in self.delimiter)
            
            pixels_processed = 0
            
            while priority_queue:
                neg_priority, x, y = heapq.heappop(priority_queue)
                pixel_index = y * width + x
                pixel = pixels[pixel_index]
                
                for i in range(3):
                    binary_data += str(pixel[i] & 1)
                
                pixels_processed += 1
                
                if pixels_processed % 1000 == 0:
                    if delimiter_binary in binary_data:
                        print(f"✓ Delimiter found after {pixels_processed} pixels!")
                        break
            
            delimiter_pos = binary_data.find(delimiter_binary)
            
            if delimiter_pos == -1:
                return False, "No hidden data found or delimiter not detected"
            
            binary_data = binary_data[:delimiter_pos]
            
            all_bytes = bytearray()
            for i in range(0, len(binary_data), 8):
                byte = binary_data[i:i+8]
                if len(byte) == 8:
                    all_bytes.append(int(byte, 2))
            
            extracted_data = bytes(all_bytes)
            print(f"✓ Extracted {len(extracted_data)} bytes")
            return True, extracted_data
            
        except Exception as e:
            return False, f"Steganography decoding failed: {str(e)}"
    
    def get_image_capacity(self, image_path):
        """Calculate storage capacity"""
        try:
            img = Image.open(image_path)
            width, height = img.size
            capacity = (width * height * 3) // 8
            return capacity
        except:
            return 0
    
    def analyze_image_priority_distribution(self, image_path):
        """
        Analyze and display priority distribution
        """
        img = Image.open(image_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        priority_queue = self.build_priority_queue(img)
        priorities = [-p for p, x, y in priority_queue]
        
        print("\n📊 PRIORITY DISTRIBUTION ANALYSIS")
        print("="*50)
        print(f"Total pixels: {len(priorities)}")
        print(f"Average priority: {np.mean(priorities):.3f}")
        print(f"Std deviation: {np.std(priorities):.3f}")
        print(f"Min priority: {np.min(priorities):.3f}")
        print(f"Max priority: {np.max(priorities):.3f}")
        
        high_priority = sum(1 for p in priorities if p > 0.7)
        medium_priority = sum(1 for p in priorities if 0.3 <= p <= 0.7)
        low_priority = sum(1 for p in priorities if p < 0.3)
        
        print(f"\nPriority Distribution:")
        print(f"  High (>0.7):      {high_priority:6d} pixels ({high_priority/len(priorities)*100:5.1f}%)")
        print(f"  Medium (0.3-0.7): {medium_priority:6d} pixels ({medium_priority/len(priorities)*100:5.1f}%)")
        print(f"  Low (<0.3):       {low_priority:6d} pixels ({low_priority/len(priorities)*100:5.1f}%)")


if __name__ == "__main__":
    steg = SteganographyWithPriority()
    
    print("✓ Priority-Based Steganography Module Loaded")
    print("\nOS Concepts Demonstrated:")
    print("  • Priority Queue (heapq)")
    print("  • Scheduling Algorithms")
    print("  • Resource Allocation")
    print("  • Data Structure Management")
