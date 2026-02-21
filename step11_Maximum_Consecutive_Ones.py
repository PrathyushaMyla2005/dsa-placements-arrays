'''Count Maximum Consecutive One's in the array
Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array..'''
def max_consecutive_ones(arr):#function to count maximum consecutive ones in the array
    max_count = 0 #initialize max_count to 0
    count = 0 #initialize count to 0
    for i in arr: #iterate through the array
        if i == 1: #if the element is 1
            count += 1 #increment the count
        else: #if the element is 0
            count = 0 #reset the count to 0
        max_count = max(max_count, count) #update the max_count if the current count is greater
    return max_count #return the max_count
'''tc: O(n) where n is the size of the array. We are iterating
through the array once.
sc: O(1) because we are using only a constant amount of extra space to store the count and max_count.'''
#example
arr = [1, 1, 0, 1, 1, 1] #input array
print(max_consecutive_ones(arr)) #output: 3
