import csv

count_len = 0
count = 0
search = input('Введите имя автора:')
with open('books.csv') as csvfile:
    table = list(csv.reader(csvfile, delimiter=';'))
    for row in table[1:]:
        count += 1
        if len(row[1]) > 30:
            count_len += 1
        if float(row[7]) < 150 and row[3] == search:
            print(row[1])

print('Количество книг в файле:', count)
print('Количество книг у которых название длиннее 30 символов:', count_len)
with open('books.txt', 'w') as file:
    for i, note in enumerate(table[112:132]):
        stroka = str(i + 1) + ' ' + note[3] + '. ' + note[1] + ' - ' + note[6][6:10] + '\n'
        file.write(stroka)
