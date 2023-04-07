# Ffaça um programa para mim em python(console) que solicite 5 int e quatro float e some todos os numeros e mostre o resultado na tela formatado.

# solicitar 5 inteiros e 4 floats do usuário
numeros_int = [int(input(f'Digite o {i+1}º número inteiro: ')) for i in range(5)]
numeros_float = [float(input(f'Digite o {i+1}º número de ponto flutuante: ')) for i in range(4)]

# calcular a soma de todos os números
soma_total = sum(numeros_int) + sum(numeros_float)

# exibir o resultado formatado na tela
print(f'\nA soma total é: R$ {soma_total:.2f}')
