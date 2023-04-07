import locale

# João é um vendedor de calcinhas e ele precisa de um programa para digitaar em seu computador o nome e os valores em inteiros de seus produtos, faça um programa simples em python (console) para resolver este problema

nome = str(input('Digite o nome do produto: '))
valor_str = str(input(f'Digite o valor do produto, {nome}: R$'))
valor_str = valor_str.replace('.','').replace(',','.')
valor = float(valor_str)

# definir o locale como pt_BR para formatar valores em Real brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# formatar o valor em Real brasileiro com o símbolo "R$"
valor_formatado = locale.currency(valor, grouping=True)

print(f'Produto {nome} no valor {valor_formatado} foi armazenado com sucesso!')
