'''Left Rotate the Array by One
Problem Statement: Given an integer array nums, rotate the array to the left by one.
Note: There is no need to return anything, just modify the given array'''
#optimal force approach
def leftRotateByOne(nums): #function to left rotate the array by one
    if not nums: #if the input array is empty, return
        return
    first = nums[0] #store the first element of the array in a variable
    for i in range(1, len(nums)): #iterate through the array starting from the second element
        nums[i-1] = nums[i] #shift each element to the left by one position
    nums[-1] = first #place the first element at the end of the array
nums = [1, 2, 3, 4, 5] #input array
leftRotateByOne(nums) #call the function to left rotate the array by one
print(nums) #print the modified array
'''tc O(n) where n is the length of the input array, as we need to iterate through the array once.
sc O(1) as we are using only a constant amount of extra space to store the variable.'''