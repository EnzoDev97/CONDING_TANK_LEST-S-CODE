# 04 - Faça um script que leia 10 números do usuário e informe se algum número foi inserido em sequência.
# Se mais de um número for repetido, informe ao menos um (caso no Exemplo 3).

lista= []
qtd_numero= 10

print('-'*100)
print ('\033[47m{:^100}\033[0m'.format('SEQUÊNCIA DE NÚMEROS'))
print('-'*100)
print('\n')


for x in range(qtd_numero):
   
    numero = int(input(''))
    number = [numero]
    lista.append(number)

print('\n')
print('-'*100)
print ('\033[44m{:^100}\033[0m'.format('LISTA DA SEQUÊNCIA DE NÚMEROS  DIGITADOS'))
print('-'*100)
print('\n')

print(lista)
print('_'*100)
print('\n')


repetidos = []


for a in range(len(lista)):
    for b in range(len(lista)):
        if a != b:
            if lista[a] == lista[b] and lista[a] not in repetidos:
                repetidos.append(lista[a])

print('\n')
print('-'*100)
print ('\033[43m{:^100}\033[0m'.format('\033[43mLISTA  DE NÚMEROS REPETIDOS DA LISTA PRINCIPAL'))
print('-'*100)
print('\n')

print(repetidos)
print('_'*100)