import random

array = [random.randrange(-100, 100) for _ in range(20)]
print(array)

def insertion_sort(arr):
    sorted_arr = arr.copy()
    
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        
        sorted_arr[j + 1] = key
    
    return sorted_arr

sorted_result = insertion_sort(array)
print(sorted_result)