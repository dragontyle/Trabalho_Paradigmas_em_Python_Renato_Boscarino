"2. Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar."

numero = float(input('Insira um número para saber se o número digitado é par ou impar:'))
resto = numero % 2

if resto == 0:
    print('Número é par')
else:
    print('Número é impar')
