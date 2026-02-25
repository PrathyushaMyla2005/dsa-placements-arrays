'''
Find the Majority Element that occurs more than N/2 times
Problem Statement: Given an integer array nums of size n, return the majority element of the array.
The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.
example 1:
Input: nums = [3,2,3]
Output: 3'''
def majorityelement(nums): # function definition
    n = len(nums) # length of the input array
    for i in range(n): # iterate through the array
        count = 0 # initialize count for the current element
        for j in range(n): # iterate through the array again to count occurrences
           if nums[i] == nums[j]: # if the current element matches the element at index j
               count += 1 # increment the count
        if count > n/2: # if the count exceeds n/2, we have found the majority element
            return nums[i] # return the majority element
nums = [3,2,3,7,7,7,7] # given input array
print("Majority element:", majorityelement(nums)) # call function and print the majority element    
'''Time Complexity: O(n^2) where n is the number of elements in the array as we are using two nested loops to count occurrences of each element.
Space Complexity: O(1) as we are using only a constant amount of extra space to store the count variable.'''
#optimal solution 
def majorityelement(nums): # function definition
    count = 0 # initialize count for the current candidate
    candidate = None # initialize candidate for majority element
    for num in nums: # iterate through the array
        if count == 0: # if count is 0, we need to choose a new candidate
            count = 1 # reset count to 1 for the new candidate
            candidate = num # set the new candidate
        elif num == candidate: # if the current number matches the candidate
            count += 1 # increment the count for the candidate
        else: # if the current number does not match the candidate
            count -= 1 # decrement the count for the candidate
    return candidate # return the majority element
nums = [3,2,3,7,7,7,7] # given input array
print("Majority element:", majorityelement(nums)) # call function and print the majority element
'''Time Complexity: O(n) where n is the number of elements in the array as we are iterating through the array once to find the majority element.
Space Complexity: O(1) as we are using only a constant amount of extra space to store the count and candidate variables.'''