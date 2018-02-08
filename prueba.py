#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot

def HexadecimalToDecimal(n): #función para convertir los valores hexadecimales a decimales
	return str(int(n,16))

def porc(x,y):
    result = (x * 100.0) / (y)
    return result

def XML ():
    fichero =  open('fichero.xml', 'w')
    xml = "<?xml version='1.0' encoding='UTF-8' ?>\n"
    xml += '<MemoriaTotal=" ' + str(memory) + ' bytes">'
    xml += '</MemoriaTotal>\n'
    xml += '<DatosTipoTexto=" ' + str(memory_text) + ' bytes">'
    xml += '</DatosTipoTexto>\n'
    xml += '<DatosTipoData=" ' + str(memory_data) + ' bytes">'
    xml += '</DatosTipoData>\n'
    xml += '<DatosModTime=" ' + str(memory_time) + ' bytes">'
    xml += '</DatosModTime>\n'
    xml += '<DatosModTdbs=" ' + str(memory_tdbs) + ' bytes">'
    xml += '</DatosModTdbs>\n'
    xml += '<DatosTimeText=" ' + str(memory_time_text) + ' bytes">'
    xml += '</DatosTimeText>\n'
    xml += '<DatosTdbsText=" ' + str(memory_tdbs_text) + ' bytes">'
    xml += '</DatosTdbsText>\n'
    xml += '<DatosTimeData=" ' + str(memory_time_data) + ' bytes">'
    xml += '</DatosTimeData>\n'
    xml += '<DatosTdbsData=" ' + str(memory_tdbs_data) + ' bytes">'
    xml += '</DatosTdbsData>\n'
    fichero.write(xml)

def AddDicc():
	#Con esto meto el tamaño de datos en los diccionarios segun el modulo y el tipo de datos
    if mod == 'time': #si el modulo que tengo es time
        if types == '.text':
            Modulo['Type']['Time']['Text'] = int(size) +  Modulo['Type']['Time']['Text']#sumo la memoria de cada modulo y tipo
        if types == '.data':
            Modulo['Type']['Time']['Data'] = int(size) +  Modulo['Type']['Time']['Data']#sumo la memoria de cada modulo y tipo
    elif mod == 'tdbs': #si el modulo que tengo es tdbs
        if types == '.text':
            Modulo['Type']['Tdbs']['Text'] = int(size) +  Modulo['Type']['Tdbs']['Text']#sumo la memoria de cada modulo y tipo
        if types == '.data':
            Modulo['Type']['Tdbs']['Data'] = int(size) +  Modulo['Type']['Tdbs']['Data']#sumo la memoria de cada modulo y tipo

def TextMemory():
    memory_text = Modulo['Type']['Time']['Text'] + Modulo['Type']['Tdbs']['Text']
    return memory_text

def DataMemory():
    memory_data = Modulo['Type']['Time']['Data'] + Modulo['Type']['Tdbs']['Data']
    return memory_data

def TimeMemory():
    memory_time = Modulo['Type']['Time']['Text'] + Modulo['Type']['Time']['Data']
    return memory_time

def TdbsMemory():
    memory_tdbs = Modulo['Type']['Tdbs']['Text'] + Modulo['Type']['Tdbs']['Data']
    return memory_tdbs

infile = open('texto.map', 'r')

memory = 0

i=0

Modulo = {'Type' : {'Time':{'Text':0, 'Data':0}, 'Tdbs' :{'Text':0, 'Data':0}}}

for line in infile:

    dicc=line.split("/")
    cad=dicc[0]
    cad=cad.split("		")
    types=cad[0]
    if cad[0][0:1] != ' ':#uso este if para quitarme las líneas que no debo de coger
        i = i + 1
        cad=cad[2]#me quedo con la parte donde está el tamaño
        cad=cad.split(" ")
        mod = dicc[5]#obtengo el módulo de cada línea
        size=cad[0]#obtengo el tamaño de los datos
        size = HexadecimalToDecimal(size)#paso el tamaño a decimal
        memory = memory + int(size)#sumo la memoria total

    #Esto me sirve para ver que va cogiendo bien la lineas
    if types[0:1] != ' ':#uso esto para quitarme las líneas que no debo de coger
        print 'Datos de la línea número ' + str(i) + '\n'
        print 'Tipo de datos: ' + types
        print 'Tamaño de datos: ' + size + ' bytes'
        print 'Módulo: ' + mod + '\n'

    AddDicc()#Meto los valores en el diccionario

# Con esto voy a recopilar datos para escribir lo que ocupa cada tipo de datos
memory_text = TextMemory()
memory_data = DataMemory()

#saco los porcentajes
porcentaje_text = porc((memory_text), memory)
porcentaje_data = porc((memory_data), memory)

#Uno los datos y las etiquetas para la representación de datos
data_types=[porcentaje_text, porcentaje_data]
label = ["Text " + str(porcentaje_text) + " %", "Data " + str(porcentaje_data) + " %"]
explode = [0,0]

#represento los datos
plt.subplot(3,1,1)
plt.pie(data_types, labels = label, explode = explode)  # Dibuja un gráfico de quesitos

# Con esto voy a recopilar datos para escribir lo que ocupa cada tipo de datos
memory_time = TimeMemory()
memory_tdbs = TdbsMemory()

#saco los porcentajes
porcentaje_time = porc((memory_time), memory)
porcentaje_tdbs = porc((memory_tdbs), memory)

#Uno los datos y las etiquetas para la representación de datos
data_types = [porcentaje_time, porcentaje_tdbs]
label = ["Time " + str(porcentaje_time) + " %", "Tdbs " + str(porcentaje_tdbs) + "%"]
explode = [0, 0]

#represento los datos
plt.subplot(3,1,2)
plt.pie(data_types, labels = label, explode = explode)  # Dibuja un gráfico de quesitos

# Ahora quiero ver dentro de TIME cuantos datos son tipo TEXT
memory_time_text = Modulo['Type']['Time']['Text']
# Ahora quiero ver dentro de TDBS cuantos datos son tipo TEXT
memory_tdbs_text = Modulo['Type']['Tdbs']['Text']
# Ahora quiero ver dentro de TIME cuantos datos son tipo DATA
memory_time_data = Modulo['Type']['Time']['Data']
# Ahora quiero ver dentro de TDBS cuantos datos son tipo DATA
memory_tdbs_data = Modulo['Type']['Tdbs']['Data']

#saco los porcentajes
porcentaje_time_text = porc((memory_time_text), memory)
porcentaje_tdbs_text = porc((memory_tdbs_text), memory)
porcentaje_time_data = porc((memory_time_data), memory)
porcentaje_tdbs_data = porc((memory_tdbs_data), memory)

#Uno los datos y las etiquetas para la representación de datos
data_types = [porcentaje_time_text, porcentaje_tdbs_text, porcentaje_time_data, porcentaje_tdbs_data]
label = ["TEXT(Time)" + str(porcentaje_time_text) + " %", "TEXT(tdbs) " + str(porcentaje_tdbs_text) + "%", "DATA(time) " + str(porcentaje_time_data) + "%", "DATA(tdbs) " + str(porcentaje_tdbs_data) + "%"]
explode = [0, 0, 0, 0]

#represento los datos
plt.subplot(3,1,3)
plt.pie(data_types, labels = label, explode = explode)  # Dibuja un gráfico de quesitos
plt.show()#muestro las tres gráficas

XML()
