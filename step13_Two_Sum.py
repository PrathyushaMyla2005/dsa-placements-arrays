'''Two Sum : Check if a pair with given sum exists in Array
Problem Statement: Given an array of integers arr[] and an integer target.
1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}'''
# Given array
arr = [2, 6, 5, 8, 11]

# Target sum we want to find
target = 14

# Find length of array (number of elements)
n = len(arr)

# Outer loop → selects first element
for i in range(n):

    # Inner loop → selects second element
    # starts from i+1 to avoid checking same element again
    for j in range(i+1, n):

        # Check if sum of two elements equals target
        if arr[i] + arr[j] == target:

            # If yes → print YES
            print("YES")

            # Stop inner loop
            break

# This else belongs to outer for loop
# It runs if loop completes normally (no break from outer loop)
else:

    # If no pair found → print NO
    print("NO")
'''tc: O(n^2) because we have two nested loops iterating through the array.
sc: O(1) because we are using only a constant amount of extra space to store the result.'''