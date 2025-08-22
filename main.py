import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


## recebe dois arrays do tipo numpy
## executa calculo do Beta em "calculo.png"
def calcula_M(lista_x, lista_y):
    m = sum((lista_x - np.mean(lista_x)) * (lista_y - np.mean(lista_y))) / sum((lista_x - np.mean(lista_x))**2)
    return m


## recebe dois arrays do tipo numpy
## executa calculo do Alfa em "calculo.png"
def calcula_b(lista_x, lista_y):
  b = np.mean(lista_y) - calcula_M(lista_y, lista_x) * np.mean(lista_x)
  return b


## recebe dois arrays do tipo numpy, um valor de a e outro de b
## retorna somatória dos erros de uma tentativa de a e b
def calcula_erro(a, b, lista_x, lista_y):
    erro_total = 0
    for i in range(len(lista_y)):
        y = a*lista_x[i] + b
        erro_total += (lista_y[i] - y)**2
    return erro_total


## converte um excel em um dataframe tipo pandas
data = pd.read_excel("data.xlsx")
## converter coluna x to dataframe para um array tipo numpy
data_x = data['x'].to_numpy()
## converter coluna y to dataframe para um array tipo numpy
data_y = data['y'].to_numpy()


## array de 100 valores "aleatórios" entre -10 e 10
array_a = np.linspace(-10, 10, 100)
## array de 100 valores "aleatórios" entre -5 e 5
array_b = np.linspace(-5, 5, 100)
## já guardar a primeira amostra como menor
amostra_do_menor_erro = {
    "a": array_a[0],
    "b": array_b[0],
    "erro": calcula_erro(array_a[0], array_b[0], data_x, data_y)}
## cria um array ou matriz de determinado tamanho
## aqui serve para armazenar todos os erros
erros = np.zeros(shape=(100, 100))


print(calcula_M(data_x, data_y))

##  enumerate pega tanto índice como valor
for ind_a,num_a in enumerate(array_a):
    for ind_b,num_b in enumerate(array_b):
        erro = calcula_erro(num_a,num_b, data_x, data_y)
        if erro < amostra_do_menor_erro["erro"]:
            amostra_do_menor_erro["a"] = num_a
            amostra_do_menor_erro["b"] = num_b
            amostra_do_menor_erro["erro"] = erro
        erros[ind_a, ind_b] = erro