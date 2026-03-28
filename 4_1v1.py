import random

array = [random.randrange(-100, 100) for _ in range(20)]
array.sort()

print(array)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

try:
    target = int(input())
    
    result = binary_search(array, target)
    
    if result != -1:
        print(target)
    else:
        print("Число не найдено.")
        
except ValueError:
    print("Ошибка, введите целое число.")