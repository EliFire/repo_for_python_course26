# level 1
x = float(input("x = "))
p = float(input("p = "))
y = float(input("y = "))
ye = 0

if p > 0 and p <=1:
    while y >= x:
        ye += 1
        x = int(x + p*x)

    x = str(x)
    ye = str(ye)
    print("x = " + x)
    print("ye = " + ye)

else:
    print("Ошибка! Введите p от 0 до 1!")


#level 2
n = int(input("n = "))
i = 1

while i <= n:
    print("for - частный случай цикла while")
    i += 1


#level 3
n = str(int(input("n = ")))
if n[0] == '-':
    num = num[1:]

sum = 0
for i in range(len(n)):
    sum += int(n[i])

print(n)
print(f"Сумма цифр: {sum}")