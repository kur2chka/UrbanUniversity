def calculate_structure_sum(*data_structure):
    total = 0
    for arg in data_structure:
        if isinstance(arg, (int, float)):
            total += arg
        elif isinstance(arg, str):
            total += len(arg)
        elif isinstance(arg, dict):
            total += calculate_structure_sum(*arg.keys(), *arg.values())
        elif isinstance(arg, (list, tuple, set)):
            total += calculate_structure_sum(*arg)
    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)