## Cache Table Updater

The Cache Table Updater is a Python application built using the Tkinter library for GUI development. It allows users to visualize and analyze cache behavior with different access patterns using an 8-way Block Set-Associative cache with LRU(Least Recently Used).

### Features

- **GUI Interface**: Provides a user-friendly graphical interface for interacting with the cache table and analyzing cache performance.
- **Cache Visualization**: Displays cache contents and age counters in a treeview format for easy visualization.
- **Sequence Selection**: Allows users to choose between sequential, random, or mid-repeat block sequences for cache access simulation.
- **Table Update**: Updates the cache table with new values based on the selected sequence.
- **Hit/Miss Analysis**: Tracks cache hits, misses, hit rate, miss rate, and calculates average memory access time (AMAT) and total memory access time (TMAT).
- **Export to File**: Exports the cache table contents to a text file for further analysis.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/cache-table-updater.git


# CSC512C-G02-Grp3-MCO2

# Cache Analysis: Sequential Sequence with 8-way Set-Associative Cache (LRU)

### Sequential Sequence Characteristics
- Sequential Access Pattern: Memory accesses occur in a predictable order, accessing contiguous memory locations.

### Cache Configuration
- 8-way Set-Associative Cache: Each set in the cache contains 8 blocks.
- LRU Replacement Policy: Evicts the least recently used block when a new block needs to be placed in a set that is already full.
- This will be the same with all the three test cases

## Analysis
1. **Cache Hits**
  - Initially, all cache sets are empty. As the sequential sequence is accessed, the cache fills up gradually.
  - Cache hits occur when the accessed block is present in the cache.
  - Due to the sequential access pattern and large block size, subsequent accesses to blocks within the same set are unlikely to result in cache hits.

2. **Cache Misses**
   - Cache misses occur when the accessed block is not present in the cache.
   - Initially, there will be cache misses as the cache is cold (empty).

3. **LRU Behavior**
   - Ensures that the least recently used block is evicted when needed.
   - Impacts cache performance based on access patterns and eviction decisions.
   - This will be the same with all the three test cases

5. **Performance Metrics**
   - **Hit Rate**: Expected to be low due to the sequential access pattern.
   - **Miss Rate**: Initially high, may decrease as the cache fills up or if the block size is low.
   - **Average Memory Access Time (AMAT)** and **Total Memory Access Time (TMAT)**: Affected by hit and miss rates, as well as cache access latency.

## Conclusion
Based on testing of sequential sequence using an 8-way set-associative cache with LRU replacement, we saw a high miss rate due to the sequential access pattern. Smaller block size and set size leads to increase hit rate.

# Cache Analysis: Random Sequence with 8-way Set-Associative Cache (LRU)

### Sequential Sequence Characteristics
- Random Access Pattern: Memory accesses occur in a non-predictable order, accessing memory locations randomly.

## Analysis
1. **Cache Hits**
  - Expected behavior: Hit rate influenced by the randomness of memory accesses.

2. **Cache Misses**
   - Expected behavior: Higher miss rate compared to sequential access due to the unpredictable access pattern.

3. **Performance Metrics**
   - **Hit Rate**: Influenced by the randomness of memory accesses.
   - **Miss Rate**: Expected to be higher due to randomness.
   - **Average Memory Access Time (AMAT)** and **Total Memory Access Time (TMAT)**: Affected by hit and miss rates, as well as cache access latency.

## Conclusion
Handling random access patterns in a cache environment requires careful consideration of cache size, replacement policy, and access characteristics, because of its unpredictable nature.

# Cache Analysis: Mid-Repeat Block Sequence with 8-way Set-Associative Cache (LRU)

### Mid-Repeat Block Sequence Characteristics
- Access Pattern: Mid-repeat blocks are accessed repeatedly within the sequence, mimicking a combination of sequential and random access patterns.

## Analysis
1. **Cache Hits**
   - High hit rate compared with the two test cases
   - Expected behavior: Hit rate influenced by the repetition of mid-repeat blocks and the size of the cache.

2. **Cache Misses**
   - Expected behavior: Miss rate influenced by the non-sequential and repetitive access pattern.

5. **Performance Metrics**
   - **Hit Rate**: High due to repetition of mid-repeat blocks and cache size.
   - **Miss Rate**: Affected by the repetitive access pattern and cache capacity.
   - **Average Memory Access Time (AMAT)** and **Total Memory Access Time (TMAT)**: Determined by hit and miss rates, as well as cache access latency and eviction behavior.

## Conclusion
Mid-Repeat Block Sequence compared with the two test cases elicit higher hit rate.


