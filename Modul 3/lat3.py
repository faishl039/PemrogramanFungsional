def add(left, right):
    return left + right

def min(left, right):
    return left - right

def mult(left, right):
    return left * right

def div(left, right):
    return left / right

def tree(node):
    if isinstance(node, tuple):
        left, operator, right = node
        if operator == '+':
            return add(tree(left), tree(right))
        elif operator == '-':
            return min(tree(left), tree(right))
        elif operator == '*':
            return mult(tree(left), tree(right))
        elif operator == '/':
            return div(tree(left), tree(right))
    else:
        return node

def filter_map_data(data):
    data_float = [value for value in data if isinstance(value, (float, int))]
    data_int = [value for value in data if isinstance(value, int)]
    data_string = [value for value in data if isinstance(value, str)]

    def map_int(value):
        if isinstance(value, int):
            hundreds = value // 100
            tens = (value % 100) // 10
            ones = value % 10
            return {'ratusan': hundreds, 'puluhan': tens, 'satuan': ones}
        return value

    data_int = list(map(map_int, data_int))

    return data_float, data_int, data_string

expression_tree = ((2, '+', 3), '*', (5, '-', 1))
result = tree(expression_tree)
print("hasil tree: ", result)

data = [result, 'helo', 'world']
data_float, data_int, data_string = filter_map_data(data)

print("Data Float:")
print(data_float)
print("Data Int:")
for item in data_int:
    if isinstance(item, dict):
        print(item)
    else:
        print(item)
print("Data String:")
print(data_string)
