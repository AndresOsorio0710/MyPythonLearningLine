#
dictionary_mounths = {'January': (1, 31), 'February': (2, 28), 'March': (3, 31), 'April': (4, 31), 'May': (5, 30), 'June': (6, 31),
                      'July': (7, 30), 'August': (8, 31), 'September': (9, 30), 'October': (10, 31), 'November': (11, 30), 'December': (12, 31)}

dictionary_product = {
    'name': 'i robot',
    'quantity': 25,
    'price': 2000
}

dictionary_person = {
    'name': 'Andres',
    'last_name': 'Osorio',
    'age': 25,
    'syze': 180
}

print(dir(dictionary_mounths))
print(type(dictionary_mounths))
print(dictionary_product.keys())
print(dictionary_product.items())

list_books = [
    {
        'name': 'i robot',
        'quantity': 25,
        'price': 2000
    },
    {
        'name': 'i dorian',
        'quantity': 33,
        'price': 3000
    },
    {
        'name': 'routers',
        'quantity': 65,
        'price': 1200
    },
    {
        'name': 'sara',
        'quantity': 25,
        'price': 2000
    }
]


for i in list_books:
    print(i)


dictionary_product.clear()
print(dictionary_product)
del dictionary_product
print(dictionary_product)