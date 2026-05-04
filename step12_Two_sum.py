''' Two Sum 
example 1:
input arr = [2,7,11,15] target = 9
output [0,1] (the indices of the two numbers that add up to the target)'''
def two_sum(arr,target):
    freq = {} # create a dictionary to store the frequency of each number
    for i in range(len(arr)):
        complement = target - arr[i]# calculate the complement of the current number    
        if complement in freq: # check if the complement exists in the dictionary
            return [freq[complement],i] # if it exists, return the indices of the complement and the current number
        freq[arr[i]] = i # if it doesn't exist, add the current number and its index to the dictionary
arr = [2,7,11,15]
target = 9
print(two_sum(arr,target))
'''tc o(n) why we traverse the array once and sc o(n) because we use a dictionary to store the frequency of each number'''