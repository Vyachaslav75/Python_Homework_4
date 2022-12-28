import random


def input_value(msg1, msg2):
    while True:
        try:
            user_number = int(input(msg1))
            break
        except ValueError:
            print(msg2)
    return user_number


def gen_list(list_lens):
    user_list = []
    for i in range(list_lens):
        user_list.append(random.randint(0, 101))
    return user_list


def polinom(koef_lst):
    result = ''
    for i in range(len(koef_lst)-1):
        if koef_lst[i] != 0:
            if i > 0 and koef_lst[i] > 0:
                result = result+f'+{koef_lst[i]}*x**{len(koef_lst)-i-1}'
            else:
                result = result+f'{koef_lst[i]}*x**{len(koef_lst)-i-1}'
    if koef_lst[-1] > 0:
        result = result[:-3]+f'+{koef_lst[-1] }=0'
    else:
        result = result[:-3]+f'{koef_lst[-1] }=0'
    return result


def write_file(user_list):
    with open('Polinom.txt', 'w', encoding='utf-8') as f:
        if len(user_list):
            f.write(user_list)


num = input_value('Введите максимальную степень многочлена: ', 'Введите целое число')
us_str=polinom(gen_list(num+1))
print('Сгенерированный многочлен: ')
print(us_str)
write_file(us_str)
