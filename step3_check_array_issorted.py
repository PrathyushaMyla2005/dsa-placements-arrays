'''check if an array is sorted
Given an array of integers, check if the array is sorted in non-decreasing order.
Example 1:[1, 2, 3, 4, 5]
Output: True'''
def is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True
# Test the function
arr = [6, 4, 5]
print(is_sorted(arr))
'''tc: O(n) where n is the number of elements in the array
sc: O(1) as we are using only a constant amount of space to store the
'''
