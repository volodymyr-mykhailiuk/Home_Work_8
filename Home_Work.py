# 1) С помощью циклов вывести на экран все простые числа от 1 до 100. Простое число — число, которое делится нацело только на единицу или само на себя. Первые простые
# числа это — 2,3,5,7…

checker = False

for i in range(2, 101):
    for j in range(2, i):
        if not i % j:
            break
    else:
        print(i)


# 2) Выведите на экран «песочные часы», максимальная ширина которых считывается с клавиатуры(число нечетное).
print()

width = int(input("Width = "))

i = width
j = 0

while i > 0:
    print(j * " ", i * "*", j * " ")
    i -= 2
    j += 1

i += 2
j -= 1

while i < width:
    i += 2
    j -= 1
    print(j * " ", i * "*", j * " ")

# 3) Написать код для зеркального переворота списка [7,2,9,4] -> [4,9,2,7]. Список может быть произвольной длины. (При выполнении задания использовать дополнительный список нельзя).
print()

x = [7, 2, 9, 4]

print(x)

x = x[::-1]

print(x)
