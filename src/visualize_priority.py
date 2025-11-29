"""
Visualize priority distribution across image
Shows which areas have high/low priority
"""

from steganography import SteganographyWithPriority
from PIL import Image, ImageDraw
import numpy as np

def create_priority_heatmap(image_path, output_path):
    """Create visual heatmap of pixel priorities"""
    steg = SteganographyWithPriority()
    img = Image.open(image_path)
    
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    width, height = img.size
    img_array = np.array(img)
    
    # Calculate priorities for all pixels
    priority_map = np.zeros((height, width))
    
    print("Calculating priorities...")
    for y in range(height):
        for x in range(width):
            priority = steg.calculate_pixel_priority(img_array, x, y, width, height)
            priority_map[y][x] = priority
        
        if y % 50 == 0:
            print(f"Progress: {y}/{height}")
    
    # Normalize to 0-255
    priority_map = ((priority_map - priority_map.min()) / 
                    (priority_map.max() - priority_map.min()) * 255).astype(np.uint8)
    
    # Create heatmap (red = high priority, blue = low priority)
    heatmap = Image.new('RGB', (width, height))
    for y in range(height):
        for x in range(width):
            value = priority_map[y][x]
            # Red for high priority, Blue for low priority
            r = value
            g = 0
            b = 255 - value
            heatmap.putpixel((x, y), (r, g, b))
    
    heatmap.save(output_path)
    print(f"✓ Priority heatmap saved: {output_path}")

if __name__ == "__main__":
    create_priority_heatmap('../test_image.png', '../priority_heatmap.png')
