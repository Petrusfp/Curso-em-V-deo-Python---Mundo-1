# ex034: Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento.Para salários superiores a R$ 1.250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Digite o salário R$"))
if salario > 1250:
    salario = salario + ((10/100) * salario)
    print("O salário com 10% de aumento vira R${}".format(salario))
else:
    salario = salario + ((15/100) * salario)
    print("O salário com 15% de aumento vira R${}".format(salario))
