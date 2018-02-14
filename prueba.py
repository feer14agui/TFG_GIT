#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import xml.etree.ElementTree as etree
from xml.dom.minidom import Document, parse
import xml.dom.minidom as dom

def HexadecimalToDecimal(n): #función para convertir los valores hexadecimales a decimales
	return str(int(n,16))

def porc(x,y):
    result = (x * 100.0) / (y)
    return result

def XML ():
	doc = Document()
	cont = doc.createElement("Contenidos")
	doc.appendChild(cont)

	data = doc.createElement("Datos")
	cont.appendChild(data)

	atributo = doc.createElement("atributo")
	data.appendChild(atributo)
	atributo.setAttribute("Nombre", "Memoria Total")
	ptext = doc.createTextNode(str(memory) + ' bytes')
	atributo.appendChild(ptext)

	atributo = doc.createElement("atributo")
	data.appendChild(atributo)
	atributo.setAttribute("Nombre", "Memoria Text")
	ptext = doc.createTextNode(str(memory_text) + ' bytes -- ' + str(percentage_text) + '% ')
	atributo.appendChild(ptext)

	atributo = doc.createElement("atributo")
	data.appendChild(atributo)
	atributo.setAttribute("Nombre", "Memoria Data")
	ptext = doc.createTextNode(str(memory_data) + ' bytes -- ' + str(percentage_data) + '% ')
	atributo.appendChild(ptext)

	atributo = doc.createElement("atributo")
	data.appendChild(atributo)
	atributo.setAttribute("Nombre", "Memoria Time")
	ptext = doc.createTextNode(str(memory_time) + ' bytes -- ' + str(percentage_time) + '% ')
	atributo.appendChild(ptext)

	atributo = doc.createElement("atributo")
	data.appendChild(atributo)
	atributo.setAttribute("Nombre", "Memoria Tdbs")
	ptext = doc.createTextNode(str(memory_tdbs) + ' bytes -- ' + str(percentage_tdbs) + '% ')
	atributo.appendChild(ptext)

	atributo = doc.createElement("atributo")
	data.appendChild(atributo)
	atributo.setAttribute("Nombre", "Memoria Time Text")
	ptext = doc.createTextNode(str(memory_time_text) + ' bytes -- ' + str(percentage_time_text) + '% ')
	atributo.appendChild(ptext)

	atributo = doc.createElement("atributo")
	data.appendChild(atributo)
	atributo.setAttribute("Nombre", "Memoria Tdbs Text")
	ptext = doc.createTextNode(str(memory_tdbs_text) + ' bytes -- ' + str(percentage_tdbs_text) + '% ')
	atributo.appendChild(ptext)

	atributo = doc.createElement("atributo")
	data.appendChild(atributo)
	atributo.setAttribute("Nombre", "Memoria Time Data")
	ptext = doc.createTextNode(str(memory_time_data) + ' bytes -- ' + str(percentage_time_data) + '% ')
	atributo.appendChild(ptext)

	atributo = doc.createElement("atributo")
	data.appendChild(atributo)
	atributo.setAttribute("Nombre", "Memoria Tdbs Data")
	ptext = doc.createTextNode(str(memory_tdbs_data) + ' bytes -- ' + str(percentage_tdbs_data) + '% ')
	atributo.appendChild(ptext)

	fich =  open('fichero.xml', 'w')
	xml = doc.toprettyxml(indent=" ")
	fich.write(xml)

def AddDicc():
	#Con esto meto el tamaño de datos en los diccionarios segun el modulo y el tipo de datos
    if mod == 'time': #si el modulo que tengo es time
        if types == '.text':
            module['Time']['Text'] = int(size) +  module['Time']['Text']#sumo la memoria de cada modulo y tipo
        if types == '.data':
            module['Time']['Data'] = int(size) +  module['Time']['Data']#sumo la memoria de cada modulo y tipo
    elif mod == 'tdbs': #si el modulo que tengo es tdbs
        if types == '.text':
            module['Tdbs']['Text'] = int(size) +  module['Tdbs']['Text']#sumo la memoria de cada modulo y tipo
        if types == '.data':
            module['Tdbs']['Data'] = int(size) +  module['Tdbs']['Data']#sumo la memoria de cada modulo y tipo

def TextMemory():
    memory_text = module['Time']['Text'] + module['Tdbs']['Text']
    return memory_text

def DataMemory():
    memory_data = module['Time']['Data'] + module['Tdbs']['Data']
    return memory_data

def TimeMemory():
    memory_time = module['Time']['Text'] + module['Time']['Data']
    return memory_time

def TdbsMemory():
    memory_tdbs = module['Tdbs']['Text'] + module['Tdbs']['Data']
    return memory_tdbs

def TimeTextMemory():
	memory_time_text = module['Time']['Text']
	return memory_time_text

def TdbsTextMemory():
	memory_tdbs_text = module['Tdbs']['Text']
	return memory_tdbs_text

def DataTimeMemory():
	memory_time_data = module['Time']['Data']
	return memory_time_data

def DataTdbsMemory():
	memory_tdbs_data = module['Tdbs']['Data']
	return memory_tdbs_data

infile = open('texto.map', 'r')

memory = 0

i=0

module = {'Time':{'Text':0, 'Data':0}, 'Tdbs' :{'Text':0, 'Data':0}}

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
percentage_text = porc((memory_text), memory)
percentage_data = porc((memory_data), memory)

#Uno los datos y las etiquetas para la representación de datos
data_types=[percentage_text, percentage_data]
label = ["Text " + str(percentage_text) + " %", "Data " + str(percentage_data) + " %"]
explode = [0,0]

#represento los datos
plt.subplot(3,1,1)
plt.pie(data_types, labels = label, explode = explode)  # Dibuja un gráfico de quesitos

# Con esto voy a recopilar datos para escribir lo que ocupa cada tipo de datos
memory_time = TimeMemory()
memory_tdbs = TdbsMemory()

#saco los porcentajes
percentage_time = porc((memory_time), memory)
percentage_tdbs = porc((memory_tdbs), memory)

#Uno los datos y las etiquetas para la representación de datos
data_types = [percentage_time, percentage_tdbs]
label = ["Time " + str(percentage_time) + " %", "Tdbs " + str(percentage_tdbs) + "%"]
explode = [0, 0]

#represento los datos
plt.subplot(3,1,2)
plt.pie(data_types, labels = label, explode = explode)  # Dibuja un gráfico de quesitos

# Ahora quiero ver dentro de TIME cuantos datos son tipo TEXT
memory_time_text = TimeTextMemory()


# Ahora quiero ver dentro de TDBS cuantos datos son tipo TEXT
memory_tdbs_text = TdbsTextMemory()
# Ahora quiero ver dentro de TIME cuantos datos son tipo DATA
memory_time_data = DataTimeMemory()
# Ahora quiero ver dentro de TDBS cuantos datos son tipo DATA
memory_tdbs_data = DataTdbsMemory()

#saco los porcentajes
percentage_time_text = porc((memory_time_text), memory)
percentage_tdbs_text = porc((memory_tdbs_text), memory)
percentage_time_data = porc((memory_time_data), memory)
percentage_tdbs_data = porc((memory_tdbs_data), memory)

#Uno los datos y las etiquetas para la representación de datos
data_types = [percentage_time_text, percentage_tdbs_text, percentage_time_data, percentage_tdbs_data]
label = ["TEXT(Time)" + str(percentage_time_text) + " %", "TEXT(tdbs) " + str(percentage_tdbs_text) + "%", "DATA(time) " + str(percentage_time_data) + "%", "DATA(tdbs) " + str(percentage_tdbs_data) + "%"]
explode = [0, 0, 0, 0]

#represento los datos
plt.subplot(3,1,3)
plt.pie(data_types, labels = label, explode = explode)  # Dibuja un gráfico de quesitos
plt.show()#muestro las tres gráficas

XML()#genero el xml
