''' find the pivot index of an array, which is the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index. If no such index exists, return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
example = [1, 7, 3, 6, 5, 6]
o/p = 3'''
def pivot_index(nums):
    for i in range(len(nums)):
        left_sum = sum(nums[:i]) # sum of elements to the left of index i
        right_sum = sum(nums[i+1:]) # sum of elements to the right of
        if left_sum == right_sum:
            return i # return the pivot index
    return -1 # return -1 if no pivot index is found
# Example usage
example = [1, 7, 3, 6, 5, 6]
result = pivot_index(example)
print(result) # Output: 3
'''time complexity: O(n^2) because of the sum function being called for each index, which iterates through the array. Space complexity: O(1) since we are using a constant amount of extra space.
To optimize the time complexity to O(n), we can calculate the total sum of the array first and then iterate through the array while keeping track of the left sum. This way, we can calculate the right sum in constant time by subtracting the left sum and the current element from the total sum. Here's the optimized code:
space complexity: O(1) since we are using a constant amount of extra space.
'''