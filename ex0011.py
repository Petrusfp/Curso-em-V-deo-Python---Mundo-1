#ex011: Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade
# de tintas necessárias para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
l = float(input("Digite a largura da parede em metros: "))
a = float(input("Digie a altura da parede em metros: "))
area = l * a
tinta = area / 2
print("A tinta necessária para pintar essa parede é",tinta)
