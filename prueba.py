#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot
import re
import lxml.etree as ET
import sys
#import lxml.etree.ElementTree as etree
#from xml.dom.minidom import Document, parse
#import xml.dom.minidom as dom

def HexadecimalToDecimal(n): #función para convertir los valores hexadecimales a decimales
    return str(int(n,16))

def porc(x,y):
    result = (x * 100.0) / (y)
    return result

def XML ():
    root = ET.Element("root")
    doc = ET.SubElement(root, "Datos")
    i = 1
    field1 = ET.SubElement(doc, "MemoriaTotal")
    field1.text = str(memory)
    doc2 = ET.SubElement(doc, "Memoria-Tipo-Datos")
    for types in Types_Memory.keys():
        i = i + 1
        field2 = ET.SubElement(doc2, "Memoria-" + str(types))
        percentage = porc((Types_Memory[types]), memory)
        ptext = ( str(Types_Memory[types]) + ' ' + str(percentage))
        field2.text = ptext

    doc3 = ET.SubElement(doc, "Memoria-Modulos")
    for mods in Mod_Memory.keys():
        i = i + 1
        field3 = ET.SubElement(doc3, "Memoria-" + str(mods))
        percentage = porc((Mod_Memory[mods]), memory)
        ptext =( str(Mod_Memory[mods]) + ' ' + str(percentage))
        field3.text = ptext

    doc4 = ET.SubElement(doc, "Memoria-Tipo-Datos-y-Modulos")
    for mods in module.keys():
        for types in module[mods].keys():
            i = i + 1
            field4 = ET.SubElement(doc4, "Memoria-" + str(mods) + "-" + str(types))
            percentage = porc((module[mods][types]), memory)
            ptext = ( str(module[mods][types]) + ' ' + str(percentage))
            field4.text = ptext

    tree = ET.ElementTree(root)
    tree.write("filename.xml")
    #xml = doc.toprettyxml(indent=" ")
    #fich.write(xml)

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

infile = open(sys.argv[1], 'r')

memory = 0

i=0

module = {}
modmemory = {}
typesmemory = {}
expresion = r'(\.\w{3,15}\s{0,10}0x\w{5,20}\s{3,10}0x\w{2,5} .{0,100})'
for line in infile:
    patron = re.search(expresion, line)
    if patron:
        find = re.findall(expresion, line)
        patron=line.split("/")
        cad=patron[0]
        cad=cad.split()
        types=cad[0]

        if cad[0][0:1] == '.':#uso este if para quitarme las líneas que no debo de coger
           print cad
           mod = patron[-1]#obtengo el módulo de cada línea
           mod = mod.split(".")
           mod = mod[0]
           size=cad[2]#obtengo el tamaño de los datos
           print "size " + str(size)
           try:#excepcion por si hay más de un espacio antes de size
               size = HexadecimalToDecimal(size)#paso el tamaño a decimal

           except ValueError:
               size=cad[2]
               size = HexadecimalToDecimal(size)#paso el tamaño a decimal
           memory = memory + int(size)#sumo la memoria total

    #Esto me sirve para ver que va cogiendo bien la lineas
        if types[0:1] == '.':#uso esto para quitarme las líneas que no debo de coger
            i = i + 1
            print 'Datos de la línea número ' + str(i) + '\n'
            print 'Tipo de datos: ' + types
            print 'Tamaño de datos: ' + str(size) + ' bytes'
            print 'Módulo: ' + mod + '\n'

            AddDicc(types)#Meto los valores en el diccionario

#creo los diccionarios con los modulos y los tipos para poder sacar los datos bien al representar
Mod_Memory = ModMemory()
Types_Memory = TypesMemory()
#Creo arrays para meter los dados en label
label_array = []
label2 = [] #Utilizo un array vacío para que no me pinte los datos al lado de cada trozo de tarta
data_array = []
otherpercentage = 0
#saco del diccionario de types los porcentajes y nombres para la representacion
for types in Types_Memory.keys():
    typememory = Types_Memory[types]
    percentagetype = porc((typememory),memory)
    percentagetype = round(percentagetype,2)
    if percentagetype <= 1:#Utilizo esta condición para los datos con menos de un 1%
        otherpercentage = percentagetype + otherpercentage
    else:
        label_array.append(types + ' ' + str(percentagetype) + '%')
        data_array.append(str(percentagetype))
        label2.append('')

label2.append('')#Uso label2 para meterlo en label a la hora de hacer la gráfica si hay muchos datos para que no se amontone la info en las gráficas
data_array.append(str(otherpercentage))
label_array.append('others ' + str(otherpercentage) + '%')


#Uno los datos y las etiquetas para la representación de datos
data_types = data_array
label = label_array
explode = []
for i in range(len(data_array)):
    explode.append(0)


explode = explode
#represento los datos
plt.title("Porcentajes de los tipos de datos")
plt.pie(data_types, labels = label, explode = explode)  # Dibuja un gráfico de quesitos
plt.legend(label)
plt.show()

#Creo arrays para meter los datos en label
label_array = []
label2 = []
mod_array = []
otherpercentage = 0
#Saco los modulos y sus porcentajes para la representacion de datos
for mods in Mod_Memory.keys():

    modmemory = Mod_Memory[mods]
    percentagemod = porc((modmemory),memory)
    percentagemod = round(percentagemod,2)
    if percentagemod < 1: #Usamos esta condición para los módulos menos a 1%
        otherpercentage = percentagemod + otherpercentage
    else:
        label_array.append(mods + ' ' + str(percentagemod) + '%')
        mod_array.append(str(percentagemod))
        label2.append('')

label2.append('')
label_array.append('others ' + str(otherpercentage) + '%')
mod_array.append(str(otherpercentage))

#Uno los datos y las etiquetas para la representación de datos
mod_types = mod_array
label = label_array
explode = []
for i in range(len(mod_array)):
    explode.append(0)

explode = explode

#represento los datos
plt.title("Porcentajes de los tipos de modulos")
plt.pie(mod_types, labels = label, explode = explode)  # Dibuja un gráfico de quesitos
plt.legend(label)
plt.show()

label_array = []
label2 = []
perc_array = []
otherpercentage = 0

for mods in module.keys():
    for types in module[mods].keys():
        percentage = porc((module[mods][types]), memory)
        percentage = round(percentage,2)
        if percentage < 1: #Usamos esta condición para los módulos menos a 1%
            otherpercentage = percentage + otherpercentage
        else:
            label_array.append(mods + ' (' + types + ') '  + str(percentage) + '%')
            perc_array.append(str(percentage))
            label2.append('')

label2.append('')
label_array.append('others ' + str(otherpercentage) + '%')
perc_array.append(str(otherpercentage))

#Uno los datos y las etiquetas para la representación de datos
data_types = perc_array
label = label_array
explode = []
for i in range(len(perc_array)):
    explode.append(0)
explode = explode
#represento los datos
plt.title("Porcentaje por tipo de datos y modulo")
plt.pie(data_types, labels = label, explode = explode)  # Dibuja un gráfico de quesitos
plt.legend(label)
plt.show()#muestro las tres gráficas

XML()#genero el xml
