# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:53:30 2022

@author: aleja
"""
import matplotlib.pyplot as plt
import random
import time

valores_de_n = [10**i for i in range(1,7)]
tiempos = [[],[]] #lista de listas


def busqueda_secuencial(lista, item):
    encontrado = False
    i = 0
    
    while i < len(lista) and not encontrado:
        if item == lista[i]:
            encontrado = True
            
        i += 1
    return encontrado

def busqueda_binaria(lista, item):
    encontrado = False
    primero = 0
    ultimo = len(lista)-1
    
    while primero <= ultimo and not encontrado:
        punto_medio = (primero + ultimo) //2 #division entera
        if lista[punto_medio] == item:
            encontrado == True
        elif lista[punto_medio] < item:
            primero = punto_medio + 1
        else:
            ultimo = punto_medio - 1
    return encontrado



for n in valores_de_n:
    lista = sorted([random.randint(-100, 100) for _ in range(n)]) #para busqueda binaria debe si o si estar ordenada
    
    tic = time.perf_counter()
    busqueda_secuencial(lista, 500)
    toc = time.perf_counter()
    tiempos[0].append(toc-tic)
    
    tic = time.perf_counter()
    busqueda_binaria(lista, 500)
    toc = time.perf_counter()
    tiempos[1].append(toc-tic)


plt.clf() #limpia el dibujo
plt.plot(valores_de_n, tiempos[0], label ="Busqueda secuencial")
plt.plot(valores_de_n, tiempos[1], label ="Busqueda binaria")
plt.xlabel("tamaños de lista")
plt.ylabel("tiempos del algoritmo")
plt.title("Tiempos en fn. del nro de elementos")
plt.legend()
    
