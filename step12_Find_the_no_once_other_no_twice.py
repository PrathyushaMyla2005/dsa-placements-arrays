'''Find the number that appears once, and the other numbers twice
Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single on'''
def single_number(arr):#function to find the single number in the array
    n = len(arr) #get the length of the array
    for i in range(n): #iterate through the array
        count = 0 #initialize count to 0
        for j in range(n): #iterate through the array again
            if arr[i] == arr[j]: #if the elements are the same
                count += 1 #increment the count
        if count == 1: #if the count is 1, we found the single number
            return arr[i] #return the single number
#example
arr = [4, 1, 2, 1, 2] #input
print(single_number(arr)) #output: 4
'''tc: O(n^2) where n is the size of the array. We are using two nested loops to count the occurrences of each element.
sc: O(1) because we are using only a constant amount of extra space to store the count variable.'''
#optimal approach
def single_number_optimal(arr):#function to find the single number in the array using XOR
    XOR = 0 #initialize XOR to 0
    for i in arr: #iterate through the array
        XOR ^= i #XOR the current element with the XOR variable
    return XOR #return the result of XOR which will be the single number
#example
arr = [4, 1, 2, 1, 2] #input
print(single_number_optimal(arr)) #output: 4
'''tc: O(n) where n is the size of the array. We are iterating through the array once.
sc: O(1) because we are using only a constant amount of extra space to store the XOR variable.'''
#example trace
'''arr = [4, 1, 2, 1, 2] #input
XOR = 0 #initialize XOR to 0
XOR ^= 4 #XOR becomes 4
XOR ^= 1 #XOR becomes 5
XOR ^= 2 #XOR becomes 7
XOR ^= 1 #XOR becomes 6
XOR ^= 2 #XOR becomes 4
return XOR #return 4 which is the single number'''