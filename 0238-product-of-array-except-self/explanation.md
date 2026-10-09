# Product of Array Except Self

**Problem:** #238
**Difficulty:** Medium
**Language:** Python

## Algorithm

**Prefix and Suffix Product Arrays**

The student implemented an approach that uses two separate arrays to store the product of all elements to the left and all elements to the right of each index. In a single loop moving forward and backward simultaneously, it builds the left product array and the right product array. Finally, it multiplies the corresponding left and right products for each index to get the result.

## Step-by-step

1. Initialize the length of the input array nums as n, and start variables lmul and rmul at 1.
2. Create two arrays l and r of size n initialized with zeros to store the left and right products respectively.
3. Loop from i = 0 to n - 1, calculating negative index j = -i - 1.
4. Assign the current left multiplier lmul to l[i] and the current right multiplier rmul to r[j].
5. Update lmul by multiplying it with nums[i], and update rmul by multiplying it with nums[j].
6. Create an empty answer array and populate it by multiplying the corresponding elements of array l and array r at each index.
7. Return the final answer array.

## Time Complexity

**O(n)**

## Space Complexity

**O(n)**

## Key Concept

Prefix Sums / Products
