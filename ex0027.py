# ex027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza primeiro = Ana último = Souza
nome = str(input("Digite seu nome completo: ")).strip()
n = nome.split()
print("Primeiro nome: {}".format(n[0]))
print("Último nome: {}".format(n[len(n)-1]))
