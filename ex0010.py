#ex010: Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar Considere US$ 1,00 = R$ 3,27
n = float(input("Digite quanto você tem na carteira: R$"))
d = n / 3.27
print("Com R${} você pode comprar U${:.1f}".format(n,d))
