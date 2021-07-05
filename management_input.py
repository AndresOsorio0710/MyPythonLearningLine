capture = input('Write something: ')
print(capture)

capture = input('Weite a number integer: ')
print(type(capture),capture)
results = int(capture)
capture = input('Weite another  number integer: ')
print(type(capture),capture)
results = results + int(capture)
print(type(results),results)

capture = input('Weite a number float: ')
print(type(capture),capture)
results = float(capture)
capture = input('Weite another  number float: ')
print(type(capture),capture)
results = results + float(capture)
print(type(results),results)

