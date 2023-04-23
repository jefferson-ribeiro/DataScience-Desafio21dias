import csv

# Abre o arquivo CSV
with open('vitimas_de_covid_brasil_2020.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    # Itera pelas linhas do arquivo e imprime os dados
    for row in reader:
        print(', '.join(row))
