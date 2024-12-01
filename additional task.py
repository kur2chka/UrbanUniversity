first = int(input('Введите первое число: '))
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []

if first <= 2 or first >= 21:
    print('Вы ввели неверное число')
else:
    for i in range(3, first + 1):
        if first % i != 0:
            continue
        else:
            for k in range(1, 20):
                for j in range(1, 20):
                    if k + j == i:
                        if j - k < 0 or j == k:
                            continue
                        else:
                            if k == 1:
                                one.append(k)
                                one.append(j)
                            if k == 2:
                                two.append(k)
                                two.append(j)
                            if k == 3:
                                three.append(k)
                                three.append(j)
                            if k == 4:
                                four.append(k)
                                four.append(j)
                            if k == 5:
                                five.append(k)
                                five.append(j)
                            if k == 6:
                                six.append(k)
                                six.append(j)
                            if k == 7:
                                seven.append(k)
                                seven.append(j)
                            if k == 8:
                                eight.append(k)
                                eight.append(j)
                            if k == 9:
                                nine.append(k)
                                nine.append(j)

list_ = [one, two, three, four, five, six, seven, eight, nine]
result = [*list_[0], *list_[1], *list_[2], *list_[3], *list_[4], *list_[5], *list_[6], *list_[7], *list_[8]]
print(first, '-', *result)