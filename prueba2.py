#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot

class datos():
    tipo = ''
    modulo = ''
    size = ''
    
class size():
    time = ''
    tdbs = ''
    
#memory = size.time + siez.tdbs
memory = 0

#Preguntas: ¿El valor del tamaño cuando lo paso a decimal en que unidades está?
#				¿Cómo meter las tres variables (tipo, tamaño y modulo) en un record?¿Podría utilizar django?

def HexadecimalToDecimal(n): #función para convertir los valores hexadecimales a decimales
	return str(int(n,16))

infile = open('texto.map', 'r')

def porc(x,y):
    result = (x * 100.0) / (y)
    return result

i=0
array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
porcentaje = [0, 0, 0, 0, 0, 0, 0, 0, 0]

Modulo = {'Type' : {'Time':{'Size': 0, 'Datos':''}, 'Tdbs' : {'Size': 0, 'Datos':''} }}

for line in infile:
	#texto = infile.readline()
	i = i + 1
	texto=line
	dicc=texto.split("/")
	size=dicc[0]
	size=size.split("		")
	types=size[0]
	size=size[2]
	size=size.split(" ")
	size=size[0]
	datos.modulo=dicc[5] #me quedo con el modulo de la funcion
	
	size = HexadecimalToDecimal(size)
	datos.size = size
	memory = memory + int(size)
	if datos.modulo == 'time':
        	print 'time'
	
	
	print 'Datos de la línea número ' + str(i) + '\n'
	print 'Tipo de datos: ' + types
	print 'Tamaño de datos: ' + datos.size + ' bytes'
	print 'Módulo: ' + datos.modulo + '\n'
	array[i] = datos.size
	
	
#porcentaje[1] = (int(array[1]) * 100) / (int(array[1]) + int(array[2]))
#porcentaje[2] = (int(array[2]) * 100) / (int(array[1]) + int(array[2]))

    
porcentaje[1] = porc(int(array[1]), memory)
porcentaje[2] = porc(int(array[2]), memory)
porcentaje[3] = porc(int(array[3]), memory)

visitas = [porcentaje[1] + porcentaje[3], porcentaje[2]]
label = ["Time " + str(porcentaje[1] + porcentaje[3]) + " %", "Tdbs " + str(porcentaje[2]) + "%"]
explode = [0, 0]

plt.pie(visitas, labels = label, explode = explode)  # Dibuja un gráfico de quesitos
plt.show()


