#ex028: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador pensar num número
print("Pense em um número de 0 a 5.")
sleep(3)
jogador = int(input("Que número você pensou? "))

if jogador == computador:
    print("Você acertou!")
else:
    print("Errou, o número era {}, não {}".format(computador, jogador))
    