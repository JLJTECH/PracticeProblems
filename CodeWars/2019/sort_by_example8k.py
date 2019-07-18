#Given an Array and an Example-Array to sort to, write a function that sorts the Array following the Example-Array.

def example_sort(arr, example_arr):
    
    #Sort array by key index
    return sorted(arr, key=example_arr.index)
