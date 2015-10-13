students = ['Alex Plim', 'Stan Krat', 'Pex Rom', 'Don Mahler']

for name in students:
    name = str(name)
    if name.find('p')!= -1:
        print name
    else:
        continue