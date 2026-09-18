print("Приветствуем вас в программе 'Калькулятор'")
print("Введите первое число:")
first_num = int(input())
print("Введите второе число:")
second_num = int(input())
print("Выберите одну из предложенных операций: +, -, *, /")
operation = input()

if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "/":
    print(first_num / second_num)
else:
    print("Недопустимая операция")
