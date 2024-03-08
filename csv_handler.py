import csv

csv_file = 'attendee.csv'

with open(csv_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

with open('attendees.txt', 'w', encoding='utf-8') as txtfile:
    # txtfile.write('First Name,Last Name,Email\n')

    for row in rows:
        new_row = '{},{},{}\n'.format(
            row['First Name'], row['Last Name'], row['Email']
        )
        txtfile.write(new_row)

print("Новый текстовый файл 'attendees.txt' создан успешно!")