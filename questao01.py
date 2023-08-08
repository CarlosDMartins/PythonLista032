'''1) Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom'''

conta = float(input("Coloque o valor da conta:"))

acrr = conta + conta / 100 * 10

print("Valor total a se pagar:", acrr)