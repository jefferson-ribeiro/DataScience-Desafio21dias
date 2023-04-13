import os
import time


def mensagem_com_pausa(msg):
    os.system('clear')
    print(msg)
    time.sleep(2)
    os.system('clear')

def menu():
    os.system('clear')  # limpa o console
    print("-" * 20)
    print("O que você deseja fazer?")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")