#level 1
l = [1, 5, 1, -1, "hellow", "Y", 7, 2, "y", 7, "hellow"]

d = []
seen = set()

for i in l:
    if i in seen and i not in d:
        d.append(i)
    seen.add(i)

print(f"Исходный список: {l}")
print(f"Повторяющиеся элементы: {d}")


#level 2
import random
N = int(input("Введите размер матрицы: "))
m = []

for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randint(0, 100))
    m.append(row)

for i in range(N):
    for j in range(N):
        print(f"{m[i][j]:4}", end="")
    print()

max_el = m[0][0]
max_i, max_j = 0, 0

for i in range(N):
    for j in range(N):
        if m[i][j] > max_el:
            max_el = m[i][j]
            max_i, max_j = i, j

print(f"Максимальный элемент: {max_el}")


#level 3
d = {"name1": "id1", "name2": "id2", "name3": "id3"}
d1 = {}

for key, value in d.items():
    d1[value] = key

print("Исходный словарь:", d)
print("Новый словарь:", d1)