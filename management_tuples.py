# Nos permite definir un conjunto de datos igual que las listas pero estos no los podemos cambiar
# Son ma srapidas que las listas
tuple_colors = ('yellow', 'green', 'blue', 'red')
tuple_mixed = (1, 'Hello world', 3.1416, False, 'My name is Andres Osorio')
tuple_mounths = ('January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December')
tuple_numbers = tuple((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))

no_is_tuple=(1)
print(type(no_is_tuple))
is_tuple=(1,)
print(type(is_tuple))

print(dir(tuple_numbers))
print(type(tuple_numbers))
print(tuple_numbers[0])
for n in tuple_numbers:
    print(n)


# eliminar tupla
del tuple_numbers
print(tuple_numbers)
