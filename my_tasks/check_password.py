import re


def ask_password(login, password, success=False, failure=False):
    login = login.lower()
    password = password.lower()
    report = ''
    if len(re.sub(f'[bcdfghjklmnpqrstvwxz]', '', password)) != 3:
        report = 'Wrong number of vowels'
    if re.sub(f'[aeiouy]', '', login) != re.sub(f'[aeiouy]', '', password):
        report = 'Everything is wrong' if report else 'Wrong consonants'
    if report:
        if failure:
            failure(login, report)
        return login, report
    else:
        if success:
            success(login)
        return login, report


def main(login, password):
    report = ask_password(login, password)
    if not report[1]:
        print(f'Привет, {report[0]}!')
    else:
        print(
            f'Кто-то пытался притвориться пользователем {report[0]}, но в пароле допустил ошибку: {report[1].upper()}.')


main(input(), input())
