'''find  the left rotate array by one position
Given an array of integers, rotate the array to the left by one position.
Example 1:
Input: [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]'''
def left_rotate_array(arr):
    first_element = arr[0] # Store the first element of the array
    for i in range(1,len(arr)): # Iterate through the array starting from the second element
        arr[i - 1] = arr[i] # Shift each element to the left by one position
    arr[len(arr) - 1] = first_element # Place the first element at the end of the array
    return arr # Return the rotated array
# Test the function
arr = [1, 2, 3, 4, 5]
print(left_rotate_array(arr))
'''tc: O(n) where n is the number of elements in the array
sc: O(1) as we are using only a constant amount of space to store the first element and perform the rotation in place
'''
