'''consecutive ones Given a binary array, find the maximum number of consecutive 1s in this array.  
Example 1:
Input: arr = [1, 1, 0, 1, 1, 1]
Output: 3 (the maximum number of consecutive 1s in the array)
'''
def max_ones(arr):
    count = 0
    max_count = 0
    for num in range(len(arr)):
        if arr[num] == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0


arr = [ 1,1,3,4]
print(max_ones(arr))
'''tc O(n) sc O(1)'''
