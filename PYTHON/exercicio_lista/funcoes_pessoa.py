import os
import time

def cadastra_pessoa(pessoas):
    os.system('clear')
    print("CADASTRO DE USUÁRIOS")
    pessoa = {}
    pessoa["nome"] = input("Digite o nome: ")
    pessoa["idade"] = input("Digite a idade: ")
    pessoa["cidade"] = input("Digite a cidade: ")
    pessoas.append(pessoa)
    time.sleep(2)
    return pessoas

def pessoa_formatada(pessoa):
    return f"""
Nome: {pessoa['nome']}
Idade: {pessoa['idade']}
Cidade: {pessoa['cidade']}"""

def mostra_pessoas(pessoas):
    os.system('clear')
    print("LISTA DE USUÁRIOS")
    if len(pessoas) == 0:
        print("Não há usuários cadastrados.")
    else:
        for pessoa in pessoas:
            print("-" * 20)
            retorno = pessoa_formatada(pessoa)
            print(retorno)
    input("\nPressione Enter para voltar ao menu...")
