# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:29:15 2022

@author: Dylan Montoya 
"""
import os
import pickle 
from cassis import *
from etiquetadoBIO2 import etiquetado
import numpy as np


for file in os.listdir():  # se usa para obtener la lista de todos los archivos y directorios en el directorio especificado
    with open('TypeSystem.xml', 'rb') as f:
        typesystem = load_typesystem(f)
        
    if file.endswith(".xmi"): 
       with open(file, 'rb') as f:
           name=os.path.basename(file) #nombre base del archivo actual
           cas= load_cas_from_xmi(f, typesystem=typesystem)
           
           #Hc=etiquetado(name,cas,'webanno.custom.Anonimizacin')
          # Hc,Di, oA=etiquetado(name,cas,'webanno.custom.NERClnico')
           data_hc, longitud, ListAnotaciones = etiquetado(name,cas,'webanno.custom.NERClnico') 
           
#find max, mean, and std length of sentences
sen_std = np.std(longitud)                         
sen_mean = np.mean(longitud)                       
sen_max = np.amax(longitud)                        
sen_precentile = np.percentile(longitud,99)        
print(sen_std, sen_mean, sen_max, sen_precentile)


with open("data_hc.pickle", 'wb') as archivo:
    pickle.dump(data_hc, archivo)

with open("data_hc.pickle", 'rb') as archivo:
    mi_variable = pickle.load(archivo)