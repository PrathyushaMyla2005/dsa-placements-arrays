'''Two Sum : Check if a pair with given sum exists in Array
Problem Statement: Given an array of integers arr[] and an integer target.
1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}'''
# Given array → This is the list of numbers
arr = [2, 6, 5, 8, 11]
# Target sum → We need to find two numbers whose sum = 14
target = 14
# Length of array → Total number of elements in array
n = len(arr)
# Flag variable → used to check whether pair is found or not
# Initially False → means pair not found yet
found = False
# Outer loop → selects first element one by one
# i represents index of first element
for i in range(n):
    # Inner loop → selects second element
    # starts from i+1 because:
    # 1. Avoid checking same element
    # 2. Avoid repeating same pair
    for j in range(i+1, n):
        # Check condition:
        # If sum of first element and second element = target
        if arr[i] + arr[j] == target:
            # If condition true → pair found
            print("YES")
            # Change flag to True → indicates pair exists
            found = True
            # Stop inner loop
            break
    # This checks flag after inner loop
    # If pair already found
    if found:
        # Stop outer loop also
        break
# After loop completes, check flag
# If still False → means no pair found
if not found:
  # Print NO
    print("NO")
'''tc: O(n^2) because we have two nested loops iterating through the array.
sc: O(1) because we are using only a constant amount of extra space to store the result.'''
# function definition for 2nd variant
def twoSum(arr, target):
    n = len(arr) # Length of array
    # Loop through each element of array
    for i in  range(n): # Outer loop selects first element
        for j in range(i+1, n): # Inner loop selects second element
            if arr[i] + arr[j] == target: # Check if sum equals target
                return [i, j] # Return indices of the two numbers
    return [-1, -1] # If no pair found, return [-1, -1]
# main program starts here
arr = [2, 6, 5, 8, 11] # Given array
target = 14 # Target sum
result = twoSum(arr, target) # Call function and store result
print("Indices of the two numbers:", result) # Print the result
'''tc: O(n^2) because we have two nested loops iterating through the array.
sc: O(1) because we are using only a constant amount of extra space to store the result.'''
def two_sum_indices(arr, target):

    # Create empty dictionary
    # This will store: number → index
    seen = {}

    # Loop through array using index
    for i in range(len(arr)):

        # Get current number from array
        num = arr[i]
        # Example first time: num = 2

        # Find which number is needed to make target
        need = target - num
        # Example: target=14, num=2
        # need = 14-2 = 12

        # Check if needed number already exists in dictionary
        if need in seen:

            # If exists → we found answer
            # seen[need] gives index of needed number
            # i is current index

            return [seen[need], i]


        # If not exists → store current number and index
        seen[num] = i

        # Example:
        # seen = {2:0}
        # means number 2 is at index 0


# Create array
arr = [2,6,5,8,11]

# Call function and print result
print(two_sum_indices(arr,14))  
'''tc: O(n) because we are iterating through the array once.
sc: O(n) because in worst case we may store all elements of array in the dictionary.'''
