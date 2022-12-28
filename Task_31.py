def Input_value(msg1, msg2):
    while True:
        try:
            user_number = int(input(msg1))
            break
        except ValueError:
            print(msg2)
    return user_number


def erat(n):
    n = n+1
    a = [0]*n
    for i in range(n):
        if i % 2 != 0:
            a[i] = i

    a[1] = 0
    a[2] = 2
    m = 2
    while m < n:
        if a[m] != 0:
            j = m*2
            while j < n:
                a[j] = 0
                j = j+m
        m += 1
    result = []
    for i in a:
        if a[i] != 0:
            result.append(a[i])
    del a
    return result


def decomp(user_number):
    simple_numbers = erat(user_number)
    result = []
    while True:
        if user_number in simple_numbers:
            result.append(user_number)
            return result
        else:
            for i in simple_numbers:
                if user_number % i == 0:
                    result.append(i)
                    user_number = user_number//i
                    break


user_number = Input_value('Введите целое цисло:  ', 'Введите целое цисло')
print(f'Список простых множителей числа {user_number} -> {decomp(user_number)}')
