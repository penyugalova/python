import math

action = raw_input('������� �������� ��� �������. ��������:' + '\n' +
'�������� (+)' + '\n' +
'��������� (-)' + '\n' +
'���������()' + '\n' +
'������� (/)' + '\n' +
'���������� ������ (sqrt)' + '\n' +
'������� (*)' + '\n' +
'���������(!)' + '\n' +
'�������� (log)'+ '\n' +
'������� (cos)'+ '\n' +
'����� (sin)')

if action == '+':
    number1 = float(input('������� ������ �����:'))
    number2 = float(input('������� ������ �����:'))
    result = number1 + number2
    print(result)

elif action == '-':
    number1 = float(input('������� ������ �����:'))
    number2 = float(input('������� ������ �����:'))
    result = number1 - number2
    print(result)

elif action == '*':
    number1 = float(input('������� ������ �����:'))
    number2 = float(input('������� ������ �����:'))
    result = number1 * number2
    print(result)

elif action == '/':
    number1 = float(input('������� ������ �����:'))
    number2 = float(input('������� ������ �����:'))
    result = number1 / number2
    print(result)

elif action == '*':
    number1 = float(input('������� �����:'))
    number2 = float(input('������� �������:'))
    result = number1 * number2
    print(result)

elif action == 'sqrt':
    number1 = float(input('������� �����:'))
    result = math.sqrt(number1)
    print(result)

elif action == '!':
    number1 = float(input('������� �����:'))
    result = math.factorial(number1)
    print(result)

elif action == 'log':
    number1 = float(input('������� �����:'))
    number2 = float(input('������� ��������� ���������:'))
    result = math.log(number1,number2)
    print(result)

elif action == 'sin':
    number1 = float(input('������� �����:'))
    result = math.sin(number1)
    print(result)

elif action == 'cos':
    number1 = float(input('������� �����:'))
    result = math.cos(number1)
    print(result)

else:
    print('�� ����, ��� �� �� ���� ������:)')