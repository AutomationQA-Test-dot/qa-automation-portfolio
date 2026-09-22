print("Программа проверки пароля приветствует вас")
print("Программа проверит ваш пароль по трем условиям:")
print("1. Длина не менее 8 символов")
print("2. Есть хотя бы одна цифра")
print("3. Есть хоть одна заглавная буква")
print("Приступим")
print("Введите ваш пароль:")
password = input()

lenght = False
digit = False
upper = False

if len(password) >= 8:
    lenght = True

for char in password:
    if char.isdigit():
        digit = True

for char in password:
    if char.isupper():
        upper = True            

if lenght and digit and upper:
    print("Пароль надежный!!!")
else:
    print("Пароль не подходит по условиям. Проблемы:")
    if not lenght:
        print(" - Длина меньше 8 символов")
    if not digit:
        print(" - Нет ни одной цифры")
    if not upper:
        print(" - Нет ни одной заглавной буквы")