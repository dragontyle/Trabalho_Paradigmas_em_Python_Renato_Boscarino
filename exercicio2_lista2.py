#2. Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar.

#Inserindo a variável tipo float e colocando a informação para a digitação
numero = float(input('Insira um número para saber se o número digitado é par ou impar:'))
resto = numero % 2
#Definindo resto para a verifição se ele é divisível por 2 com o número digitado
#If usado para igualar o resultado do resto à 0 e definir se o número é par
if resto == 0:
    print('Número é par')
else:
    print('Número é impar')
#Else usado caso a número gerado não seja igualado a 0 na divisão por dois, sendo um número não divisível por dois, então ele é ímpar, sendo um número quebrado
