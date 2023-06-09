# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 14:48:43 2022

@author: Dylan Montoya
"""

from cassis import *
import numpy as np

Samples={}

def etiquetado(name, cas, layer):
    # name es el nombre base del documento que se esta leyendo, se usa libreria os
    # cas es el documento que se esta procesando actualmente en la carperta y que termina con .xmi
    # layer toma la capa en que se hicieron las anotaciones, en inception donde se crea la capa se puede ver el nombre
    # por ejemplo acá también esta 'webanno.custom.NERClnico'

    ListAnotaciones=[]
    
    for data in cas.select(layer): #tomar las entidades anotadas en la capa especificada
        lista = [[data.begin, data.end], data.Value, data.get_covered_text()]
        ListAnotaciones.append(lista)

    TokensI = "de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Token"
    tokens=[]
    spans=[] #almacena los spans de inicio de cada palabra para hacer el etiquetado BIO
    for s in cas.select(TokensI):
        tokens.append(s.get_covered_text())
        spans.append(s.begin)
        
    etiquetasbio= ['O']*len(spans)
    
    if len(ListAnotaciones)==0:
        arreglo=np.transpose(np.vstack((tokens,etiquetasbio)))
        Samples[name]=arreglo

    else:
        for anotacion in ListAnotaciones:
           
           rangoS= anotacion[0] 
           for item, i in enumerate(spans):
               
              if rangoS[0]== i: #si el span de inicio de lo anotado en igual al span(i) significa que es B-entidad
                  etiquetasbio[item]=('B-' + str(anotacion[1]))
              
              elif rangoS[0] < i < rangoS[1]: #si el span(i) se encuentra en el rango de los spans(inicio y final) de la entidad es I-entidad 
                  etiquetasbio[item]=('I-' + str(anotacion[1]))
              
           arreglo=np.transpose(np.vstack((tokens,etiquetasbio)))
           #hice transpuesta porque creo que así es mas fácil de analizar los datos
        
        Samples[name]=arreglo #Diccionario con key: nombre del documento Value: tokens y su etiquetado
        
    return Samples, ListAnotaciones,tokens, arreglo, spans


