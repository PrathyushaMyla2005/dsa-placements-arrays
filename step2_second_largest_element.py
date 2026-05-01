''' find the second largest element in an array 
Given an array of integers, find the second largest element in the array.
Example 1:
Input: [1, 2, 3, 4, 5]
Output: 4'''
def second_largest(arr):
    max = arr[0] # Initialize max to the first element of the array
    second_max = float('-inf') # Initialize second_max to negative infinity
    for i in range(1,len(arr)): # Iterate through the array starting from the second element
        if arr[i] > max[0]: # If the current element is greater than max
            second_max = max # Update second_max to the current max
            max = arr[i] # Update max to the current element
        elif arr[i] > second_max and arr[i] != max : # If the current element is greater than second_max and not equal to max
            second_max = arr[i] # Update second_max to the current element
    return second_max # Return the second largest element
# Test the function
arr = [1, 2, 3, 4, 5]
print(second_largest(arr))
'''tc: O(n) where n is the number of elements in the array
sc: O(1) as we are using only a constant amount of space to store the max and second_max
'''
