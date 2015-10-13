students = ['Alex Plim', 'Stan Krat', 'Alex Karter', 'Pex Rom', 'Don Mahler', 'Don MacLech', 'Don Stivensson', 'Stan Deroy']

names = []
groups = []

for name in students: #getting all the names
    name = str(name)
    name = name.split(" ")
    names.append(name[0])

for name in set(names): #creating groups with the same names
    group = []
    for name2 in students:
        name = str(name)
        name2 = str(name2)
        if name[0] == name2[0]:
            group.append(name2)
    groups.append(group)

#print groups

for i in groups:
    print i