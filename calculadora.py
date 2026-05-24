num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

print('Enter the operator:')
print('\t1. Addition')
print('\t2. Subtraction')
print('\t3. Multiplication')
print('\t4. Division')
print('\t5. Exponentiation')
operator = str(input('-> '))


if operator=='1':
    print('Result: ', num1+num2)
elif operator=='2':
    print('Result: ', num1-num2)
elif operator=='3':
    print('Result: ', num1*num2)
elif operator=='4':
    print('Result: ', num1/num2)
elif operator=='5':
    print('Result:', num1**num2)
else:
    print('Please insert a valid procedure.')