# Priority Queue Implementation in Steganography

## 📚 Project Information

**Student:** Aayushi Priya [1RV24IS005]  
**Course:** Operating Systems  
**Institution:** RV College of Engineering  
**Academic Year:** 2024-2025

---

## 🎯 Objective

Implement Operating System scheduling concepts through a priority-based pixel selection algorithm for steganographic data hiding, demonstrating:
- Priority Queue data structure
- Scheduling algorithms
- Resource allocation strategies
- Heap operations

---

## 📊 OS Concepts Demonstrated

### 1. Priority Queue (Data Structure)

**Definition:** A queue where each element has an associated priority, and elements are served based on priority rather than insertion order.

**In Operating Systems:**
- Process ready queue (CPU scheduling)
- I/O request queue
- Interrupt handling queue
- Memory page replacement

**In Our Project:**
- Each pixel has a calculated priority score
- Higher priority pixels are selected first
- Implemented using Python's `heapq` module (min-heap)
- Efficient O(log n) insertion and extraction

**Operations:**
```python
Insert:       O(log n)    # heapq.heappush()
Extract-Max:  O(log n)    # heapq.heappop()
Peek:         O(1)        # queue[0]
Build:        O(n log n)  # heapify all elements
```

---

### 2. Scheduling Algorithm

**Type:** Priority-Based Scheduling (Non-Preemptive)

**Similar OS Algorithms:**
- Priority Scheduling
- Shortest Job First (SJF)
- Multilevel Queue Scheduling

**Algorithm Steps:**
```
1. Analyze all pixels and calculate priority (O(n))
2. Build priority queue using heap (O(n log n))
3. While data remains to hide:
   a. Extract highest priority pixel (O(log n))
   b. Hide data bits in that pixel
   c. Continue until all data hidden
```

**Comparison Table:**

| Aspect | OS Process Scheduling | Steganography |
|--------|----------------------|---------------|
| Queue Type | Ready Queue | Pixel Priority Queue |
| Element | Process | Pixel (x, y coordinates) |
| Priority Basis | CPU burst time, I/O | Complexity, Entropy, Location |
| Resource | CPU time | Data bits |
| Selection | Highest priority process | Highest priority pixel |
| Execution | Run process | Hide data in pixel |

---

### 3. Resource Allocation

**Resources:** Image pixels (limited capacity based on image size)

**Allocation Strategy:**
1. **Analysis Phase:** Evaluate resource quality (pixel suitability)
2. **Priority Assignment:** Calculate scores for all resources
3. **Allocation:** Assign data to best resources first
4. **Optimization:** Efficient use of available capacity

**Analogous to OS:**
- Memory allocation (best-fit, first-fit algorithms)
- Disk scheduling (shortest seek time first)
- Network bandwidth allocation
- Cache replacement policies

---

### 4. Heap Data Structure

**Implementation:** Binary Min-Heap (array-based)

**Properties:**
- Complete binary tree structure
- Heap property: Parent ≤ Children (min-heap)
- Array representation: Parent at i, children at 2i+1 and 2i+2
- Efficient operations without explicit tree structure

**Heap Visualization:**
```
Array: [0.15, 0.32, 0.28, 0.45, 0.67, 0.51, 0.39]

Tree representation:
         0.15
        /    \
     0.32    0.28
     /  \    /  \
  0.45 0.67 0.51 0.39
```

**Operations Complexity:**
- Insert: O(log n) - Bubble up
- Extract-Min: O(log n) - Bubble down
- Peek: O(1) - Access root
- Heapify: O(n) - Build from array

---

## 🔢 Priority Calculation

### Formula
```
Priority = (Complexity × 0.4) + (Entropy × 0.3) + (Edge_Distance × 0.3)
```

### Factor 1: Complexity (40% weight)

**Measures:** Local pixel variation (difference from 8 neighbors)

**Calculation:**
```python
neighbors = get_8_neighbors(pixel)
differences = [abs(pixel_value - neighbor) for neighbor in neighbors]
complexity = mean(differences) / 255  # Normalize to [0, 1]
```

**Range:** 0.0 to 1.0
- 0.0 = Uniform area (sky, solid color)
- 0.5 = Moderate variation
- 1.0 = High variation (texture, edges, patterns)

**Why Important:**
- Complex areas mask data changes better
- Statistical analysis less effective in noisy regions
- Human eye less sensitive to changes in complex areas

**Example:**
```
Sky pixel (uniform blue):
  Neighbors: [100, 100, 100, 100, 101, 100, 100, 100]
  Complexity: ~0.01 (very uniform)

Tree bark pixel (textured):
  Neighbors: [85, 120, 95, 140, 75, 110, 90, 130]
  Complexity: ~0.85 (high variation)
```

---

### Factor 2: Entropy (30% weight)

**Measures:** Randomness of existing Least Significant Bits

**Calculation:**
```python
r_lsb = red_value & 1
g_lsb = green_value & 1
b_lsb = blue_value & 1
lsb_sum = r_lsb + g_lsb + b_lsb

# Ideal is random (average 1.5 out of 3)
entropy = abs(lsb_sum - 1.5) / 1.5
```

**Range:** 0.0 to 1.0
- 0.0 = All LSBs same (000 or 111) - very predictable
- 0.5 = Moderate randomness
- 1.0 = Ideal randomness (average distribution)

**Why Important:**
- Natural randomness in LSBs hides our modifications
- Already-random LSBs less suspicious when changed
- Avoids creating patterns in LSB plane

---

### Factor 3: Edge Distance (30% weight)

**Measures:** Distance from image edges

**Calculation:**
```python
distance_from_left = x
distance_from_right = width - x
distance_from_top = y
distance_from_bottom = height - y

edge_x = min(distance_from_left, distance_from_right) / (width / 2)
edge_y = min(distance_from_top, distance_from_bottom) / (height / 2)
edge_distance = (edge_x + edge_y) / 2
```

**Range:** 0.0 to 1.0
- 0.0 = At image corner
- 0.5 = Midway between edge and center
- 1.0 = Center of image

**Why Important:**
- Edge/corner pixels less scrutinized by human viewers
- Center pixels more important for image composition
- Cropping often removes edges, less risk of data loss

---

### Combined Example

**Sky Pixel (uniform area):**
```
Position: (100, 50) in 500×500 image
RGB: (135, 206, 235) - Light blue
Neighbors: All similar values

Complexity: 0.05 (very uniform)
Entropy: 0.33 (LSBs: 1,1,1)
Edge_Distance: 0.25 (near top edge)

Priority = (0.05 × 0.4) + (0.33 × 0.3) + (0.25 × 0.3)
         = 0.02 + 0.10 + 0.08
         = 0.20 (LOW PRIORITY - avoid hiding here)
```

**Textured Pixel (complex area):**
```
Position: (250, 250) in 500×500 image
RGB: (87, 142, 65) - Tree bark
Neighbors: Highly varied values

Complexity: 0.82 (high variation)
Entropy: 0.67 (LSBs: 1,1,0 - moderately random)
Edge_Distance: 0.50 (center area)

Priority = (0.82 × 0.4) + (0.67 × 0.3) + (0.50 × 0.3)
         = 0.33 + 0.20 + 0.15
         = 0.68 (HIGH PRIORITY - excellent for hiding)
```

---

## 🔄 Algorithm Flow

### Phase 1: Priority Queue Construction
```
For each pixel (x, y) in image:
    1. Get 8 neighboring pixels
    2. Calculate complexity score
    3. Calculate entropy score
    4. Calculate edge distance score
    5. Compute weighted priority
    6. Insert (-priority, x, y) into heap
       (negative for max-heap behavior)

Time Complexity: O(n log n) where n = total pixels
Space Complexity: O(n) for storing queue
```

### Phase 2: Data Hiding
```
Initialize: data_index = 0
While data_index < total_data_bits AND queue not empty:
    1. Pop highest priority pixel from queue: O(log n)
       pixel = heappop(priority_queue)
       
    2. Extract RGB values from pixel
       
    3. For each color channel (R, G, B):
       a. Get current LSB
       b. Replace with data bit
       c. Increment data_index
       
    4. Update pixel in image
    
    5. Continue to next pixel

Total Time: O(m log n) where m = data bits, n = pixels
```

### Phase 3: Data Extraction
