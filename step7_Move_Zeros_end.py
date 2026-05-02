'''move zeros to the end of the array
Given an array of integers, move all the zeros to the end of the array while maintaining the relative order of the non-zero elements.
Example 1:
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]'''
def move_zeros_to_end(arr):
    n = len(arr) # Get the length of the array
    j = 0 # Initialize a pointer j to keep track of the position of the next non-zero element
    for i in range(n):
        if arr[i] != 0:  #check the element is not zero
            arr[j],arr[i] = arr[i],arr[j]
            j += 1
    return arr
arr = [1,0,2,4,0,6]
print(move_zeros_to_end(arr))
      