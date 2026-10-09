# Sort Colors

**Problem:** #75
**Difficulty:** Medium
**Language:** Python

## Algorithm

**Selection Sort**

The student implemented a comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent or distant pairs of elements, and swaps them if they are in the wrong order until the entire list is sorted.

## Step-by-step

1. Find the length of the input array nums and store it in variable n.
2. Start an outer loop with index i from 0 to n-1.
3. Start an inner loop with index j from i+1 to n-1.
4. Compare the element at index j with the element at index i (nums[j] < nums[i]).
5. If nums[j] is smaller, swap the values of nums[i] and nums[j] using a temporary variable.
6. Repeat the process until the entire array is sorted in-place.

## Time Complexity

**O(n^2)**

## Space Complexity

**O(1)**

## Key Concept

Sorting
