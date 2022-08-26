#ex013: Faça um algoritmo que leia o salário de uma funcionário e mostre seu novo salário, com 15% de aumento
sa = float(input("Digite o salário R$"))
sn = (sa + (sa * (15/100)))
print("O novo salário é de R${:.2f}".format(sn))
