'''Find Second Smallest and Second Largest Element in an array
Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.'''
# Function to find the second smallest and second largest elements in the array
def getElements(arr, n):
    # Edge case: when the array has less than 2 elements
    if n == 0 or n == 1:
        print(-1, -1)  # Print -1 for both second smallest and second largest
        return

    # Sort the array to easily find the second smallest and second largest elements
    arr.sort()

    # Second smallest element is at index 1 after sorting
    small = arr[1]

    # Second largest element is at index n-2 after sorting
    large = arr[n - 2]

    # Output the second smallest and second largest elements
    print("Second smallest is", small)
    print("Second largest is", large)

# Main function to handle input and output
if __name__ == "__main__":
    # Initialize the array with elements
    arr = [1, 2, 4, 6, 7, 5]
    
    # Calculate the size of the array
    n = len(arr)
    
    # Call the function to find and print the second smallest and second largest elements
    getElements(arr, n)
'''tc: O(n log n) due to sorting the array
sc: O(1) as we are using only a constant amount of extra space for variables
'''
def getElements(arr, n):# Function to find the second smallest and second largest elements in the array n is the size of the array
    if n < 2:# Edge case: when the array has less than 2 elements
        return -1, -1  # Return -1 for both if there are less than 2 elements
    small = float('inf')  # Initialize smallest to positive infinity
    second_small = float('inf')  # Initialize second smallest to positive infinity
    for i in range(n):  # Iterate through the array to find the smallest and second smallest elements   
        if arr[i] < small:  # If the current element is smaller than the smallest
            second_small = small  # Update second smallest to the previous smallest
            small = arr[i]  # Update smallest to the current element
        elif small < arr[i] < second_small:  # If the current element is between smallest and second smallest
            second_small = arr[i]  # Update second smallest to the current element
    return small,second_small  # Return the second smallest and smallest elements
# Main function to handle input and output
arr = [1, 2, 4, 6, 7, 5]  # Initialize the array with elements
n = len(arr)  # Calculate the size of the array
second_small, small = getElements(arr, n)  # Call the function to find the
print("Second smallest is", second_small)  # Print the second smallest element
print("Smallest is", small)  # Print the smallest element (which is the second
'''tc: O(n) as we are iterating through the array once
sc: O(1) as we are using only a constant amount of extra space for variables
'''
def getElements(arr, n):# Function to find the second smallest and second largest elements in the array n is the size of the array
    if n < 2:
        return -1, -1  # Return -1 for both if there are less than 2 elements
    large = float('-inf')  # Initialize largest to negative infinity
    second_large = float('-inf')  # Initialize second largest to negative infinity
    for i in range(n): # Iterate through the array to find the largest and second largest elements   
        if arr[i] > large:  # If the current element is larger than the largest
            second_large = large  # Update second largest to the previous largest
            large = arr[i]  # Update largest to the current element
        elif second_large < arr[i] < large:  # If the current element is between second largest and largest
            second_large = arr[i]  # Update second largest to the current element
    return second_large, large  # Return the second largest and largest elements
# Main function to handle input and output
arr = [1, 2, 4, 6, 7, 5]  # Initialize the array with elements
n = len(arr)  # Calculate the size of the array
second_large, large = getElements(arr, n)  # Call the function to find the second largest and largest elements
print("Second largest is", second_large)  # Print the second largest element
print("Largest is", large)  # Print the largest element
'''tc: O(n) as we are iterating through the array once
sc: O(1) as we are using only a constant amount of extra space for variables
'''