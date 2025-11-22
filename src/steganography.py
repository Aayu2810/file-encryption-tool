from PIL import Image
import os

class Steganography:
    def __init__(self):
        self.delimiter = b"<<<END_OF_DATA>>>"  # Marker to identify end of hidden data
    
    def encode_data_in_image(self, image_path, data, output_path):
        """Hide encrypted data inside an image using LSB steganography"""
        try:
            # Open the cover image
            img = Image.open(image_path)
            
            # Convert to RGB if not already
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Get image dimensions
            width, height = img.size
            max_bytes = (width * height * 3) // 8  # 3 color channels, 8 bits per byte
            
            # Add delimiter to mark end of data
            data_with_delimiter = data + self.delimiter
            
            # Check if image is large enough
            if len(data_with_delimiter) > max_bytes:
                return False, f"Image too small! Need at least {len(data_with_delimiter)} bytes, but image can hold {max_bytes} bytes"
            
            # Convert data to binary
            binary_data = ''.join(format(byte, '08b') for byte in data_with_delimiter)
            data_len = len(binary_data)
            
            # Load pixel data
            pixels = list(img.getdata())
            new_pixels = []
            
            data_index = 0
            
            for pixel in pixels:
                # Each pixel has 3 values (R, G, B)
                new_pixel = list(pixel)
                
                for i in range(3):  # R, G, B
                    if data_index < data_len:
                        # Modify LSB (Least Significant Bit)
                        new_pixel[i] = (new_pixel[i] & 0xFE) | int(binary_data[data_index])
                        data_index += 1
                
                new_pixels.append(tuple(new_pixel))
                
                # Stop if all data is embedded
                if data_index >= data_len:
                    # Keep remaining pixels unchanged
                    new_pixels.extend(pixels[len(new_pixels):])
                    break
            
            # Create new image with hidden data
            stego_img = Image.new(img.mode, img.size)
            stego_img.putdata(new_pixels)
            
            # Save as PNG (lossless)
            if not output_path.lower().endswith('.png'):
                output_path += '.png'
            
            stego_img.save(output_path, 'PNG')
            
            return True, f"Data successfully hidden in image: {output_path}"
            
        except Exception as e:
            return False, f"Steganography encoding failed: {str(e)}"
    
    def decode_data_from_image(self, image_path):
        """Extract hidden data from an image"""
        try:
            # Open the stego image
            img = Image.open(image_path)
            
            # Convert to RGB if needed
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Load pixel data
            pixels = list(img.getdata())
            
            # Extract binary data from LSBs
            binary_data = ''
            
            for pixel in pixels:
                for i in range(3):  # R, G, B
                    binary_data += str(pixel[i] & 1)  # Get LSB
            
            # Convert binary to bytes
            all_bytes = bytearray()
            for i in range(0, len(binary_data), 8):
                byte = binary_data[i:i+8]
                if len(byte) == 8:
                    all_bytes.append(int(byte, 2))
            
            # Find delimiter
            delimiter_index = all_bytes.find(self.delimiter)
            
            if delimiter_index == -1:
                return False, "No hidden data found in image"
            
            # Extract actual data (before delimiter)
            extracted_data = bytes(all_bytes[:delimiter_index])
            
            return True, extracted_data
            
        except Exception as e:
            return False, f"Steganography decoding failed: {str(e)}"
    
    def get_image_capacity(self, image_path):
        """Calculate how many bytes can be hidden in an image"""
        try:
            img = Image.open(image_path)
            width, height = img.size
            capacity = (width * height * 3) // 8  # 3 RGB channels, 8 bits per byte
            return capacity
        except:
            return 0


# Test the module
if __name__ == "__main__":
    steg = Steganography()
    
    print("Testing Steganography Module...")
    print("Note: You need a test image (test_image.png) to run this test")
    
    # Example usage
    test_data = b"This is secret encrypted data hidden in an image!"
    
    # To test, you would need:
    # 1. A cover image: test_image.png
    # 2. steg.encode_data_in_image("test_image.png", test_data, "output_stego.png")
    # 3. steg.decode_data_from_image("output_stego.png")
    
    print("\n✓ Steganography module loaded successfully")
    print("  - Use encode_data_in_image() to hide data")
    print("  - Use decode_data_from_image() to extract data")