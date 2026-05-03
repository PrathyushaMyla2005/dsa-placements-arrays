'''union of two sorted arrays
Given two sorted arrays, find their union. The union of two arrays is the set of distinct elements present in either of the two arrays.
Example 1:
Input: arr1 = [1, 2, 4], arr2 = [2, 3, 4]
Output: [1, 2, 3, 4] (the union of the two arrays)'''
def union_sorted_array(arr1,arr2):
    st = set(arr1) | set(arr2)# Create a set from both arrays and take the union of the sets to get distinct elements   
    return sorted(st) # Convert the set back to a sorted list 
# Test the function
arr1 = [1, 2, 4]
arr2 = [2, 3, 4]
print(union_sorted_array(arr1, arr2))
