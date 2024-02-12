import csv

total_adult = total_pensioner = total_child =  0.0

with open('products.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        total_adult += float(row['Взрослый'])
        total_pensioner += float(row['Пенсионер'])
        total_child += float(row['Ребенок'])

print(f"{total_adult:.2f} {total_pensioner:.2f} {total_child:.2f}")