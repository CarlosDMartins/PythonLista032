#4) Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
#tela o valor do índice de massa corporal desta pessoa (IMC).
import math

#Fórmula: IMC = peso / altura2
# - Obs: peso em quilos e altura em metros.

peso = float(input("Adicione seu peso:"))
altura = float(input("Coloque sua altura"))

imc = peso / math.pow(altura,2)

print("Seu índice de massa corporal (IMC) é", imc)