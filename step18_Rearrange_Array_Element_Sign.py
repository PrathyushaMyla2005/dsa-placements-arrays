'''Rearrange Array Elements by Sign
Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. 
Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.'''
def rearrange_array(arr): # function definition
    pos = [] # initialize an empty list to store positive elements
    neg = [] # initialize an empty list to store negative elements
    for i in arr: # iterate through the array
        if i >= 0: # if the current number is positive
            pos.append(i) # add it to the pos list
        else: # if the current number is negative
            neg.append(i) # add it to the neg list
    for i in range(len(pos)): # iterate through the pos list
        arr[2*i] = pos[i] # place the positive elements at even indices
        arr[2*i + 1] = neg[i] # place the negative elements at odd indices
    return arr # return the rearranged array
arr = [3, -2, 1, -5, 4, -6] # given input array
print("Rearranged array:", rearrange_array(arr)) # call function and print the rearranged array
'''Time Complexity: O(n) where n is the number of elements in the array as we
    are iterating through the array twice, once to separate positive and negative elements and once to rearrange them.  
Space Complexity: O(n) as we are using two additional lists to store the positive and negative elements.'''
'''trace   the example in the code
arr = [3, -2, 1, -5, 4, -6]
pos = [3, 1, 4], neg = [-2, -5, -6]
i = 0, arr[0] = 3, arr[1] = -2
i = 1, arr[2] = 1, arr[3] = - 5
i = 2, arr[4] = 4, arr[5] = -6
The rearranged array is [3, -2, 1, -5, 4, -6], which has positive and negative elements alternately while maintaining their relative order.
'''
def rearrange_array(arr): # function definition
    pos_index = 0 # initialize index for positive elements
    neg_index = 1 # initialize index for negative elements
    for i in arr: # iterate through the array
        if i >= 0: # if the current number is positive
            arr[pos_index] = i # place it at the current positive index
            pos_index += 2 # move to the next even index
        else: # if the current number is negative
            arr[neg_index] = i # place it at the current negative index
            neg_index += 2 # move to the next odd index
    return arr # return the rearranged array
arr = [3, -2, 1, -5, 4, -6] # given input array
print("Rearranged array:", rearrange_array(arr)) # call function and print the rearranged array
'''Time Complexity: O(n) where n is the number of elements in the array as we
    are iterating through the array once to rearrange the elements.
Space Complexity: O(1) as we are rearranging the elements in place without using any
    additional space.'''
'''trace   the example in the code line by line 
a
arr = [3, -2, 1, -5, 4, -6] # given input array
arr = [0, 0, 0, 0, 0, 0] # after initializing the array with zeros
pos_index = 0, neg_index = 1
current number = 3, arr[0] = 3, pos_index = 2
current number = -2, arr[1] = -2, neg_index = 3
current number = 1, arr[2] = 1, pos_index = 4
current number = -5, arr[3] = -5, neg_index = 5
current number = 4, arr[4] = 4, pos_index = 6
current number = -6, arr[5] = -6, neg_index = 7
The rearranged array is [3, -2, 1, -5, 4, -6], which has positive and negative elements alternately while maintaining their relative order.
'''

