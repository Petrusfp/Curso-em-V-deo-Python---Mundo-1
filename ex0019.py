#ex019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
def main():

    import random
    a1 = input("Digite o nome do primeiro aluno: ")
    a2 = input("Digite o nome do segundo aluno: ")
    a3 = input("Digite o nome do terceiro aluno: ")
    a4 = input("Digite o nome do quarto aluno: ")
    lista = [a1, a2, a3, a4]
    escolhido = random.choice(lista)
    print("O aluno escolhido foi ",escolhido)

    restart = str(input('Voce deseja continuar?(sim/nao)'))
    if restart == 'sim':
        main()
    else:
        exit()

main()
