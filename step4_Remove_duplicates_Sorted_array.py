'''find the unique elements in a sorted array
Given a sorted array of integers, find the unique elements in the array.
Example 1: [1, 1, 2, 2, 3, 4, 4]
Output: [1, 2, 3, 4]'''
def unique_elements(arr): # Initialize an empty list to store the unique elements
    set = [] # Iterate through the array
    for i in range(len(arr)): #if the current element is not in the set, add it to the set
        if arr[i] not in set :
            set.append(arr[i]) # Return the list of unique elements
    return set
# Test the function
arr = [1, 1, 2, 2, 3, 4, 4]
print(unique_elements(arr))
'''tc: O(n) where n is the number of elements in the array
sc: O(n) as we are using a list to store the unique elements, which can grow up to the size of the input array in the worst case
'''