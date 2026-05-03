'''find the number that appear once  return that number
example 1:
input arr = [1,2,3,4,1,2,3]
output 4 (the number that appears once in the array)'''
def  find_Single(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in freq:
        if freq == 1:
            return num 
arr = [3,3,1,2,2,7]
print((find_Single(arr)))
'''tc O(n) sc O(n)'''