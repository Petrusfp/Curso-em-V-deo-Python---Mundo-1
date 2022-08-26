#ex015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
#carro custa R$ 60 por dia e R$ 0,15 por Km rodado
km = int(input("Digite a quantidade de Km percorridos: "))
dia = int(input("Digite a quantidade de dias: "))
preçokm = km * 0.15
preçodias = dia * 60
soma = preçokm + preçodias
print("O preço a ser pago é de R$",soma)
