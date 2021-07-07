list_range = list(range(10, 100))
tuple_mounths = ('January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December')
dictionary_mounths = {'January': (1, 31), 'February': (2, 28), 'March': (3, 31), 'April': (4, 31), 'May': (5, 30), 'June': (6, 31),
                      'July': (7, 30), 'August': (8, 31), 'September': (9, 30), 'October': (10, 31), 'November': (11, 30), 'December': (12, 31)}
set_colors = {'red', 'gray', 'green', 'yelow',
              'blue', 'pink', 'purple', 'black'}

for n in list_range:
    if (n % 2) == 0:
        print(f'{n} is even')

for month in tuple_mounths:
    if month == 'March':
        continue
    if month == 'September':
        break
    print(month)

for n in range(1, 9):
    print(n)

for s in 'abcdefghijk':
    print(s)

count = 0

while count <= 10:
    print(count)
    count = count+1
r = 'S'

while r == 'S':
    r = input('Write s to continue, another character to end:__ ')
    r = r.upper()
    print(r)
