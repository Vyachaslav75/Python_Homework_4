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
        user_list.append(random.randint(0, 15))
    return user_list


def check_list(user_list):
    result = []
    wrong = []
    for i in range(len(user_list)):
        if user_list[i] not in wrong:
            if user_list[i] in user_list[i+1:]:
                wrong.append(user_list[i])
            else:
                result.append(user_list[i])
    return result


#print(check_list(gen_list(input_value('Введите длину списка: ', 'Введите целое число'))))
num = input_value('Введите длину списка: ', 'Введите целое число')
us_lst = gen_list(num)
print(f'Сгенерированный список: {us_lst}')
print(f'Список не повторяющихся элементов: {check_list(us_lst)}')
