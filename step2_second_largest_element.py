"""
Find the Second Largest and Second Smallest Element in an Array

Time Complexity  : O(n)
Space Complexity : O(1)

Approach:
---------
Traverse the array only once.

For Second Largest:
    - Keep track of the largest element.
    - Keep track of the second largest element.

For Second Smallest:
    - Keep track of the smallest element.
    - Keep track of the second smallest element.
"""


# ---------------- SECOND LARGEST ---------------- #

def second_largest(arr):

    # If the array has fewer than 2 elements,
    # there is no second largest element.
    if len(arr) < 2:
        return None

    # Assume the first element is the largest.
    largest = arr[0]

    # Initialize second largest to negative infinity.
    # This ensures any real number will be larger.
    second_largest = float('-inf')

    # Traverse the array starting from the second element.
    for i in range(1, len(arr)):

        # Case 1:
        # Current element is greater than the largest.
        if arr[i] > largest:

            # Previous largest becomes second largest.
            second_largest = largest

            # Update largest.
            largest = arr[i]

        # Case 2:
        # Current element is not the largest,
        # but it is greater than the current second largest.
        # Also avoid duplicates.
        elif arr[i] > second_largest and arr[i] != largest:

            second_largest = arr[i]

    # If second largest is still -infinity,
    # it means no second largest exists.
    if second_largest == float('-inf'):
        return None

    return second_largest


# ---------------- SECOND SMALLEST ---------------- #

def second_smallest(arr):

    # If array has fewer than 2 elements,
    # second smallest does not exist.
    if len(arr) < 2:
        return None

    # Assume first element is the smallest.
    smallest = arr[0]

    # Initialize second smallest to positive infinity.
    second_smallest = float('inf')

    # Traverse from the second element.
    for i in range(1, len(arr)):

        # Case 1:
        # Current element is smaller than the smallest.
        if arr[i] < smallest:

            # Previous smallest becomes second smallest.
            second_smallest = smallest

            # Update smallest.
            smallest = arr[i]

        # Case 2:
        # Current element is greater than smallest,
        # but smaller than second smallest.
        # Ignore duplicates.
        elif arr[i] < second_smallest and arr[i] != smallest:

            second_smallest = arr[i]

    # If second smallest is still infinity,
    # it means no second smallest exists.
    if second_smallest == float('inf'):
        return None

    return second_smallest


# ---------------- DRIVER CODE ---------------- #

arr = [1, 2, 3, 4, 5]

print("Array :", arr)

print("Second Largest :", second_largest(arr))

print("Second Smallest :", second_smallest(arr))