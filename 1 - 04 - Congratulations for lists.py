a = [1, -20, 38, 0, 44]
b = [88, -20, 48, 4, 33, 2]

len_a = len(a)
len_b = len(b)

minimum = min(len_a, len_b)

for i in range(0, minimum):
    winner = min(a[i], b[i])

#* ... � ����� ����������� ����� ������ �� ������ ���������� �� ���� ����� ������� ���������, ������� ��� �������, � ������� �� ����� ������������ �������.
    if abs(a[i]-b[i]) < 15:
        modul = abs(a[i]-b[i])
        print('������ �������� �����: ' + str(modul) + ' ����������!')
        if a[i] == winner:
            index = a.index(winner)
            if index+modul > len_a:
                modul_index = int(modul%len_a)
                index = index + modul_index
                if index <= len_a:
                    print('�����, ������ ������ �� ������ �������, ������� � ����� ����������: ' + str(a[index]))
                else:
                    print('�����, ������ ������ �� ������ �������, ������� � ����� ����������: ' + str(a[index-len_a]))
            else:
                    print('�����, ������ ������ �� ������ �������, ������� � ����� ����������: ' + str(a[index+modul]))
        else:
            index = b.index(winner)
            if index+modul > len_b:
                modul_index = int(modul%len_b)
                index = index + modul_index
                if index <= len_b:
                    print('�����, ������ ������ �� ������ �������, ������� � ����� ����������: ' + str(b[index]))
                else:
                    print('�����, ������ ������ �� ������ �������, ������� � ����� ����������: ' + str(b[index-len_b]))
            else:
                    print('�����, ������ ������ �� ������ �������, ������� � ����� ����������: ' + str(a[index+modul]))
