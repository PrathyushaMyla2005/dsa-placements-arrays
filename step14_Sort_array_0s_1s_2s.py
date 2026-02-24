'''Problem Statement: Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.'''
def sortColors(nums): # function definition
    count0 = 0 # count of 0s
    count1 = 0 # count of 1s
    count2 = 0 # count of 2s
    # count the number of 0s, 1s, and 2s in the array
    for num in nums:
        if num == 0: # if current number is 0
            count0 += 1 # increment count of 0s
        elif num == 1: # if current number is 1
            count1 += 1 # increment count of 1s
        else: # if current number is 2
            count2 += 1 # increment count of 2s
    # overwrite the original array with sorted order
    index = 0 # index to keep track of current position in array
    # place all 0s in the array
    for i in range(count0):
        nums[index] = 0 # assign 0 to current index
        index += 1 # move to next index
    # place all 1s in the array
    for i in range(count1):
        nums[index] = 1 # assign 1 to current index
        index += 1 # move to next index
    # place all 2s in the array
    for i in range(count2):
        nums[index] = 2 # assign 2 to current index
        index += 1 # move to next index
# main program starts here
nums = [2, 0, 2, 1, 1, 0] # given array
sortColors(nums) # call function to sort the array
print("Sorted array:", nums) # print the sorted array
'''Time Complexity: O(n) where n is the number of elements in the array as we are iterating through the array twice (once for counting and once for overwriting).
Space Complexity: O(1) as we are using only a constant amount of extra space to store the counts and index variable.'''
def sortColors(nums): # function definition
    low = 0 # pointer for the next position of 0
    mid = 0 # pointer for the current element
    high = len(nums) - 1 # pointer for the next position of 2
    while mid <= high: # loop until mid pointer is less than or equal to high pointer
        if nums[mid] == 0: # if current element is 0
            nums[low], nums[mid] = nums[mid], nums[low] # swap 0 with the element at low pointer
            low += 1 # move low pointer to the right
            mid += 1 # move mid pointer to the right
        elif nums[mid] == 1: # if current element is 1
            mid += 1 # move mid pointer to the right
        else: # if current element is 2
            nums[mid], nums[high] = nums[high], nums[mid] # swap 2 with the element at high pointer
            high -= 1 # move high pointer to the left
nums = [0,1,2,0,0,1]
print ("Original array:", nums) # print the original array
sortColors(nums) # call function to sort the array
print("Sorted array:", nums) # print the sorted array
