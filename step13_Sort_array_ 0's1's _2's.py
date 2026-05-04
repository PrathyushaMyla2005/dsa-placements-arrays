'''find the number that appear 0's 1's and 2's in the array and sort the array
example 1:
input arr = [0,1,2,0,1,2]
output [0,0,1,1,2,2] (the sorted array)'''
def sort_array(arr):
    n = len(arr)
    count = 0 # count of 0's
    count1 = 0 # count of 1's
    count2 = 0 # count of 2's
    for i in range(n):
        if arr[i] == 0:
            count += 1
        elif arr[i] == 1:
            count1 += 1
        else:
            count2 += 1
# fill the array with 0's 1's and 2's based on the count
    i = 0
    for _ in range(count):# fill the first count elements with 0's
        arr[i] = 0
        i += 1
    for _ in range(count1):# fill the next count1 elements with 1's
        arr[i] = 1# fill the next count1 elements with 1's
        i += 1# fill the next count1 elements with 1's
    for _ in range(count2):# fill the next count2 elements with 2's
        arr[i] = 2
        i += 1
    return arr
arr = [0,1,2,0,1,2]
print(sort_array(arr))
'''tc O(n) sc O(1) because we are using constant space to store the count of 0's 1's and 2's'''