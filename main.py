"""#-----------------------------TALLER 1: Colorclass-------------------------------------------------------------------
                              Erick Steven Badillo Vargas
                                Ingenieria Electronica
                           Procesamiento de imagenes y vision
                                    Julian Quiroga
                                         2020
#----------------------------------------------------------------------------------------------------------------------#"""
# importar--------------------------------------------------------------------------------------------------------------
from colorImage import colorImage #importar del archivo
import numpy as np
import cv2
import os

# Iniciar el programa---------------------------------------------------------------------------------------------------
pro= colorImage()		        # inicializar programa
original= pro.iniciar() 	    # cargar imagen
cv2.imshow('imagen',original) 	# visualizar la imagen
cv2.waitKey(0) 			        # Esperar a que se cierre la imagen

# Dimension de la imagen:
pro.displayProperties() 	    # Mostrar tamaño


# Imagen en gris: ------------------------------------------------------------------------------------------------------
Gray=pro.makeGray()             # Con el método makeGray se puede transformar una imagen en tonos de grises
cv2.imshow('imagen2',Gray)	    # Mostrar imagen en gris
cv2.waitKey(0)	    		    # Mostrar imagen hasta que se cierre

#Imagen colorizada:-----------------------------------------------------------------------------------------------------
"""
#Estas líneas le permiten al usuario ingresar el color en el que quiere ver la imagen seleccionada anteriormente. 
print("escriba el color en el que desea ver la imagen(blue,red,green)")
colorcito= input()#si quiere que el usuario ingrese el color comente la línea de abajo y descomente esta y la anterior.
"""
#red=Rojizo------blue=azulado-------green=verdoso
colorcito='red'			                # Variable que permite mostrar el color de la imagen deseado
Imgcolorized=pro.colorizeRGB(colorcito) #Con el método colorizeRGB se puede generar una imagen en el tono deseado (Rojo, Azul y Verde)
cv2.imshow('imagen3',Imgcolorized)	    # Mostrar imagen en el color deseado
cv2.waitKey(0)				            # Mostrar imagen hasta que se cierre

# Mostrar HUE:----------------------------------------------------------------------------------------------------------
colorhue=pro.makeHue()              # Con el método makeHue se puede observar la imagen en tonos resaltados
cv2.imshow('imagen3',colorhue) 	    # Mostrar la imagen con tonos resaltados
cv2.waitKey(0)		        		# Mostrar la imagen hasta que se cierre


# ejemplo de direccion = C:/Users/Erick/Desktop/OCTAVO SEMESTRE/PROC DE IMAGENES/TALLER_1/lena.png"
