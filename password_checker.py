def check_password(password):
    problems = []

    if password.strip() == "":
        problems.append("Пароль пустой. Введите что-нибудь.")
        return problems

    if len(password) < 8:
        problems.append("Длина меньше 8 символов")

    if not any(char.isdigit() for char in password):
        problems.append("Нет ни одной цифры")

    if not any(char.isupper() for char in password):
        problems.append("Нет ни одной заглавной буквы")

    return problems


def main():
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

        problems = check_password(password)

        if problems:
            print("Пароль не подходит по условиям. Проблемы:")
            for problem in problems:
                print(f" - {problem}")
            print()
        else:
            print("Пароль надежный!!!")
            break


if __name__ == "__main__":
    main()
