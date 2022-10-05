# 4. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
# respectivo índice. Imprima a idade e a altura na ordem inversa a ordem lida.

# Definido as variáveis 
idade1 = []
altura1 = []

# For irá realizar a função de repetição para o usuário digitar os valores das 5 pessoas
for i in range(1, 6):
    print('%dº Pessoa' %i)
    idade2 = int(input('Insira a idade: '))
    altura2 = float(input('Insira a altura: '))
    idade1.append(idade2)
    altura1.append(altura2)
    
# Print para imprimir a ordem em maneira crescente
print('Ordem lida')
print('Alturas')
print(altura1)

print('Idades')
print(idade1)    

# Print para imprimer a ordem descrecente
print('Ordem inversa')
print('Alturas')
print(altura1[::-1])

print('Idades')
print(idade1[::-1])
