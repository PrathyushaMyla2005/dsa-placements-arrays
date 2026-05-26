'''prefix_sum is a technique used to calculate the sum of a subarray in constant time after an initial preprocessing step.
Example:
Input: arr = [1, 2, 3, 4, 5]
Output: prefix_sum = [1, 3, 6, 10, 15]'''
def prefix_sum(arr):
    n = len(arr) #get the length of the input array
    prefix_sum = [0] * n #create a prefix sum array of the same length as the input array
    prefix_sum [0] = arr[0] #the first element of the prefix sum array is the same as the first element of the input array
    for i in range(1,n):#iterate through the input array starting from the second element
        prefix_sum[i] = prefix_sum[i-1] + arr[i]#the current element of the prefix sum array is the sum of the previous element of the prefix sum array and the current element of the input array
    return prefix_sum #return the prefix sum array
# Example usage
arr = [1, 2, 3, 4, 5]
print(prefix_sum(arr)) # Output: [1, 3, 6, 10, 15]
'''tc: O(n) where n is the length of the input array
sc: O(n) for the prefix sum array'''