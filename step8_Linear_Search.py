'''linear search is a simple search algorithm that checks each element in the list one by one until it finds the target element or reaches the end of the list. It is also known as sequential search.
Example 1:
Input: arr = [1, 2, 3, 4, 5], target = 3
Output: 2 (the index of the target element in the array)
'''
def linear_search(arr, target):
    for i in range(len(arr)): # Iterate through each element in the array
        if arr[i] == target: # Check if the current element is equal to the target
            return i # If found, return the index of the target element
    return -1 # If not found, return -1 to indicate that the target element is not in the array
# Test the function
arr = [1, 2, 3, 4, 5]
target = 3
print(linear_search(arr, target))