#ex018: Faça um programa que leia um ângulo qualquer a mostre
# na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = int(input("Digite o ângulo: "))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print("O seno do ângulo é",seno,"o cosseno é",cosseno,"e a tangente é",tangente)
