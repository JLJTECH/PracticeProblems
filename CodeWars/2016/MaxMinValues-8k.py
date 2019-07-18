#Create two functions and return the largest and lowest number in that array/vector.
def min(arr):
    return sorted(arr)[0]

def max(arr):
    return sorted(arr)[-1]


#Alternate Solution
def min(arr):
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low

def max(arr):
    high = arr[0]
    for i in arr[1:]:
        if i > high:
            high = i
    return high