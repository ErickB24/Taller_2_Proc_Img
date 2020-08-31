"""#-----------------------------TALLER 2: imageShape-------------------------------------------------------------------
                              Erick Steven Badillo Vargas
                                Ingenieria Electronica
                           Procesamiento de imagenes y vision
                                    Julian Quiroga
                                         2020
#----------------------------------------------------------------------------------------------------------------------#"""


# IMPORTAR
from imageShape import imageShape                   # importar el archivo
import numpy as np
import cv2
import os
import random

IS=imageShape()                                     # Libreria
IS.generateShape()                                  # generar imagen
IS.showShape()                                      # mostrar imagen 5s
image,name_real = IS.getShape()                     # obtener la imagen y el nombre

print ("imagen dibujada:")
print(name_real)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#imagen en grises para la mascara
ret,mask = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)   # mascara
name_detect=IS.whatShape(mask)                      # deteccion de poligonos

print ("imagen detectada:")
print(name_detect)                                  # poligono detectado

if name_real == name_detect:

    print('Deteccion correcta')


