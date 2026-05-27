'''find the number of subarrays with sum k
Example:
Input: arr = [1, 2, 3], k = 3
Output: 2 (subarrays are [1, 2] and [3])
'''
def count_subarrays_with_sum_k(arr, k):
    count = 0 #initialize count of subarrays with sum k
    current_sum = 0 #initialize current sum of the subarray
    for i in range(len(arr)):#Iterate through the input array
        for j in range(i,len(arr)):#Iterate through the input array starting from the current index
            current_Sum += arr[j]#add the current element to the current sum
            if current_sum == k :#if the current sum is equal to k, increment the count
                count += 1
    return count #return the count of subarrays with sum k
# Example usage
arr = [1, 2, 3]
k = 3
print(count_subarrays_with_sum_k(arr, k)) # Output: 2
'''tc: O(n^2) where n is the length of the input array
sc: O(1) for the count and current sum variables'''
'''optimized solution using prefix sum'''
def count_subarrays_with_sum_k(arr, k):
    count = 0 #initialize count of subarrays with sum k
    hash_map = {0: 1} #initialize a hash map to store the frequency of prefix sums
    current_sum = 0 #initialize current sum of the subarray
    for i in range(len(arr)):#Iterate through the input array
        current_sum += arr[i]#add the current element to the current sum
        if current_sum - k in hash_map:#if the difference between the current sum and k is in the hash map, increment the count by the frequency of that prefix sum
            count += hash_map[current_sum - k]
        if current_sum in hash_map:#if the current sum is already in the hash map, increment its frequency
            hash_map[current_sum] += 1
        else:#if the current sum is not in the hash map, add it with a frequency of 1
            hash_map[current_sum] = 1
    return count #return the count of subarrays with sum k
# Example usage
arr = [1, 2, 3]
k = 3
print(count_subarrays_with_sum_k(arr, k)) # Output: 2
'''tc: O(n) where n is the length of the input array
sc: O(n) for the hash map storing prefix sums'''