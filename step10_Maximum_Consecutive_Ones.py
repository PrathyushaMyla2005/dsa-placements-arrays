"""
Maximum Consecutive Ones

Problem:
--------
Given a binary array containing only 0's and 1's,
find the maximum number of consecutive 1's.

Example:
--------
Input  : [1,1,0,1,1,1]
Output : 3

Time Complexity  : O(n)
Space Complexity : O(1)
"""

def max_consecutive_ones(arr):

    # Stores the current consecutive count of 1's
    count = 0

    # Stores the maximum consecutive count found so far
    max_count = 0

    # Traverse every element in the array
    for num in arr:

        # If the current element is 1
        if num == 1:

            # Increase the current consecutive count
            count += 1

            # Update maximum if needed
            if count > max_count:
                max_count = count

        # If the current element is 0
        else:

            # Consecutive sequence breaks
            count = 0

    # Return the maximum consecutive 1's
    return max_count


# ---------------- DRIVER CODE ---------------- #

arr = [1,1,0,1,1,1]

print("Array :", arr)

print("Maximum Consecutive Ones :", max_consecutive_ones(arr))