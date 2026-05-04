'''majority element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the majority element always exists in the array.
example 1:
input arr = [3,2,3]
output 3 (the majority element in the array)'''
def majority_element(arr):
    freq = {} # create a dictionary to store the frequency of each number
    n = len(arr)
    for num in arr:
        if num in freq:
            freq[num] += 1 # if the number is already in the dictionary, increment its frequency
        else:
            freq[num] = 1 # if the number is not in the dictionary, add it with frequency 1
    for num in freq:
        if freq[num] > n//2: # check if the frequency of the number is greater than n/2
            return num # if it is, return the number
arr = [3,2,3]
print(majority_element(arr))
'''tc O(n)  because we traverse the array once to count the frequency of each number and sc O(n) because we use a dictionary to store the frequency of each number'''
