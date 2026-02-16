'''Check if an Array is Sorted
Problem Statement: Given an array of size n, write a program to check 
if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not.
 If the array is sorted then return True, Else return False.'''
#brute force approach
class solution: #class to check if an array is sorted
    def isSorted(self,n):#function to check if an array is sorted
        for i in range(n):#iterate through the array starting from the second element
           for j in range(i+1,n):#iterate through the array starting from the element after the current element
               if arr[i] > arr[j]: #if the current element is greater than the next element, the array is not sorted
                   return False #return False if the array is not sorted
        return True
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5] #input array
    n = len(arr) #length of the input array
    obj = solution() #create an object of the solution class
    result = obj.isSorted(n) #call the isSorted function to check if the array is sorted
    print(result) #print the result
'''tc O(n^2) where n is the length of the input array, as we need to iterate through the array twice.
sc  O(1) as we are using only a constant amount of extra space to store the variables.'''
#optimal approach
def isSorted(arr): #function to check if an array is sorted
    n = len(arr)
    if n==0 or n==1:
        return False
    for i in range(1,n): #iterate through the array starting from the second element    
        if arr[i] < arr[i-1]: #if the current element is less than the previous element, the array is not sorted
            return False #return False if the array is not sorted
    return True #return True if the array is sorted
arr = [1,2,3,4]
k = isSorted(arr) #call the isSorted function to check if the array is sorted
print(k) #print the result
'''tc O(n) where n is the length of the input array, as we need to iterate through the array once.
sc O(1) as we are using only a constant amount of extra space to store the variables.'''