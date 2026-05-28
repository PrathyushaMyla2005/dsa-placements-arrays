from itertools import permutations

class Solution:
    # Function to find the next permutation
    def nextPermutation(self, nums):
        # Generate all unique permutations
        perms = sorted(set(permutations(nums)))

        # Convert list to tuple for comparison
        current = tuple(nums)

        # Traverse the list
        for i in range(len(perms)):
            if perms[i] == current:
                # If last permutation, return first
                if i == len(perms) - 1:
                    return list(perms[0])
                # Else return next
                return list(perms[i + 1])

        return nums

# Driver code
sol = Solution()
nums = [1, 2, 3]
result = sol.nextPermutation(nums)
print(" ".join(map(str, result)))
