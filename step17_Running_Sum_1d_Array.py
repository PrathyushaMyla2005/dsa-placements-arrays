'''example
Input: nums = [1,2,3,4]
Output: [1,3,6,10]'''
def sum(arr):
    result =[]#create an empty list to store the result
    sum = 0 #Initialize the sum to 0
    for i in range(len(arr)):#Iterate through the input array
        sum += arr[i] #Add the current element to the sum
        result.append(sum) #Append the current sum to the result list
    return result #Return the result list
#Example usage
arr = [1,2,3,4]
print(sum(arr))
'''tc O(n) where n is the length of the input array, as we need to iterate through the array once to calculate the running sum.
sc O(n) where n is the length of the input array, as we need to store'''