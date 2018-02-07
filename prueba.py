#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot
from matplotlib.gridspec import GridSpec

class datos():
    tipo = ''
    modulo = ''
    size = ''

class size():
    time = ''
    tdbs = ''

memory = 0

def HexadecimalToDecimal(n): #función para convertir los valores hexadecimales a decimales
	return str(int(n,16))

infile = open('texto.map', 'r')

def porc(x,y):
    result = (x * 100.0) / (y)
    return result

i=0

Modulo = {'Type' : {'Time':{'Text':0, 'Data':0}, 'Tdbs' :{'Text':0, 'Data':0}}}

for line in infile:
	#texto = infile.readline()
    texto=line
    dicc=texto.split("/")
    size=dicc[0]
    size=size.split("		")
    types=size[0]
    if size[0][0:1] != ' ':#uso este if para quitarme las líneas que no debo de coger
        i = i + 1
        size=size[2]
        size=size.split(" ")
        mod = dicc[5]
        size=size[0]
        datos.modulo = mod
        size = HexadecimalToDecimal(size)
        memory = memory + int(size)

	#Con esto meto el tamaño de datos en los diccionarios segun el modulo y el tipo de datos
    if mod == 'time': #si el modulo que tengo es time
            if types == '.text':
                Modulo['Type']['Time']['Text'] = int(size) +  Modulo['Type']['Time']['Text']
            if types == '.data':
                Modulo['Type']['Time']['Data'] = int(size) +  Modulo['Type']['Time']['Data']
    elif mod == 'tdbs': #si el modulo que tengo es tdbs
            if types == '.text':
                Modulo['Type']['Tdbs']['Text'] = int(size) +  Modulo['Type']['Tdbs']['Text']
            if types == '.data':
                Modulo['Type']['Tdbs']['Data'] = int(size) +  Modulo['Type']['Tdbs']['Data']

	#Esto me sirve para ver que va cogiendo bien la lineas
    if types[0:1] != ' ':#uso esto para quitarme las líneas que no debo de coger
        print 'Datos de la línea número ' + str(i) + '\n'
        print 'Tipo de datos: ' + types
        print 'Tamaño de datos: ' + size + ' bytes'
        print 'Módulo: ' + mod + '\n'

# Con esto voy a recopilar datos para escribir lo que ocupa cada tipo de datos
memoria_text = Modulo['Type']['Time']['Text'] + Modulo['Type']['Tdbs']['Text']
memoria_data = Modulo['Type']['Time']['Data'] + Modulo['Type']['Tdbs']['Data']
#saco los porcentajes
porcentaje_text = porc((memoria_text), memory)
porcentaje_data = porc((memoria_data), memory)
#Uno los datos y las etiquetas para la representación de datos
tipos_datos=[porcentaje_text, porcentaje_data]
label = ["Text " + str(porcentaje_text) + " %", "Data " + str(porcentaje_data) + " %"]
explode = [0,0]
#represento los datos
plt.subplot(3,1,1)
plt.pie(tipos_datos, labels = label, explode = explode)  # Dibuja un gráfico de quesitos

# Con esto voy a recopilar datos para escribir lo que ocupa cada tipo de datos
memoria_time = Modulo['Type']['Time']['Text'] + Modulo['Type']['Time']['Data']
memoria_tdbs = Modulo['Type']['Tdbs']['Text'] + Modulo['Type']['Tdbs']['Data']
#saco los porcentajes
porcentaje_time = porc((memoria_time), memory)
porcentaje_tdbs = porc((memoria_tdbs), memory)
#Uno los datos y las etiquetas para la representación de datos
visitas = [porcentaje_time, porcentaje_tdbs]
label = ["Time " + str(porcentaje_time) + " %", "Tdbs " + str(porcentaje_tdbs) + "%"]
explode = [0, 0]
#represento los datos
plt.subplot(3,1,2)
plt.pie(visitas, labels = label, explode = explode)  # Dibuja un gráfico de quesitos

# Ahora quiero ver dentro de TIME cuantos datos son tipo TEXT
memoria_time_text = Modulo['Type']['Time']['Text']
# Ahora quiero ver dentro de TDBS cuantos datos son tipo TEXT
memoria_tdbs_text = Modulo['Type']['Tdbs']['Text']
# Ahora quiero ver dentro de TIME cuantos datos son tipo DATA
memoria_time_data = Modulo['Type']['Time']['Data']
# Ahora quiero ver dentro de TDBS cuantos datos son tipo DATA
memoria_tdbs_data = Modulo['Type']['Tdbs']['Data']
#saco los porcentajes
porcentaje_time_text = porc((memoria_time_text), memory)
porcentaje_tdbs_text = porc((memoria_tdbs_text), memory)
porcentaje_time_data = porc((memoria_time_data), memory)
porcentaje_tdbs_data = porc((memoria_tdbs_data), memory)
#Uno los datos y las etiquetas para la representación de datos
visitas = [porcentaje_time_text, porcentaje_tdbs_text, porcentaje_time_data, porcentaje_tdbs_data]
label = ["TEXT(Time)" + str(porcentaje_time_text) + " %", "TEXT(tdbs) " + str(porcentaje_tdbs_text) + "%", "DATA(time) " + str(porcentaje_time_data) + "%", "DATA(tdbs) " + str(porcentaje_tdbs_data) + "%"]
explode = [0, 0, 0, 0]
#represento los datos
plt.subplot(3,1,3)
plt.pie(visitas, labels = label, explode = explode)  # Dibuja un gráfico de quesitos
plt.show()
