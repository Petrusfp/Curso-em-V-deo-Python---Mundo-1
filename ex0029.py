#ex029: Escreva um programa que leia a velocidade de uma carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.
velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    velocidade2 = velocidade - 80
    multa = velocidade2 * 7
    print("Está acima do limite de velocidade! A multa será de R${:.2f}.".format(multa))
else:
    print("O limite de velocidade está dentro do permitido!")
