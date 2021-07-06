# Coleccion desordenada, se usasn para definir una coleccion qu eno tiene indise
set_colors = {'red', 'gray', 'green', 'yelow',
              'blue', 'pink', 'purple', 'black'}

print(dir(set_colors))
print(type(set_colors))
print('red' in set_colors)
set_colors.add('violet')
print(set_colors)
set_colors.remove('green')
print(set_colors)
set_colors.add('green')
print(set_colors)

set_colors.clear()
print(set_colors)
del set_colors
print(set_colors)
