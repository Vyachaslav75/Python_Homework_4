import random


def gen_list(list_lens):
    user_list = []
    for i in range(list_lens):
        user_list.append(random.randint(-20, 100))
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


def write_file(user_list, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        if len(user_list):
            f.write(user_list)


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        result = f.readline()
    return result


def parse_polinom(us_str):
    result = {}
    temp_str = ('', '', '1')
    while len(temp_str[2]) > 0:
        temp_str = us_str.partition('x**')
        if len(temp_str[2]) > 0:
            if len(temp_str[0][:-1]) > 0:
                result[int(temp_str[2][:1])] = int(temp_str[0][:-1])
            else:
                result[int(temp_str[2][:1])] = 1
            us_str = temp_str[2][1:]
        else:
            temp_str = us_str.partition('x')
            if len(temp_str[2]) > 0:
                if len(temp_str[0][:-1]) > 0:
                    result[1] = int(temp_str[0][:-1])
                else:
                    result[1] = int(temp_str[0][:-1])
                us_str = temp_str[2]
            else:
                temp_str = us_str.partition('=0')
                result[0] = int(temp_str[0])
    return result


def sum_polinom(dict1, dict2):
    n = max(max(dict1.keys()), max(dict2.keys()))
    result = [0]*(n+1)
    for i in (dict1, dict2):
        for j in range(len(result)):
            try:
                result[j] += i[j]
            except:
                pass
    return result


polinom1 = polinom(gen_list(random.randint(1, 10)))
polinom2 = polinom(gen_list(random.randint(1, 10)))

write_file(polinom1, 'Polinom1.txt')
write_file(polinom2, 'Polinom2.txt')
print('Первый многочлен: ')
print(read_file('Polinom1.txt'))
print('Второй многочлен: ')
print(read_file('Polinom2.txt'))
dict1 = parse_polinom(read_file('Polinom1.txt'))
dict2 = parse_polinom(read_file('Polinom2.txt'))
new_lst = sum_polinom(dict1, dict2)
new_lst.reverse()
print('Сумма первого и второго : ')
print(polinom(new_lst))
