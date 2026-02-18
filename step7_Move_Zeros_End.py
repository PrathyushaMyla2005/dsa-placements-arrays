'''Move all Zeros to the end of the array
Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.'''
# function definition to move all zeroes to end
def moveZeroes(arr):
    # index variable tells where next non-zero element should be placed
    index = 0
    # loop through each element of array using index i
    for i in range(len(arr)):
        # check if current element is not zero
        if arr[i] != 0:
            # place the non-zero element at 'index' position
            arr[index] = arr[i]
            # move index to next position
            index += 1
    # after placing all non-zero elements,
    # fill remaining positions with zero
    for i in range(index, len(arr)):
        # assign zero to remaining positions
        arr[i] = 0
    # return final updated array
    return arr
# main program starts here
# create array
arr = [0, 1, 0, 3, 12]
# call function and store result
result = moveZeroes(arr)
# print the final array
print("Array after moving zeroes:", result)
'''Time Complexity: O(n) where n is the number of elements in the array as we are iterating through the array twice
Space Complexity: O(1) as we are using only a constant amount of extra space for the index variable'''
# function definition
def moveZeroes(arr):
    # index keeps track of position to place next non-zero element
    index = 0
    # loop through the array
    for i in range(len(arr)):
        # check if current element is non-zero
        if arr[i] != 0:
            # swap current element with element at index
            arr[i], arr[index] = arr[index], arr[i]
            # move index to next position
            index += 1
    # return updated array
    return arr
# main
arr = [0, 1, 0, 3, 12]
print(moveZeroes(arr))
'''Time Complexity: O(n) where n is the number of elements in the array as we are iterating through the array once
Space Complexity: O(1) as we are using only a constant amount of extra space for
the index variable and performing in-place swaps'''

