print("Программа проверки пароля приветствует вас")
print("Программа проверит ваш пароль по трем условиям:")
print("1. Длина не менее 8 символов")
print("2. Есть хотя бы одна цифра")
print("3. Есть хоть одна заглавная буква")
print("Для выхода введите 'quit'\n")

while True:
    password = input("Введите ваш пароль: ")

    if password.lower() == "quit":
        print("Выход. До встречи.")
        break

    if password.strip() == "":
        print("Пароль пустой. Введите что-нибудь.\n")
        continue

    length = len(password) >= 8
    digit = False
    upper = False

    for char in password:
        if char.isdigit():
            digit = True
        if char.isupper():
            upper = True

    if length and digit and upper:
        print("Пароль надежный!!!")
        break
    else:
        print("Пароль не подходит по условиям. Проблемы:")
        if not length:
            print(" - Длина меньше 8 символов")
        if not digit:
            print(" - Нет ни одной цифры")
        if not upper:
            print(" - Нет ни одной заглавной буквы")
        print()
