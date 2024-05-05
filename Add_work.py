first_number = int(input('Введите число в первом поле:'))
password = ''
for i in range(1, first_number):
    for j in range(i + 1, first_number):
        if first_number % (i +j) == 0:
            password = password + str(i) +str(j)
print('Пароль для числа', first_number, '-', password)