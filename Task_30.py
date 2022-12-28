import math


def my_pi(d):
    # Алгоритм Брента-Саламина
    a = 1
    b = 1/math.sqrt(2)
    t = 1/4
    p = 1
    pi = 0
    while True:
        pi1 = math.pow(a+b, 2)/(4*t)
        a1 = (a+b)/2
        b1 = math.sqrt(a*b)
        t1 = t-p*math.pow(a-a1, 2)
        p1 = 2*p
        a, b, t, p = a1, b1, t1, p1
        if abs(pi-pi1) < d:
            break
        pi = pi1
    return pi


def Input_value(msg1, msg2):
    while True:
        try:
            user_number_str = input(msg1)
            if user_number_str == '0.'+'0'*(len(user_number_str)-3)+'1':
                user_number = float(user_number_str)
            else:
                raise ValueError
            break
        except ValueError:
            print(msg2)
    return (user_number, user_number_str)


def print_num(msg, num, d):
    print(msg)
    print(f'Округленное {round(num, d)}')
    num = str(num)[:str(num).find('.')+d+1]
    print(f'Обрезанное {num}')


user_number = Input_value(
    'Введите точность вычисления, число вида 0.0..01:  ', 'Введите число вида 0.0..01')
calc_pi = my_pi(user_number[0])
print_num('Вычисленное пи по алгоритму Брента-Саламина',
          calc_pi, len(user_number[1][2:]))
print_num('Пи из библиотеки math', math.pi, len(user_number[1][2:]))
