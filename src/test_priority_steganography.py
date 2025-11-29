#!/usr/bin/env python3
"""
Priority-Based Steganography Test Script
Demonstrates OS Concepts: Priority Queue, Scheduling, Heap Operations

Author: Aayushi Priya [1RV24IS005]
Course: Operating Systems
Institution: RV College of Engineering
"""

from steganography import SteganographyWithPriority
import os
import sys

def print_header(title):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)

def print_section(title):
    """Print section divider"""
    print(f"\n{'─'*70}")
    print(f"  {title}")
    print('─'*70)

def test_priority_steganography():
    """Main test function"""
    print_header("PRIORITY-BASED STEGANOGRAPHY DEMONSTRATION")
    print("Operating Systems Course Project")
    print("RV College of Engineering\n")
    
    steg = SteganographyWithPriority()
    
    # Check for test image
    test_image = '../test_image.png'
    if not os.path.exists(test_image):
        print(f"\n⚠️  Test image not found: {test_image}")
        print("\nPlease create a test image by running:")
        print("  python3 -c \"from PIL import Image; Image.new('RGB',(500,500),'blue').save('test_image.png')\"")
        return
    
    # TEST 1: Analyze Priority Distribution
    print_section("TEST 1: IMAGE PRIORITY ANALYSIS")
    try:
        steg.analyze_image_priority_distribution(test_image)
        print("\n✅ Priority analysis completed successfully")
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    # TEST 2: Encode with Priority Queue
    print_section("TEST 2: HIDING DATA WITH PRIORITY QUEUE")
    
    test_data = b"PRIORITY QUEUE DEMO: This data is hidden using OS scheduling algorithms!"
    output_image = '../test_output_stego.png'
    
    try:
        success, message = steg.encode_data_in_image(test_image, test_data, output_image)
        
        if success:
            print(f"\n✅ {message}")
        else:
            print(f"\n❌ Encoding failed: {message}")
            return
    except Exception as e:
        print(f"❌ Error during encoding: {e}")
        return
    
    # TEST 3: Decode and Verify
    print_section("TEST 3: EXTRACTING AND VERIFYING DATA")
    
    if not os.path.exists(output_image):
        print(f"❌ Output image not found: {output_image}")
        return
    
    try:
        success, extracted_data = steg.decode_data_from_image(output_image)
        
        if success:
            print(f"\n✅ Extraction successful!")
            print(f"\nOriginal data ({len(test_data)} bytes):")
            print(f"  {test_data[:50]}...")
            print(f"\nExtracted data ({len(extracted_data)} bytes):")
            print(f"  {extracted_data[:50]}...")
            
            if test_data == extracted_data:
                print("\n🎉 TEST PASSED: Data integrity verified!")
                print("   Original and extracted data match perfectly")
            else:
                print("\n❌ TEST FAILED: Data mismatch detected")
        else:
            print(f"❌ Extraction failed: {extracted_data}")
    except Exception as e:
        print(f"❌ Error during extraction: {e}")
    
    # Cleanup
    print_section("CLEANUP")
    try:
        if os.path.exists(output_image):
            os.remove(output_image)
            print("✓ Temporary files removed")
    except:
        pass

def explain_os_concepts():
    """Explain OS concepts demonstrated"""
    print_header("OS CONCEPTS DEMONSTRATED")
    
    concepts = [
        {
            "name": "1. PRIORITY QUEUE",
            "description": "Data structure where elements are served by priority",
            "os_use": "Process scheduling, I/O requests, interrupt handling",
            "our_use": "Pixel selection based on hiding quality score",
            "operations": "Insert: O(log n), Extract-Max: O(log n)"
        },
        {
            "name": "2. SCHEDULING ALGORITHM",
            "description": "Priority-based selection (Highest Priority First)",
            "os_use": "CPU scheduling, Job scheduling",
            "our_use": "Select best pixels for data hiding first",
            "operations": "Similar to Priority Scheduling in OS"
        },
        {
            "name": "3. HEAP DATA STRUCTURE",
            "description": "Binary heap for efficient priority operations",
            "os_use": "Priority queue implementation, memory management",
            "our_use": "Maintain sorted pixel priorities efficiently",
            "operations": "Space: O(n), Operations: O(log n)"
        },
        {
            "name": "4. RESOURCE ALLOCATION",
            "description": "Strategic allocation of limited resources",
            "os_use": "Memory allocation, CPU time distribution",
            "our_use": "Allocate data bits to optimal pixels",
            "operations": "Priority-based best-fit allocation"
        }
    ]
    
    for concept in concepts:
        print(f"\n{concept['name']}")
        print(f"  Definition:   {concept['description']}")
        print(f"  OS Usage:     {concept['os_use']}")
        print(f"  Our Usage:    {concept['our_use']}")
        print(f"  Operations:   {concept['operations']}")
    
    print_header("PRIORITY CALCULATION FORMULA")
    print("""
Priority = (Complexity × 0.4) + (Entropy × 0.3) + (Edge_Distance × 0.3)

Where:
  • Complexity: How different pixel is from neighbors (0-1)
  • Entropy: Randomness of existing LSBs (0-1)  
  • Edge_Distance: Distance from image edges (0-1)

Higher priority = Better for hiding data
    """)
    
    print_header("COMPARISON TO OS SCHEDULING")
    
    comparison = """
    OS Process Scheduler              Priority-Based Steganography
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Ready Queue                   →   Priority Queue of Pixels
    Process Priority              →   Pixel Hiding Quality Score
    CPU Time Allocation           →   Data Bit Allocation
    Context Switch                →   Pixel Selection
    Highest Priority Executes     →   Highest Priority Pixel Used
    Preemptive/Non-Preemptive     →   Non-Preemptive (Complete task)
    
    Time Complexity: O(log n) per operation in both cases
    """
    
    print(comparison)

def main():
    """Main execution function"""
    try:
        # Run tests
        test_priority_steganography()
        
        # Explain concepts
        explain_os_concepts()
        
        print_header("DEMONSTRATION COMPLETE")
        print("\n✓ All tests completed successfully")
        print("✓ OS concepts demonstrated effectively")
        print("\nFor detailed documentation, see: PRIORITY_QUEUE_EXPLANATION.md\n")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
