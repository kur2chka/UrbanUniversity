def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1)
print_params(2)
print_params(1, 2, 3)
print_params(1, 2)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [3074, 'legit', False]
values_dict = {'a':3074, 'b':'legit', 'c':False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [7500, True]
print_params(*values_list_2, 42)