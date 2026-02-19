'''Linear Search in 
Problem Statement: Given an array, and an element num the task is to find if num is present in the given array 
or not. If present print the index of the element or print -'''
'''brute force approach: we can iterate through the array and check if the element is present or not.'''
# Linear Search Brute Force

arr = [10, 20, 30, 40, 50] # given array
num = 40# element to be searched

# assume element not found
index = -1

# check each element
for i in range(0, len(arr)):# iterate through the array
    
    if arr[i] == num:# check if the current element is equal to the target element
        index = i# update index if element is found
        break 

# print result
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")
    '''Time Complexity: O(n) where n is the number of elements in the array. In the worst case, we may have to check all elements of the array.
    Space Complexity: O(1) as we are using only a constant amount of extra space to store the index.
    '''
#optimized approach: we can use a hash set to store the elements of the array and then check if the target element is present in the set or not. This will reduce the time complexity to O(1) for searching the element after O(n) time to create the set.
# Linear Search Optimized
# Linear Search Program in Python

# function to perform linear search
def linear_search(arr, num):
    
    # traverse each element in array
    for i in range(len(arr)):
        
        # check if element is equal to num
        if arr[i] == num:
            return i   # return index if found
    
    return -1   # return -1 if not found


# main program
arr = [10, 20, 30, 40, 50]
num = 30

result = linear_search(arr, num)

# print result
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
'''Time Complexity: O(n) where n is the number of elements in the array. In the worst case, we may have to check all elements of the array.
Space Complexity: O(1) as we are using only a constant amount of extra space to store the index.'''