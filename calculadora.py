num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
operator = str(
    input('Enter the operator (1 For addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for exponentiation): ')
)

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