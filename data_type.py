# Formas de declarar un String
from typing import Tuple


single_quotes = 'Single Quotes'
double_quotes = "Double Quotes"
single_quotes_3 = '''Single Quotes * 3'''
double_quotes_3 = """Double Quotes * 3"""
print(single_quotes)
print(double_quotes)
print(single_quotes_3)
print(double_quotes_3)

# Visualizar el tipo de datop de una variable
print(single_quotes, ' -> ', type(single_quotes))
print(double_quotes, ' -> ', type(double_quotes))
print(single_quotes_3, ' -> ', type(single_quotes_3))
print(double_quotes_3, ' -> ', type(double_quotes_3))

# Concatenar String
concatenate_string = single_quotes+' + '+double_quotes + \
    ' + '+single_quotes_3+' + '+double_quotes_3
print(type(concatenate_string), ' -> ', concatenate_string)

# Declarar tipos númericos
# Imteger
number_int = 30
# Float
number_float = 30.6
print(type(number_int), ' -> ', number_int)
print(type(number_float), ' -> ', number_float)

# Declaracion de tipo Boolean
boolean_type = number_int > number_float
print(type(boolean_type), ' -> ', number_int,
      ' > ', number_float, ' = ', boolean_type)
boolean_type = number_int < number_float
print(type(boolean_type), ' -> ', number_int,
      ' < ', number_float, ' = ', boolean_type)

# List
list_type_int = [10, 20, 30, 40, 50, 60, 70, 80, 90,
                 100, 200, 300, 400, 500, 600, 700, 800, 900]
list_type_float = [10.43, 20.24, 30.454, 40.55, 50.454, 60.12, 70.1354, 80.74, 90.45,
                   100.145, 200.654, 300.457, 400.45, 500.45, 600.78, 700.45, 800.85, 900.456]
list_type_string = [single_quotes, double_quotes,
                    single_quotes_3, double_quotes_3]
list_type_bool = [True, False, False, True, True, True, True, False]
list_mixed = [double_quotes, True, 85, double_quotes_3, 5.878]
print(type(list_type_int), ' -> ', list_type_int)
print(type(list_type_float), ' -> ', list_type_float)
print(type(list_type_string), ' -> ', list_type_string)
print(type(list_type_bool), ' -> ', list_type_bool)
print(type(list_mixed), ' -> ', list_mixed)

# Tuples, por lo genetral las usamos en datos que no cambian
tuple_type_int = (10, 20, 30, 40, 50, 60, 70, 80, 90,
                  100, 200, 300, 400, 500, 600, 700, 800, 900)
tuple_type_float = (10.43, 20.24, 30.454, 40.55, 50.454, 60.12, 70.1354, 80.74, 90.45,
                    100.145, 200.654, 300.457, 400.45, 500.45, 600.78, 700.45, 800.85, 900.456)
tuple_type_string = (single_quotes, double_quotes,
                     single_quotes_3, double_quotes_3)
tuple_type_bool = (True, False, False, True, True, True, True, False)
tuple_mixed = (double_quotes, True, 85, double_quotes_3, 5.878)
print(type(tuple_type_int), ' -> ', tuple_type_int)
print(type(tuple_type_float), ' -> ', tuple_type_float)
print(type(tuple_type_string), ' -> ', tuple_type_string)
print(type(tuple_type_bool), ' -> ', tuple_type_bool)
print(type(tuple_mixed), ' -> ', tuple_mixed)

# Dictionaries, te permiten agrupar datos que pertenecen a una misma entidad
dictionarie_person = {'name': 'Andres Javier',
                      'lastname': 'Osorio Peralta', 'nickname': 'AJ', 'age': 25}

print(type(dictionarie_person), ' -> ', dictionarie_person)
print(type(dictionarie_person.name), ' -> ', dictionarie_person.name)
