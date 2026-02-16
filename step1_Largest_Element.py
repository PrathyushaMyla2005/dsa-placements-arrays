'''Find the Largest element in an array
Problem Statement: Given an array, we have to find the largest element in the array.'''
def largestElement(arr): #function to find the largest element in an array
    if not arr: #if the input array is empty, return None
        return None
    arr.sort() #sort the input array in ascending order
    return arr[-1] #return the last element of the sorted array, which is the largest element
arr = [1, 2, 3, 4, 5] #input array
k = largestElement(arr) #call the function to find the largest element in the array
print(k) #print the largest element in the array
'''tc O(n log n) where n is the length of the input array, as we need to sort the array.    
sc O(1) as we are using only a constant amount of extra space to store the variable.'''
#optimal approach
def largestelement(arr,n): #function to find the largest element in an arra
    max = arr[0] #initialize the maximum element with the first element of the arra
    for i in range(1,n): #iterate through the array starting from the second element
        if arr[i] > max: #if current element is greater than the max,update max
            max = arr[i] #update the maximum element with the current element
    return max
arr = [1, 2, 3, 4, 5] #input array
n = len(arr) #length of the input array
k = largestelement(arr,n) #call the function to find the largest element in the array
print(k) #print the largest element in the array
'''tc O(n) where n is the length of the input array, as we need to iterate through the array once.
    sc O(1) as we are using only a constant amount of extra space to store the variable.'''
