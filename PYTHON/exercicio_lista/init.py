import pessoas.funcoes as fnp
import telas.funcoes as fnt

pessoas = []

while True:
    fnt.menu()
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        fnp.cadastra_pessoa()
    elif opcao == "2":
        fnp.mostra_pessoas()
    elif opcao == "3":
        fnt.mensagem_com_pausa('Encerrando o programa...')
        break
    else:
        fnt.mensagem_com_pausa("Opção inválida. Tente novamente.")
