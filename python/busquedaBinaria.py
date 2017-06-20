#Algoritmo de Búsqueda Binaria
#Autor = "Luis Suárez"
#fecha = 20/06/2017 01:10 a.m
#Version de python 3.6.2
import math

def buscar(valorAbuscar):
    valores = [2, 4, 7, 10, 14, 15, 18, 20, 100, 250]
    #Asignacion Multiple Elegancia
    minimo, maximo, promedio, encontrado = 0, (len(valores)-1), 0, False
    while minimo <= maximo:
        promedio = (maximo + minimo) / 2
        #Redondeo hacia abajo math.floor(x) y para el redondeo hacia arriba(math.ceil(x))
        promedio = math.floor(promedio)
        if valores[promedio] == valorAbuscar:
            encontrado = True
            break
        if valores[promedio] < valorAbuscar:
            minimo = promedio + 1
        else:
            maximo = promedio - 1

    return encontrado



print (buscar(3))
