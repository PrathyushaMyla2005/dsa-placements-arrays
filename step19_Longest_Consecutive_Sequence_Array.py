'''Longest Consecutive Sequence in an Array
Problem Statement: Given an array nums of n integers.
Return the length of the longest sequence of consecutive integers
The integers in this sequence can appear in any order.
Example 1:
Input:
 nums = [100, 4, 200, 1, 3, 2]  
Output:
 4  
Explanation:
 The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4. This sequence can be formed regardless of the initial order of the elements in the array.'''
class Solution:
    def longestConsecutive(self, nums):
        n = len(nums)
        # If the array is empty
        if n == 0:
            return 0 

        # Initialize the longest sequence length
        longest = 1 
        st = set()

        # Put all the array elements into the set
        for i in range(n):
            st.add(nums[i])

        # Traverse the set to find the longest sequence
        for it in st:
            # Check if 'it' is a starting number of a sequence
            if it - 1 not in st:
                # Initialize the count of the current sequence
                cnt = 1 
                # Starting element of the sequence
                x = it 

                # Find consecutive numbers in the set
                while x + 1 in st:
                    # Move to the next element in the sequence
                    x = x + 1 
                    # Increment the count of the sequence
                    cnt = cnt + 1 
                # Update the longest sequence length
                longest = max(longest, cnt)
        return longest

if __name__ == "__main__":
    a = [100, 4, 200, 1, 3, 2] 
    # Create an instance of the solution class
    solution = Solution() 
    # Function call to find the longest consecutive sequence
    ans = solution.longestConsecutive(a) 
    print("The longest consecutive sequence is", ans)
