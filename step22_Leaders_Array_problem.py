'''leaders in an array are those elements which are greater than all the elements to their right side. The rightmost element is always a leader. For example, in the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.
Input:
The first line of input contains an integer T denoting the number of test cases. Then T
example ;[16, 17, 4, 3, 5, 2]
lines follow, each line contains an integer N denoting the size of the array and then N space separated integers denoting the elements of the array.
Output:
[17, 5, 2]'''
def find_leaders(arr):
    leaders = []

    for i in range(len(arr)):
        right = arr[i + 1:]

        if len(right) == 0 or arr[i] > max(right):
            leaders.append(arr[i])

    return leaders

arr = [16, 17, 4, 3, 5, 2]
print(find_leaders(arr))