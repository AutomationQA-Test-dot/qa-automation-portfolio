print("Приветствуем вас в игре 'FizzBuzz'")
print("Введите число от 1 до 100:")
num = int(input())
print("Вы ввели:", num)
if 1 <= num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz!!!")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
else:
    print("Не корректное число")