list_colors = ['yellow', 'green', 'blue', 'red']
list_mixed = [1, 'Hello world', 3.1416, False,
              'My name is Andres Osorio', list_colors]

# Asignar valores a una lñista
# Si se le van a asignar datos agrupados debe hacerse de esta manera, de lo contrario nos marcara un error
list_numbers = list((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
print(type(list_numbers), list_numbers)

# range(), me crea un alista a partir de un rango
list_range = list(range(0, 10))
print(type(list_range), list_range)
list_range = list(range(0, 35))
print(type(list_range), list_range)

print(type(list_colors), list_colors)
print('Metods -> ', dir(list_colors))
print('len -> ', len(list_mixed))
print('len -> ', len(list_colors))
print('len -> ', len(list_numbers))
print('len -> ', len(list_range))
print('[n] -> ', list_range[15])
print('[n] -> ', list_colors[3])
print('[n] -> ', list_range[-15])
print('[n] -> ', list_colors[-3])
print('in -> ', 25 in list_numbers)
print('in -> ', 25 in list_range)
print('in -> ', 'red' in list_colors)
print('in -> ', False in list_mixed)
print('in -> ', list_colors in list_mixed)
list_numbers.append(10)
print('append ->', list_numbers)
list_mixed.extend([10, 4.2485, 'Carlos', True])
print('extend ->', list_mixed)
list_range.insert(15, 25)
print('insert ->', list_range)
print('pop ->', list_numbers)
list_numbers.pop()
print('pop ->', list_numbers)
list_numbers.pop()
print('pop ->', list_numbers)
list_numbers.pop(3)
print('pop(n) ->', list_numbers)
list_numbers.pop(3)
print('pop(n) ->', list_numbers)
list_numbers.pop(3)
print('pop(n) ->', list_numbers)
list_numbers.remove(8)
print('remove(8) ->', list_numbers)
list_numbers.clear()
print('clear ->', list_numbers)

list_colors.sort()
print('sort ->', list_colors)
list_colors.sort(reverse=True)
print('sort(reverse=True) ->', list_colors)
list_range.sort()
print('sort ->', list_range)
list_range.sort(reverse=True)
print('sort(reverse=True) ->', list_range)

print('index ->', list_colors.index('green'))
print('count ->', list_range.count(25))

print(list_colors)
list_colors[3] = 'pink'
print(list_colors)
