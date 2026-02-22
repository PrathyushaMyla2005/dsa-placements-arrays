'''Rotate array by K elements 
Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right'''
def rotate_array(arr,k): #function to rotate the array by k elements to the left
    n = len(arr) #get the length of the array
    #right rotation can be achieved by left rotating the array by n-k elements
    if n == 0: #if the array is empty, return the empty array
        return arr
    k = k % n #if k is greater than n, we need to take the modulus to get the effective rotation
    temp = arr[-k:]  #get the last k elements of the array
    for i in range(n-k-1, -1, -1): #iterate through the array from the end to the beginning
        arr[i+k] = arr[i] #shift the elements to the right by k positions
    for i in range(k): #iterate through the first k elements
        arr[i] = temp[i] #place the last k elements at the beginning of the array
    return arr #return the rotated array
#example
arr = [1, 2, 3, 4, 5] #input
k = 2 #number of positions to rotate
print(rotate_array(arr, k)) #output: [4, 5, 1, 2, 3]
#left rotation example
def rotate_array_left(arr,k): #function to rotate the array by k elements to the left
   n = len(arr) #get the length of the array
   if n == 0: #if the array is empty, return the empty array
       return arr
   k = k % n #if k is greater than n, we need to take the modulus to get the effective rotation
   temp = arr[:k] #get the first k elements of the array
   for i in range(k, n): #iterate through the array from the k-th element to the end
         arr[i-k] = arr[i] #shift the elements to the left by k positions
   for i in range(n-k, n): #iterate through the last k elements
        arr[i] = temp[i-n+k] #place the first k elements at the end of the array
   return arr #return the rotated array
#example
arr = [1, 2, 3, 4, 5] #input
k = 2 #number of positions to rotate
print(rotate_array_left(arr, k)) #output: [3, 4, 5, 1, 2]
'''tc: O(n) where n is the size of the array. We are iterating
through the array a few times, but the overall time complexity is linear.
sc: O(k) because we are using a temporary array to store the k elements that are
being rotated. The space complexity is linear with respect to k.'''
#optimal approach using reversal algorithm
def rotate_array(arr,k,start,end): #function to reverse a portion of the array from start to end
    while start < end: #while the start index is less than the end index
        arr[start], arr[end] = arr[end], arr[start] #swap the elements at start and end indices
        start += 1 #move the start index to the right
        end -= 1 #move the end index to the left
def rotate_array_optimal(self,arr,k,direction): #function to rotate the array by k elements to the left using reversal algorithm
    n = len(arr) #get the length of the array
    if n == 0: #if the array is empty, return the empty array
        return arr
    k = k % n #if k is greater than n, we need to take the modulus to get the effective rotation
    if direction == 'left': #if the direction is left, we need to reverse the first k elements, then reverse the remaining n-k elements, and finally reverse the entire array
       self.reverse(arr, 0, k-1) #reverse the first k element #if the direction is right, we need to reverse the last k elements, then reverse the remaining n-k elements, and finally reverse the entire array
       self.reverse(arr, n-k, n-1) #reverse the last k elements
       self.reverse(arr, 0, n-1) #reverse the entire array
    elif direction == 'right': #if the direction is right, we need to reverse the last k elements, then reverse the remaining n-k elements, and finally reverse the entire array
         self.reverse(arr, n-k, n-1) #reverse the last k elements
         self.reverse(arr, 0, n-k-1) #reverse the remaining n-k elements
         self.reverse(arr, 0, n-1) #reverse the entire array
    return arr #return the rotated array
#example
arr = [1, 2, 3, 4, 5] #input
k = 2 #number of positions to rotate
print(rotate_array_optimal(arr, k, 'left')) #output: [3, 4, 5, 1, 2]
print(rotate_array_optimal(arr, k, 'right')) #output: [4, 5, 1, 2, 3]
'''tc: O(n) where n is the size of the array. We are iterating
through the array a few times, but the overall time complexity is linear.
sc: O(1) because we are not using any extra space to store the elements. We are performing the rotation in place.'''