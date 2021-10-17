# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число
# «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции! К каждому элементу списка добавить 17 и заново
# вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

# create and fill odd_cube list
odd_cube = list()
count = 0

# while from 1 to 1000 number for odd_cube
while count < 1000:
    if count % 2 != 0:  # check for odd count
        odd_cube.append(count ** 3)  # adding cube entry to odd_cube
    count += 1
print('Список, состоящий из кубов нечётных чисел: ', odd_cube)


# while, calculating the sum of the values div by 7
def calc_val_list(list_name):
    count = 0
    while count < len(list_name):
        result = list_name[count]
        div_count, math_result = 1, 0
        # nested while, calculating the sum value
        while result != 0:
            div_count = result % 10
            result = result // 10
            math_result += div_count
        # if, overwrite the list value conditionally
        if math_result % 7 == 0:
            list_name[count] = math_result
        count += 1
    print('Вывод списка со значениями, где сумма цифр кратная 7: ', list_name)


# View a list with values where the sum div 7
calc_val_list(odd_cube)

# Arephmetic sum of each value in a odd_cube list and number 17
count = 0
while count < len(odd_cube):
    odd_cube[count] += 17
    count += 1
print('Арифметическое сложение каждого значения списка odd_cube и 17: ', odd_cube)

# View a list with values where the sum div 7
calc_val_list(odd_cube)
