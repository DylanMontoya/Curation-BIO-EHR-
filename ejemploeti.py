# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:29:15 2022

@author: Dylan Montoya
"""
import os 
from cassis import *
from etiquetadoBIO import etiquetado

for file in os.listdir():  # se usa para obtener la lista de todos los archivos y directorios en el directorio especificado
    with open('TypeSystem.xml', 'rb') as f:
        typesystem = load_typesystem(f)
        
    if file.endswith(".xmi"):
       with open(file, 'rb') as f:
           name=os.path.basename(file) #nombre base del archivo actual
           cas= load_cas_from_xmi(f, typesystem=typesystem)
           
           #Hc=etiquetado(name,cas,'webanno.custom.Anonimizacin')
           Hc,Di,oA, arrlego, spa = etiquetado(name,cas,'webanno.custom.NERClnico') 
