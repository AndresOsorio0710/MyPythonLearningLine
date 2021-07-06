# Comparadores
# Lógicos
x = 3
y = 5
z = 2
print('x > y', x > y)
print('x < y', x < y)
print('x == z', x == z)

i = 2.25
j = 5.001
k = 3.992

print(f'{y} >= {j} {y>=j}')
print(f'{y} <= {j} {y<=j}')

print('x > y', x > y)
print('x < y', x < y)
print('x == z', x == z)

print('(x+z) == y', (x+z) == y)
print('(x*i+z) < j', (x*i+z) < j)

print(f'({x} > {y}) | ({i} < {j})', ((x > y) | (i < j)))
print(f'({x} > {y}) or ({i} < {j})', ((x > y) or (i < j)))
print(f'({x} > {y}) & ({i} < {j})', ((x > y) & (i < j)))
print(f'({k} > {x}) and ({k} < {y})', ((k > x) and (k < y)))


a='hi'
b='hello'
c='by'
d='hello'

print(f'{a} == {b}',a==b)
print(f'{c} == {b}',c==b)
print(f'{d} == {b}',d==b)
print(f'{d} == {c}',d==c)

a='a'
b='b'
c='c'
d='d'

print(f'{a} < {b}',a<b)
print(f'{b} < {c}',b<c)
print(f'{c} < {d}',c<d)
print(f'{d} < {a}',d<a)
print(f'{c} < {b}',c<b)
print(f'{b} < {a}',b<a)

a='ad'
b='bc'
c='c'
d='d'

print(f'{a} < {b}',a<b)
print(f'{b} < {c}',b<c)
print(f'{c} < {d}',c<d)
print(f'{d} < {a}',d<a)
print(f'{c} < {b}',c<b)
print(f'{b} < {a}',b<a)


print('Enter 3 numbers, I will find the highest number')
n1 = input('n1: ')
n2 = input('n2: ')
n3 = input('n3: ')


if n1 > n2:
    if n1 > n3:
        print(f'{n1} is the largest number')
elif n2 > n3:
    print(f'{n2} is the largest number')
else:
    print(f'{n3} is the largest number')

if (n1 > n2) & (n1 > n3):
    print(f'{n1} is the largest number')
elif n2 > n3:
    print(f'{n2} is the largest number')
else:
    print(f'{n3} is the largest number')

# 2:36:32
