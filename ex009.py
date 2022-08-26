#ex009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada
n = int(input("Digite um número: "))
i = 0
while i <= 10:
    print(n ,"x",i,"=", n * i)
    i = i + 1
