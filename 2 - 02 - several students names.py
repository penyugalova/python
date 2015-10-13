students = ['Alex Blim', 'Stan Krat', 'Rex Rom', 'Don Mahler']

n = len(students)

txt = '¬ведите номера студентов в формате число:число. ¬сего в списке сейчас {} студентов.'

number = []

number = raw_input(txt.format(n))

print(students[int(number[0]):int(number[2])])