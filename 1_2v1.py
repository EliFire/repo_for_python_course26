#level 1
a = int(input())
b = int(input())
c = int(input())

if a == b and c == b:
    print("3")
elif a == b or c == b or a == c:
    print('2')
else:
    print('0')

#level 2
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if not (1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8):
    print("Число должно быть от 1 до 8.")
else:
    if x1 == x2 or y1 == y2:
        print('YES')
    else:
        print('NO')

#level 3
while True:
    password = str(input())
    if len(password) > 8 and any(c.islower() for c in password) and any(c.isupper() for c in password):
        break
    print("Не соответствует требованиям!")