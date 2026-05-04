'''maximum subarray sum (Kadane's Algorithm)
kadane's algorithm is a dynamic programming algorithm that is used to find the maximum sum of a contiguous subarray in an array of integers. The algorithm works by iterating through the array and keeping track of the maximum sum of a subarray that ends at each index. The maximum sum of a subarray that ends at index i can be calculated as the maximum of the current element and the sum of the current element and the maximum sum of a subarray that ends at index i-1. The algorithm also keeps track of the overall maximum sum found so far.
different from the previous problems because we are not looking for a specific number or a specific condition, but we are looking for the maximum sum of a contiguous subarray.
kadane algo and difference from previous problems:
1. we are looking for the maximum sum of a contiguous subarray, not a specific number
2. we are using dynamic programming to keep track of the maximum sum of a subarray that ends at each index, not a dictionary to store the frequency of each number
example 1:
input arr = [-2,1,-3,4,-1,2,1,-5,4]
output 6 (the maximum sum of a contiguous subarray is [4,-1,2,1] which has a sum of 6)
'''
def max_subarray_sum(arr):
    max_sum = -float('inf')# initialize max_sum to negative infinity to handle cases where all elements are negative
    current_sum = 0 # initialize current_sum to 0
    for num in arr:
        current_sum += num # add the current number to current_sum
        if current_sum > max_sum: # if current_sum is greater than max_sum, update max_sum
            max_sum = current_sum
        if current_sum < 0: # if current_sum is negative, reset it to 0
            current_sum = 0
    return max_sum
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(arr))
'''tc O(n) because we traverse the array once and sc O(1) because we are using constant space to store the current_sum and max_sum'''