import random

# Генерируем случайный массив от 3 до 10 элементов
n = random.randint(3, 10)
numbers = [random.randint(1, 100) for _ in range(n)]

print(f"Исходный массив ({n} элементов): {numbers}")

def make_max_number(arr):
    """Составляет максимальное число из элементов массива"""
    # Преобразуем числа в строки
    str_numbers = [str(x) for x in arr]
    
    # Сортируем строки по специальному правилу:
    # числа должны идти в порядке, дающем максимальную конкатенацию
    for i in range(len(str_numbers)):
        for j in range(i + 1, len(str_numbers)):
            # Сравниваем два варианта: a+b и b+a
            if str_numbers[i] + str_numbers[j] < str_numbers[j] + str_numbers[i]:
                # Меняем местами
                str_numbers[i], str_numbers[j] = str_numbers[j], str_numbers[i]
    
    # Склеиваем все строки
    return ''.join(str_numbers)

# Получаем результат
result = make_max_number(numbers)
print(f"Максимальное число: {result}")

# Для наглядности покажем как число (если оно не слишком большое)
try:
    print(f"Как число: {int(result)}")
except:
    print("(слишком большое для отображения в виде числа)")


#level3
import random

n = random.randint(3, 10)
numbers = [random.randint(1, 100) for _ in range(n)]

print(f"Массив ({n} элементов): {numbers}")

def max_number(arr):
    str_numbers = [str(x) for x in arr]

    for i in range(len(str_numbers)):
        for j in range(i + 1, len(str_numbers)):
            if str_numbers[i] + str_numbers[j] < str_numbers[j] + str_numbers[i]:
                str_numbers[i], str_numbers[j] = str_numbers[j], str_numbers[i]
    
    return ''.join(str_numbers)

result = max_number(numbers)
print(result)