
# Перевірте, чи є число парним чи ні.
# Ваша функція повинна повертати True,
# якщо число парне, і False, якщо число непарне.

def get_even(number):
    if number % 2 == 0:
        return True
    return False

# def get_even(number):
#     if not number % 2:
#         return True
#     return False
#
# print(get_even(7))
# print(get_even(146))

# Ця функція повинна приймати рядок як вхідні дані
# та повертати кількість
# голосних (a, e, i, o, u) у рядку. Функція має
# бути нечутливою до регістру.

def counter_symbol(s):
    temp = "aeiou"
    s = s.lower()
    count_lit = 0
    for lit in temp:
        count_lit += s.count(lit)
    return count_lit


s = "Clear weather in Odessa will be observed throughout the day. No precipitation."

# print(counter_symbol(s))

# Ця функція повинна приймати на вхід ціле число невід('ємне і '
#  'повертати факторіал цього числа.)
# Факторіал невід('ємного цілого числа n - це добуток '
# всіх позитивних цілих чисел, менших або рівних n.)

def get_factorial(number):
    factorial = 1
    if number == 0:
        print('Error')
    while number > 0:
        factorial *= number
        number -= 1
    return factorial

print(get_factorial(6))