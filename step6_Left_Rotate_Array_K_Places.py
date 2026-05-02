'''find the left rotate array by k positions
Given an array of integers and a number k, rotate the array to the left by k positions.
Example 1:
Input: [1, 2, 3, 4, 5], k = 2
Output: [3, 4, 5, 1, 2]'''   
def left_rotate_array_k_places(arr, k):
    n = len(arr) #get the length of the array
    k = k % n # Handle cases where k is greater than the length of the array
    # Step 1: Reverse the first k elements
    arr[:k] = arr[:k][::-1] # Reverse the first k elements of the array
    # Step 2: Reverse the remaining n-k elements
    arr[k:] = arr[k:][::-1] # Reverse the remaining n-k elements of the array
    # Step 3: Reverse the entire array
    arr[:] = arr[::-1] # Reverse the entire array to get the final rotated array
    return arr # Return the rotated array
# Test the function
arr = [1, 2, 3, 4, 5]
k = 2
print(left_rotate_array_k_places(arr, k))
'''tc: O(n) where n is the number of     elements in the array, as we are performing three reversals which each take O(n) time
sc: O(1) as we are performing the rotation in place without using any additional data structures
'''