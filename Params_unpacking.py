def print_params(a=1, b='string', c=False):
    print(a, b, c)

print_params()
print_params(25)
print_params(True, 11)
print_params(1, 2, 3)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [3-2j, {5, 6, 8}, (123, 'Test')]
values_dict = {'a':('Top', 1, True), 'b':{15, 12, False}, 'c':'string'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [True, 'Text']
print_params(*values_list_2, 125)