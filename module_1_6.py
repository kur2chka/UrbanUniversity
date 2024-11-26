my_dict = {'Max':88005553535, 'Anton':89005056765, 'Zhenek':89456655778}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Max'))
print('Not existing value:', my_dict.get('Zahar'))
my_dict.update({'Amelie':89567657890,
                'Genadiy':89562345432})
print('Deleted value:', my_dict.pop('Anton'))
print('Modified dictionary:', my_dict)
my_set = {1, 1, 2, 2, 3, 3, 'Git', 'Git'}
print('Set:', my_set)
my_set.discard(1)
print('Modified set:', my_set)
