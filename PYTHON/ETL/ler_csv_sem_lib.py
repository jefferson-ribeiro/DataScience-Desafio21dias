# Abre o arquivo CSV
with open('vitimas_de_covid_brasil_2020.csv', 'r', encoding='utf-8') as file:
    # Lê todas as linhas do arquivo
    lines = file.readlines()
    
    # Itera pelas linhas do arquivo e imprime os dados
    for line in lines:
        # Remove o caractere de nova linha do final da linha
        line = line.strip()
        
        # Separa os campos pelo separador de campo padrão (',')
        fields = line.split(',')
        
        # Imprime os campos separados por vírgula
        print(', '.join(fields))
