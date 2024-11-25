immutable_var = 'netlimiter', 3074, True
print(immutable_var)
#immutable_var[0] = 'legit'
#команда выше выдаст ошибку, ибо кортеж относится к неизменяемым типам данных
mutable_list = ['netlimiter', 3074, True]
mutable_list[0] = 'legit'
mutable_list[1] = 7500
mutable_list[2] = False
print(mutable_list)


