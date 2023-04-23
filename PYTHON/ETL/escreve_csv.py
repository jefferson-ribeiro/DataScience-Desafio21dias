import csv
import random

# Dicionário com as siglas dos estados e suas respectivas cidades
cidades = {
    'SP': ['São Paulo', 'Campinas', 'São José dos Campos', 'Santo André', 'São Bernardo do Campo'],
    'RJ': ['Rio de Janeiro', 'Niterói', 'Campos dos Goytacazes', 'Petrópolis', 'Nova Iguaçu'],
    'MG': ['Belo Horizonte', 'Uberlândia', 'Juiz de Fora', 'Montes Claros', 'Contagem'],
    'RS': ['Porto Alegre', 'Caxias do Sul', 'Pelotas', 'Santa Maria', 'Rio Grande'],
    'BA': ['Salvador', 'Feira de Santana', 'Vitória da Conquista', 'Juazeiro', 'Ilhéus']
}

# Criação do arquivo CSV
with open('vitimas_de_covid_brasil_2020.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['id', 'cidade', 'estado', 'numero_de_vitimas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    # Geração de 100 linhas de dados aleatórios
    for i in range(1, 101):
        estado = random.choice(list(cidades.keys()))
        cidade = random.choice(cidades[estado])
        numero_de_vitimas = random.randint(1, 1000)
        writer.writerow({'id': i, 'cidade': cidade, 'estado': estado, 'numero_de_vitimas': numero_de_vitimas})
