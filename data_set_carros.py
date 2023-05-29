import pandas as pd

car = pd.read_csv('carros.csv', sep=';')

print(car.head(50))

print('------------------------//------------------------//-------------------//--------------')

print('TIPOS DE DADOS DO DATASET')
print(car.dtypes)
print('')
print('Os tipos de dados das colunas são: STRING, FLOAT, INTEIRO E BOOLEANO')

print('--------------------//--------------------//------------------//-----------------')

print('DESCRIBE DAS COLUNAS ESPECÍFICAS QUILOMETRAGEM E VALOR')

describe_colunas = ['Quilometragem', 'Valor']

colunas_selecionadas = car[describe_colunas]

descricao = (colunas_selecionadas.describe()).round(0)


print(descricao)

print('')
print('O QUE ESSES VALORES SIGNIFICAM?')
print("""
count: número de valores não nulos na coluna
mean: média dos valores na coluna.
std: desvio padrão dos valores na coluna, que mede a dispersão dos dados.
min: valor mínimo presente na coluna.
25%: primeiro quartil dos dados, também conhecido como quartil inferior ou percentil 25.
50%: segundo quartil dos dados, também conhecido como mediana ou percentil 50. Representa o valor que divide a distribuição em duas partes iguais.
75%: terceiro quartil dos dados, também conhecido como quartil superior ou percentil 75.
max: valor máximo presente na coluna.""")

print('----------//------------------//------------------------')
print('')
print('MAIS INFORMAÇÕES DO DATASET COM A FUNÇÃO INFO().')
print(car.info())

print("""8- Com base no Dataset que estamos trabalhando, defina uma função para mostrar a quilometragem media de todos os carros
...sabendo que a formula é: km_media = km_total / (ano_atual - ano_fabricacao) /// A função tem que receber como parâmetros: o 
dataset e o ano atual. Execute a funçaõ e mostre o resultado.""")

#def quilometragem_media(dt_set, anno_atual):
#    ler_data = pd.read_csv()

print('9 - PESQUISA COM QUERIES', 'a)mostre os carros com motor "Diesel V8" ', sep="\n")

print(car.loc[car['Motor'] == 'Motor Diesel V8'])

print('b) Carros com motor 1.0 8v e com Valor menor que R$100.000')
b = (car['Motor'] == 'Motor 1.0 8v') & (car['Valor'] < 100000)
b_filtro = car.loc[b]
print(b_filtro)

print('c) Carros com média de km média de até 10000km com motor 1.8 16v')
c = (car['Quilometragem'] <= 10000) & (car['Motor'] == 'Motor 1.8 16v' )
c_filtro = car.loc[c]
print(c_filtro)

print('d) Listagem dos tipos de motores cadastrados')
motores_cadastrados = car['Motor']
Lista_motores = []
for c in motores_cadastrados:
    if c not in Lista_motores:
        Lista_motores.append(c)
print('MOTORES CADASTRADOS', Lista_motores, sep='=> ')

print('---------------//-------------------//--------------')
print('e) liste os carros com câmbio automático com valor abaixo de R$ 100.000')


def filtro_carros(row):
    acessorios = row['Acessórios']
    nome = row['Nome']
    valor = row['Valor']
    if 'Câmbio automático' in acessorios and valor < 100000:
        return True
    else:
        return False

carros_filtrados = car[car.apply(filtro_carros, axis=1)]

# Exibindo os carros filtrados
print(carros_filtrados)

print('--------//-----------------//--------------------')
print('')

print('f) liste os carros novos com "freios ABS" que custam acima de R$ 100.000')

def filtro_carros_abs(row):
    acessorios = row['Acessórios']
    nome = row['Nome']
    valor = row['Valor']
    if 'Freios ABS' in acessorios and valor > 100000:
        return True
    else:
        return False

carros_filtrados_abs = car[car.apply(filtro_carros_abs, axis=1)]

# Exibindo os carros filtrados
print(carros_filtrados_abs)

print('-------------//-------------//-----------------')
print('')

print('g) liste os carros novos ou usados com km média abaixo de 10.000 km que custam até R$ 100.000')

def filtro_carros_nu(row):
    quilometragem = row['Quilometragem']
    nome = row['Nome']
    valor = row['Valor']
    if quilometragem < 10000 and valor <= 100000:
        return True
    else:
        return False

carros_filtrados_nu = car[car.apply(filtro_carros_nu, axis=1)]

# Exibindo os carros filtrados
print(carros_filtrados_nu)

