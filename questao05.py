#5) Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
#números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
#multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
#do primeiro pelo segundo número

num1 = float(input("Adicione um número:"))
num2 = float(input("Adicione um segundo número:"))

soma = num1 + num2
sub = num1 - num2
sub2 = num2 - num1
multi = num1 * num2
div = num1 / num2
rest = num1 % num2

print("Resultado da soma:",soma)
print("Resultado da subtração:",sub)
print("Resultado da segunda subtração:",sub2)
print("Resultado da multiplicação:",multi)
print("Resultado da divisão:",div)
print("Resto da divisão:",rest)

