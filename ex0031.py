#ex031: Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
# para viagens de até 200km e R$ 0,45 para viagens mais longas.
distancia = float(input("Digite a distância de uma viagem: "))
valor = 0
if distancia <= 200:
    valor = distancia * 0.50
    print("O valor da passagem será de R${:.2f}".format(valor))
else:
    valor = distancia * 0.45
    print("O valor da passagem será de R${:.2f}".format(valor))
