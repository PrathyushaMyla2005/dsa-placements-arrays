'''Remove Duplicates in-place from Sorted Array
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once.
 The relative order of the elements should be kept the same.
'''
def removeDuplicates(nums):#function to remove duplicates from a sorted array
    if not nums:#if the input array is empty, return 0
        return 0#initialize a set to store the unique elements
    seen = set()#to store the unique elements
    index = 0#to keep track of the index of the unique elements
    for num in nums:#iterate through the input array
        if num not in seen: #if the current number is not in the seen set, it is a unique element
           seen.add(num) #add the unique element to the seen set
           nums[index] = num #update the input array with the unique element at the current index
           index += 1 #increment the index for the next unique element
    return index #return the number of unique elements in the array
nums = [1, 1, 2, 3, 3]
k = removeDuplicates(nums)
print("k:", k)#print the number of unique elements in the array
print("Unique array:", nums[:k]) #print the unique elements in the array up to index k
'''tc: O(n) where n is the length of the input array, as we need to iterate through the array once.
sc: O(n) in the worst case when all elements are unique, as we need to'''
#optimal 
def removeDuplicates(nums): #function to remove duplicates from a sorted array
    if not nums:#if the input array is empty, return 0
        return 0 #initialize a pointer to keep track of the index of the unique elements
    i = 0 #to keep track of the index of the unique elements
    for j in range(1,len(nums)):#iterate through the input array starting from the second element
        if nums[j] != nums[i]: #if the current number is different from the last unique element, it is a unique element
            i += 1 #increment the index for the next unique element
            nums[i] = nums[j] #update the input array with the unique element at the current index
    return i + 1 #return the number of unique elements in the array
nums = [1, 1, 2, 3, 3]
k = removeDuplicates(nums)
print("k:", k) #print the number of unique elements in the array
print("Unique array:", nums[:k]) #print the unique elements in the array up to index k
'''tc O(n) where n is the length of the input array, as we need to iterate through the array once.  
sc O(1) as we are using only a constant amount of extra space to store the pointers.'''