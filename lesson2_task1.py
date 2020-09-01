my_list = ['abc', 132, 25.03, False]
i = 0

type(my_list)

for el in my_list:
    print('Element', i, '=', el, 'Type: ', type(el))
    i += 1