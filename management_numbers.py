number_int_1 = 4
number_int_2 = 3
number_float_1 = 0.5
number_float_2 = 4.2412
print('Sum---------------------------------------------------------------------')
results = number_float_1+number_float_2
print(type(results), f'{number_float_1} + {number_float_2} = ', results)
results = number_float_1+number_int_2
print(type(results), f'{number_float_1} + {number_int_2} = ', results)
results = number_int_1+number_float_2
print(type(results), f'{number_int_1} + {number_float_2} = ', results)
results = number_int_1+number_int_2
print(type(results), f'{number_int_1} + {number_int_2} = ', results)
print('Subtraction-------------------------------------------------------------')
results = number_float_1-number_float_2
print(type(results), f'{number_float_1} - {number_float_2} = ', results)
results = number_float_1-number_int_2
print(type(results), f'{number_float_1} - {number_int_2} = ', results)
results = number_int_1-number_float_2
print(type(results), f'{number_int_1} - {number_float_2} = ', results)
results = number_int_1-number_int_2
print(type(results), f'{number_int_1} - {number_int_2} = ', results)
print('Multiplication----------------------------------------------------------')
results = number_float_1*number_float_2
print(type(results), f'{number_float_1} * {number_float_2} = ', results)
results = number_float_1*number_int_2
print(type(results), f'{number_float_1} * {number_int_2} = ', results)
results = number_int_1*number_float_2
print(type(results), f'{number_int_1} * {number_float_2} = ', results)
results = number_int_1*number_int_2
print(type(results), f'{number_int_1} * {number_int_2} = ', results)
print('Division----------------------------------------------------------------')
results = number_float_1/number_float_2
print(type(results), f'{number_float_1} / {number_float_2} = ', results)
results = number_float_1/number_int_2
print(type(results), f'{number_float_1} / {number_int_2} = ', results)
results = number_int_1/number_float_2
print(type(results), f'{number_int_1} /{number_float_2} = ', results)
results = number_int_1/number_int_2
print(type(results), f'{number_int_1} / {number_int_2} = ', results)
print('Exponent----------------------------------------------------------------')
results = number_int_1**number_int_2
print(type(results), f'{number_int_1} ^ {number_int_2} = ', results)
results = number_float_1**number_int_2
print(type(results), f'{number_float_1} ^ {number_int_2} = ', results)
results = number_int_1 ** number_float_1
print(type(results), f'{number_int_1} ^ {number_float_1} = ', results)
print('Module------------------------------------------------------------------')
results = number_int_1 // number_int_2
print(type(results), f'{number_int_1} // {number_int_2} = ', results)
results = number_int_1 % number_int_2
print(type(results), f'{number_int_1} % {number_int_2} = ', results)
