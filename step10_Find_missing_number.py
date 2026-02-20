'''Problem Statement
You are given an array of size n-1 containing numbers from 1 to n.
One number is missing. Find that missing number.'''
#brute force approach
def find_missing_number(arr):#function to find the missing number in the array
    n = len(arr)#calculate the size of the array
    for i in range(1, n+2):#iterate through the numbers from 1 to n
        if i not in arr:#if the number is not in the array
            return i#return the missing number
'''tc: O(n^2) because we are iterating through the array for each number from 1 to n.
sc: O(1) because we are not using any extra space.'''
#optimal approach
def find_missing_number(arr):#function to find the missing number in the array
    n = len(arr)#calculate the size of the array
    total_sum = (n+1)*(n+2)//2#calculate the sum of numbers from 1 to n using the formula n(n+1)/2
    arr_sum = sum(arr)#calculate the sum of the elements in the array
    return total_sum - arr_sum#return the difference between the total sum and the array sum which will be the missing number
'''tc: O(n) because we are iterating through the array once to calculate the sum.
sc: O(1) because we are not using any extra space.'''
#example
arr = [1, 2, 4, 5]#array of size n
print(find_missing_number(arr))#3 is the missing number
