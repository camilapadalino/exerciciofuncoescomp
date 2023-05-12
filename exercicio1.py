"""
Crie uma função que receba três númeroscomo parâmetros, e retorne Truese a soma de quaisquer
 pares de números gera a soma do terceiro número. Caso contrário retorne False.
"""
def soma_num(num1,num2,num3):
    if num1 + num2 == num3 or num2 + num3 == num1 or num1 + num3 == num2:
        print("True")
    else: 
        print("False")

num1 = int(input('Insira um número: '))
num2 = int(input('Insira um outro número: '))
num3 = int(input('Insira um último número: '))
soma_num(num1,num2,num3)

