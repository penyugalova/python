import math

action = raw_input('¬ведите действие над числами. ¬озможны:' + '\n' +
'сложение (+)' + '\n' +
'вычетание (-)' + '\n' +
'умножение()' + '\n' +
'деление (/)' + '\n' +
'квадратный корень (sqrt)' + '\n' +
'степень (*)' + '\n' +
'факториал(!)' + '\n' +
'логарифм (log)'+ '\n' +
'косинус (cos)'+ '\n' +
'синус (sin)')

if action == '+':
    number1 = float(input('¬ведите первое число:'))
    number2 = float(input('¬ведите второе число:'))
    result = number1 + number2
    print(result)

elif action == '-':
    number1 = float(input('¬ведите первое число:'))
    number2 = float(input('¬ведите второе число:'))
    result = number1 - number2
    print(result)

elif action == '*':
    number1 = float(input('¬ведите первое число:'))
    number2 = float(input('¬ведите второе число:'))
    result = number1 * number2
    print(result)

elif action == '/':
    number1 = float(input('¬ведите первое число:'))
    number2 = float(input('¬ведите второе число:'))
    result = number1 / number2
    print(result)

elif action == '*':
    number1 = float(input('¬ведите число:'))
    number2 = float(input('¬ведите степень:'))
    result = number1 * number2
    print(result)

elif action == 'sqrt':
    number1 = float(input('¬ведите число:'))
    result = math.sqrt(number1)
    print(result)

elif action == '!':
    number1 = float(input('¬ведите число:'))
    result = math.factorial(number1)
    print(result)

elif action == 'log':
    number1 = float(input('¬ведите число:'))
    number2 = float(input('¬ведите основание логарифма:'))
    result = math.log(number1,number2)
    print(result)

elif action == 'sin':
    number1 = float(input('¬ведите число:'))
    result = math.sin(number1)
    print(result)

elif action == 'cos':
    number1 = float(input('¬ведите число:'))
    result = math.cos(number1)
    print(result)

else:
    print('Ќе знаю, что ты от мен€ хочешь:)')