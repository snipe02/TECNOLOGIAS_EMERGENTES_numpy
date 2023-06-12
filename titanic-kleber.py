import pandas as pd

titanic = pd.read_csv('titanicc.csv')

print(titanic.head(50))

print("""a) percentual de passageiros sobreviventes do sexo masculino //
       OBSERVAÇÃO: Na coluna 'survided', temos que 0 = MORTO e 1 == SOBREVIVENTE""")

print('QUANTIDADE DE HOMENS')
soma_dos_homens = ((titanic['Sex'] == 'male').sum())
print(soma_dos_homens)



print('QUANTIDADE DE SOBREVIVENTES HOMENS')
linhas_homens_sobreviventes = (titanic['Survived'] == 1) & (titanic['Sex'] == 'male')
novo_data_frame_criado_homens_sobrevivente = titanic[linhas_homens_sobreviventes]

print(len(novo_data_frame_criado_homens_sobrevivente))

print('----------------')

print('PORCENTAGEM DOS SOBREVIVENTES')

porcentagem_sobreviventes_masculinos = (((len(novo_data_frame_criado_homens_sobrevivente)) / soma_dos_homens)*100).round(2)

print(f'{porcentagem_sobreviventes_masculinos} %')

print('------------------------------------')
print('------------------------------------')
print('------------------------------------')
print('------------------------------------')
print('------------------------------------')


print('b) Porcentagem de mulheres sobreviventes.')
print('TOTAL DE MULHERES SOBREVIVENTES')

soma_das_mulheres = ((titanic['Sex'] == 'male').sum())
print(soma_das_mulheres)



print('QUANTIDADE DE SOBREVIVENTES MULHERES')
linhas_mulheres_sobreviventes = (titanic['Survived'] == 1) & (titanic['Sex'] == 'female')
novo_data_frame_criado_mulheres_sobrevivente = titanic[linhas_mulheres_sobreviventes]

print(len(novo_data_frame_criado_mulheres_sobrevivente))

print('----------------')

print('PORCENTAGEM DOS SOBREVIVENTES')

porcentagem_sobreviventes_feminino = (((len(novo_data_frame_criado_mulheres_sobrevivente)) / soma_das_mulheres)*100).round(2)

print(f'{porcentagem_sobreviventes_feminino} %')

print('------------------------------------')
print('------------------------------------')
print('------------------------------------')
print('------------------------------------')
print('------------------------------------')

print('c) quantidade de crianças <= 12 de idade, mortas ')
crianças_menor_12_mortas = (titanic['Survived'] == 1) & (titanic['Sex'] == 'female')
novo_data_frame_criado_crianças_menor_12_mortas = titanic[crianças_menor_12_mortas]

print(f'quantidade de crianças menores ou de 12 de idade mortas é de {len(novo_data_frame_criado_crianças_menor_12_mortas)}')

print('------------------------------------')
print('------------------------------------')
print('------------------------------------')
print('------------------------------------')
print('------------------------------------')

print('d) quantidade de sobreviventes por classe')
agrupando = titanic.groupby('Pclass')



print((agrupando['Survived'].sum()).round(2))


