students = ['Alex Blim', 'Stan Krat', 'Rex Rom', 'Don Mahler']

n = len(students)
txt = '������� ����� ��������. ����� �� � ����� ������ {}'
number = input(txt.format(n))

number = number -1

print(students[number])