# ex:017: Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo, calcule o mostre o comprimento da hipotenusa.
import math
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(co,ca)
print("O valor da hipotenura é de",hipotenusa)
