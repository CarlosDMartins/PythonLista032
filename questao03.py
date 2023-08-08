#3) Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
#programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.

peso = float(input("Coloque seu peso:"))
alt = float(input("Coloque sua altura:"))

gramas = peso * 1000
altura = alt * 100

print("Seu peso em gramas é", gramas,"e sua altura em centímetros é", altura)