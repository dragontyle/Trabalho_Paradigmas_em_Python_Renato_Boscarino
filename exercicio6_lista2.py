# 5. Faça um Programa que leia uma estrutura A com 10 números inteiros, calcule e mostre a soma
# dos quadrados dos elementos desta estrutura.

# Definindo a variável
somaquadrados = 0
# For para realizar a criação da lista para digitação dos 10 números inteiros e in para realizar se está dentro do for
for i in range(10):
    somaquadrados += int(input(f"Digite o {i+1}º numero inteiro: ")) ** 2
print(f"A soma dos quadrados dos numeros digitados é {somaquadrados}")
