#ex012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input("Digite o preço R$"))
nv = p - (p * (5/100))
print("O novo preço é R$",nv)
