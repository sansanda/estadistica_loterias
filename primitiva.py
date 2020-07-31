
import requests
from requests.auth import HTTPBasicAuth

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


url = 'https://www.loteriasyapuestas.es/servicios/buscadorSorteos'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
fechaInicioInclusiva = '20200701'  #formato aaaammdd
fechaFinInclusiva = '20200730'     #formato aaaammdd

#fechaInicioInclusiva = '20190101'   #formato aaaammdd
#fechaFinInclusiva = '20191231'      #formato aaaammdd

params = {'game_id':'LAPR', 'celebrados':'true', 'fechaInicioInclusiva':fechaInicioInclusiva,'fechaFinInclusiva':fechaFinInclusiva}

auth = HTTPBasicAuth('dsanchezsanc@uoc.edu','d1392an4Mtx23')
response = requests.get(url, params=params, headers=headers, auth = auth).json()

lista_posibles_numeros = [i for i in range(49)]
repeticiones_posibles_numeros = [0 for i in range(49)]
repeticiones_posibles_reintegros = [0 for i in range(10)]


for sorteo in response:

    # los 6 primeros numeros de la lista con la comb ganadora
    # el septimo es el complementario
    # el octavo es el reintegro
    combinacion_ganadora = str(dict(sorteo)['combinacion']).replace(" ","").split("-")

    #Eliminamos los caracteres indeseados y obtenemos el C y el R
    last = combinacion_ganadora[-1]
    combinacion_ganadora[-1] = last[0:2]
    combinacion_ganadora.append(last[4:6])
    combinacion_ganadora.append(last[9:10])
    #print(combinacion_ganadora)
    #convertimos la lista de str a una lista de ints
    combinacion_ganadora = [int(n) for n in combinacion_ganadora]
    #print(combinacion_ganadora)

    # no miramos el reintegro
    for n in combinacion_ganadora[0:len(combinacion_ganadora)-1]:
        repeticiones_posibles_numeros[n-1] = repeticiones_posibles_numeros[n-1] + 1

    # solo miramos el reintegro
    repeticiones_posibles_reintegros[combinacion_ganadora[-1]] = repeticiones_posibles_reintegros[combinacion_ganadora[-1]] + 1

#contamos la repeticion de los numeros
max_rep = 0

for n in range(0,len(repeticiones_posibles_numeros)):
    if repeticiones_posibles_numeros[n]>max_rep:
        max_rep = repeticiones_posibles_numeros[n]

for i in range(0,max_rep+1):
    print('numeros con ',i, 'repeticiones')
    l = list()
    for n in range(0,len(repeticiones_posibles_numeros)):
        if repeticiones_posibles_numeros[n] == i:
            l.append(n+1)
    print(l)

#print(repeticiones_posibles_reintegros)

max_rep = 0

for n in range(0,len(repeticiones_posibles_reintegros)):
    if repeticiones_posibles_reintegros[n]>max_rep:
        max_rep = repeticiones_posibles_reintegros[n]

for i in range(0,max_rep+1):
    print('reintegros con ',i, 'repeticiones')
    l = list()
    for n in range(0,len(repeticiones_posibles_reintegros)):
        if repeticiones_posibles_reintegros[n] == i:
            l.append(n)
    print(l)

#graficamos usando pandas
