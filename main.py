#Задание 1
while True:
    try:
        num1 = float(input("Введите первое чило:"))
        num2 = float(input("Введите второе чило:"))
        break
    except ValueError:
        print("Ошибка: Введите числа корректно!")


sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2


if num2!=0:
    Del_result = num1/num2
else:
    Del_result = "Деление на ноль невозможно"

#Вывод результатов
print("Сумма:", sum_result)
print("Разность:" ,diff_result)
print("Произведение:", prod_result)
print("Частное:", Del_result)