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

def AddDicc(types):
	#Con esto meto el tamaño de datos en los diccionarios segun el modulo y el tipo de datos
	claves = module.keys() #obtengo todas las claves del diccionario
	if module.has_key(mod):#busco el modulo en el diccionario
		types = types.split('.')

		try:
			types = types[1]#separo el punto de .text para quedarme con text
		except IndexError:
			types = 'null'

		if types in module[mod].keys():#busco el tipo de datos en el diccionario
			module[mod][types] = int(size) + module[mod][types]#meto el tamaño del tipo y modulo en el diccionario
		elif not types in module[mod].keys() and types != 'null':
			module[mod].setdefault(types, 0)
			module[mod][types] = int(size) + module[mod][types]#meto el tamaño del tipo y modulo en el diccionario
	else:#si no encuentro el modulo en el diccionarios
		types = types.split('.')

		try:
			types = types[1]#separo el punto de .text para quedarme con text
		except IndexError:
			types = 'null'

		module[mod] = {types: 0}
		module[mod][types] = int(size) + module[mod][types]#meto el tamaño del tipo y modulo en el diccionario

def ModMemory():#Creo un diccionario con los modulos y sus tamaños
	for i in module.keys():
		for j in module[i].keys():
			if modmemory.has_key(i):
				modmemory[i] = module[i][j] + modmemory[i]
			else:
				modmemory[i] = module[i][j]
	return modmemory

def TypesMemory():#creo un diccionario con los tipos de datos y sus tamaños
	for i in module.keys():
		for j in module[i].keys():
			if typesmemory.has_key(j):
				typesmemory[j] = module[i][j] + typesmemory[j]
			else:
				typesmemory[j] = module[i][j]
	return typesmemory

def TimeMemory():
    memory_time = module['time']['text'] + module['time']['data']
    return memory_time

def TdbsMemory():
    memory_tdbs = module['tdbs']['text'] + module['tdbs']['data']
    return memory_tdbs

def TimeTextMemory():
	memory_time_text = module['time']['text']
	return memory_time_text

def TdbsTextMemory():
	memory_tdbs_text = module['tdbs']['text']
	return memory_tdbs_text

def DataTimeMemory():
	memory_time_data = module['time']['data']
	return memory_time_data

def DataTdbsMemory():
	memory_tdbs_data = module['tdbs']['data']
	return memory_tdbs_data

infile = open('texto.map', 'r')

memory = 0

i=0

module = {}
modmemory = {}
typesmemory = {}

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

    AddDicc(types)#Meto los valores en el diccionario
print module

#creo los diccionarios con los modulos y los tipos para poder sacar los datos bien al representar
Mod_Memory = ModMemory()
Types_Memory = TypesMemory()
#Creo arrays para meter los dados en label
label_array = []
data_array = []
#saco del diccionario de types los porcentajes y nombres para la representacion
for types in Types_Memory.keys():
	typememory = Types_Memory[types]
	percentagetype = porc((typememory),memory)
	label_array.append(types + ' ' + str(percentagetype) + '%')
	data_array.append(str(percentagetype))


#Uno los datos y las etiquetas para la representación de datos
data_types = data_array
label = label_array
explode = [0,0]

#represento los datos
plt.subplot(3,1,1)
print label
plt.pie(data_types, labels = label, explode = explode)  # Dibuja un gráfico de quesitos

#Creo arrays para meter los datos en label
label_array = []
mod_array = []
#Saco los modulos y sus porcentajes para la representacion de datos
for mods in Mod_Memory.keys():
	modmemory = Mod_Memory[mods]
	percentagemod = porc((modmemory),memory)
	label_array.append(mods + ' ' + str(percentagemod) + '%')
	mod_array.append(str(percentagemod))


#Uno los datos y las etiquetas para la representación de datos
mod_types = mod_array
label = label_array
explode = [0, 0]

#represento los datos
plt.subplot(3,1,2)
plt.pie(mod_types, labels = label, explode = explode)  # Dibuja un gráfico de quesitos

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

#XML()#genero el xml
