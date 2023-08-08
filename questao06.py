#6) Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
#ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
#exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
#do mês.

nome = input("Qual é o seu nome?")
sal = float(input("Coloque o seu salário:"))
vendas = int(input("Total de vendas em dinheiro é:"))

com = vendas + vendas / 100 * 15
saltotal =  sal + com

print("Seu nome",nome)
print("Seu salário",sal)
print("Sua comissão é",com)
print("Seu salário completo é R$", saltotal)