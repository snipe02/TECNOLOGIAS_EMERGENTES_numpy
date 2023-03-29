import numpy as np

# Criando um array numpy
a = np.array([1, 2, 3])

# Imprimindo o array
print("Array a:")
print(a)

# Acessando elementos individuais do array
print("Primeiro elemento de a:", a[0])
print("Segundo elemento de a:", a[1])

# Operações matemáticas básicas com arrays
b = np.array([4, 5, 6])
print("Array b:")
print(b)
print("Soma de a e b:", a + b)
print("Subtração de a e b:", a - b)
print("Multiplicação de a e b:", a * b)
print("Divisão de a e b:", a / b)

# Funções matemáticas básicas em arrays
print("Média de a:", np.mean(a))
print("Desvio padrão de a:", np.std(a))
print("Seno de b:", np.sin(b))
print("Máximo de b:", np.max(b))

# Indexação booleana
c = np.array([10, 20, 30, 40])
print("Array c:")
print(c)
boolean_index = c > 20
print("Indexação booleana de c:", boolean_index)
print("Elementos maiores que 20 em c:", c[boolean_index])
