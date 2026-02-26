'''Kadane's Algorithm : Maximum Subarray Sum in an Array
Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.'''
def maxsubarraysum(nums): # function definition
    maxi = float('-inf') # initialize maximum sum to negative infinity
    for i in range(len(nums)): # iterate through the array
        for j in range(i, len(nums)): # iterate through the array starting from index 
            sum = 0 
            for k in range(i, j+1): # iterate through the subarray from index i to j
                sum += nums[k] # calculate the sum of the current subarray
            maxi = max(maxi, sum) # update the maximum sum if the current sum is greater
    return maxi # return the maximum subarray sum
nums = [-2,1,-3,4,-1,2,1,-5,4] # given input array
print("Maximum subarray sum:", maxsubarraysum(nums)) # call function and print the maximum subarray sum
'''Time Complexity: O(n^3) where n is the number of elements in the array as we are using three nested loops to calculate the sum of all possible subarrays.
Space Complexity: O(1) as we are using only a constant amount of extra space to store the sum and maxi variables.'''
def maxsubarraysum(nums): # function definition
    maxi = float('-inf') # initialize maximum sum to negative infinity
    sum = 0 # initialize current sum to 0
    for i in range(len(nums)): # iterate through the array
        sum += nums[i] # add the current element to the current sum
        if sum > maxi: # if the current sum is greater than the maximum sum
            maxi = sum # update the maximum sum
        if sum < 0: # if the current sum is negative
            sum = 0 # reset the current sum to 0
    return maxi # return the maximum subarray sum
nums = [-2,1,-3,4,-1,2,1,-5,4] # given input array
print("Maximum subarray sum:", maxsubarraysum(nums)) # call function and print the maximum subarray sum
'''Time Complexity: O(n) where n is the number of elements in the array as we
    are iterating through the array once to find the maximum subarray sum
Space Complexity: O(1) as we are using only a constant amount of extra space to store the sum and maxi variables.'''
