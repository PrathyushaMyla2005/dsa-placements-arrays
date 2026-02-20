'''Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays
The union of two arrays can be defined as the common and distinct elements in the two arrays.
NOTE: Elements in the union should be in ascending order.'''
#brute force approach
def union(arr1, arr2):#function to find the union of two sorted arrays
    result = []#initialize an empty list to store the result
    for i in arr1:#iterate through the first array
        if i not in result:#if the element is not already in the result list
            result.append(i)#append the element to the result list
    for j in arr2:#iterate through the second array
        if j not in result:#if the element is not already in the result list
            result.append(j)#append the element to the result list
    return sorted(result)#return the sorted result list
'''tc: O((n+m)log(n+m)) where n and m are the sizes of the two arrays. This is because we are sorting the result list which can have at most n+m elements.
sc: O(n+m) because in the worst case, all elements from both arrays are distinct
and will be stored in the result list.'''
#example
arr1 = [1, 2, 4, 5, 6]#first sorted array
arr2 = [2, 3, 5, 7]#second sorted array
print(union(arr1, arr2))#[1, 2, 3, 4, 5, 6, 7]

#optimal approach