'''Find the largest element in an array
Given an array of integers, find the largest element in the array.
Example 1:
Input: [1, 2, 3, 4, 5]
Output: 5'''
def largest_element(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
# Test the function
arr = [1, 2, 3, 4, 5]
print(largest_element(arr))
'''tc: O(n) where n is the number of elements in the array
sc: O(1) as we are using only a constant amount of space to store the
'''
#optimized solution
def largest_element(arr):
    return max(arr)
# Test the function
arr = [1, 2, 3, 4, 5]
print(largest_element(arr))
'''tc: O(n) where n is the number of elements in the array
sc: O(1) as we are using only a constant amount of space to store the
'''
#smallest element in an array
def smallest_element(arr):
    min = arr[0] #initialize min to the first element of the array
    for i in range(1,len(arr)):#Iterate through the input array starting from the second element
        if arr[i] < min:#if the current element is smaller than min, update min
            min = arr[i]
    return min #return the smallest element in the array
# Test the function
arr = [1, 2, 3, 4, 5]

print(smallest_element(arr))
'''tc: O(n) where n is the number of elements in the array
sc: O(1) as we are using only a constant amount of space to store the
'''