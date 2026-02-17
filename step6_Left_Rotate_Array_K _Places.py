'''Rotate array by K elements 
Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right'''
class Solution:
    # Rotate the array to the right by k positions
    def rotateRight(self, arr, k):
        n = len(arr)
        if n == 0:
            return

        k %= n

        # Store last k elements
        temp = arr[-k:]

        # Shift the remaining elements
        for i in range(n - k - 1, -1, -1):
            arr[i + k] = arr[i]

        # Copy stored elements to the front
        for i in range(k):
            arr[i] = temp[i]

    # Rotate the array to the left by k positions
    def rotateLeft(self, arr, k):
        n = len(arr)
        if n == 0:
            return

        k %= n

        # Store first k elements
        temp = arr[:k]

        # Shift remaining elements
        for i in range(k, n):
            arr[i - k] = arr[i]

        # Copy stored elements to the end
        for i in range(k):
            arr[n - k + i] = temp[i]


# Driver code
sol = Solution()

arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
sol.rotateRight(arr, k)
print("Array after right rotation:", arr)

arr2 = [1, 2, 3, 4, 5, 6, 7]
sol.rotateLeft(arr2, k)
print("Array after left rotation:", arr2)
'''Time Complexity: O(n) for both left and right rotations as we are iterating through the array a few times
Space Complexity: O(k) for both left and right rotations as we are using a temporary array to store k elements'''
