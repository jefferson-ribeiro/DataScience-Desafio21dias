import csv
import random

# Dicionário com as siglas dos estados e suas respectivas cidades
cidades = {
    'AC': ['Rio Branco', 'Cruzeiro do Sul', 'Senador Guiomard'],
    'AL': ['Maceió', 'Arapiraca', 'Rio Largo'],
    'AP': ['Macapá', 'Santana', 'Laranjal do Jari'],
    'AM': ['Manaus', 'Parintins', 'Itacoatiara'],
    'BA': ['Salvador', 'Feira de Santana', 'Vitória da Conquista'],
    'CE': ['Fortaleza', 'Caucaia', 'Juazeiro do Norte'],
    'DF': ['Brasília', 'Ceilândia', 'Taguatinga'],
    'ES': ['Vitória', 'Cariacica', 'Serra'],
    'GO': ['Goiânia', 'Aparecida de Goiânia', 'Anápolis'],
    'MA': ['São Luís', 'Imperatriz', 'Timon'],
    'MT': ['Cuiabá', 'Várzea Grande', 'Rondonópolis'],
    'MS': ['Campo Grande', 'Dourados', 'Três Lagoas'],
    'MG': ['Belo Horizonte', 'Uberlândia', 'Juiz de Fora'],
    'PA': ['Belém', 'Ananindeua', 'Santarém'],
    'PB': ['João Pessoa', 'Campina Grande', 'Santa Rita'],
    'PR': ['Curitiba', 'Londrina', 'Maringá'],
    'PE': ['Recife', 'Jaboatão dos Guararapes', 'Olinda'],
    'PI': ['Teresina', 'Parnaíba', 'Picos'],
    'RJ': ['Rio de Janeiro', 'Niterói', 'Petrópolis'],
    'RN': ['Natal', 'Mossoró', 'Parnamirim'],
    'RS': ['Porto Alegre', 'Caxias do Sul', 'Pelotas'],
    'RO': ['Porto Velho', 'Ji-Paraná', 'Ariquemes'],
    'RR': ['Boa Vista', 'Caracaraí', 'Rorainópolis'],
    'SC': ['Florianópolis', 'Joinville', 'Blumenau'],
    'SP': ['São Paulo', 'Campinas', 'São José dos Campos'],
    'SE': ['Aracaju', 'Nossa Senhora do Socorro', 'Lagarto'],
    'TO': ['Palmas', 'Araguaína', 'Gurupi'],
}


# Criação do arquivo CSV
with open('vitimas_de_covid_brasil_2020.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['id', 'cidade', 'estado', 'numero_de_vitimas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    # Geração de 100 linhas de dados aleatórios
    for i in range(1, 1000001):
        estado = random.choice(list(cidades.keys()))
        cidade = random.choice(cidades[estado])
        numero_de_vitimas = random.randint(1, 1000)
        writer.writerow({'id': i, 'cidade': cidade, 'estado': estado, 'numero_de_vitimas': numero_de_vitimas})
