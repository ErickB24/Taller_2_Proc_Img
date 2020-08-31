"""#-----------------------------TALLER 1: Colorclass-------------------------------------------------------------------
                              Erick Steven Badillo Vargas
                                Ingenieria Electronica
                           Procesamiento de imagenes y vision
                                    Julian Quiroga
                                         2020                              
#----------------------------------------------------------------------------------------------------------------------#"""

#importar
import numpy as np
import cv2
import os

#clase colorImage-------------------------------------------------------------------------------------------------------
class colorImage:
    # Constructor:
    def __init__ (self):
        print("Indique la direccion de la Imagen:")     # Imprimir en pantalla
        self.dir= input()                               # Entrada de direccion del usuario

    # Cargar imagen de la direccion::
    def iniciar (self):
        self.path = self.dir
        self.path_file = os.path.join(self.path)        # Abrir archivo
        self.image = cv2.imread(self.path_file)         # Guardar la imagen en self
        return self.image                               # Retornar la imagen

    # Dimensiones de la imagen:
    def displayProperties(self):
        print('Las dimensiones de la imagen(H,W,C) son: ',self.image.shape)     # Mostrar las dimensiones de la imagen

    # Escala de grises:
    def makeGray(self):
        self.Img_Gray= cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)             # Transformacion de BGR a escala de grises con Cv2
        return self.Img_Gray                                                    # Retornar la imagen en gris

    # Colorizar imagen:
    def colorizeRGB(self,color):
        if color == "red":                      # Si desea verla en rojo:
            self.rojo = np.copy(self.image)     # Copia de la imagen a modificar
            self.rojo[:, :, 1] = 0              # Capa verde en 0
            self.rojo[:, :, 0] = 0              # Capa azul en 0
            return self.rojo                    # Retornar la imagen rojiza


        if color == "blue":                     # Si desea verla en Azul:
            self.azul = np.copy(self.image)     # Copia de la imagen a modificar
            self.azul[:, :, 1] = 0              # Capa verde en 0
            self.azul[:, :, 2] = 0              # Capa rojo en 0
            return self.azul                    # Retornar la imagen Azulosa


        if color == "green":                    # Si desea verla en Verde:
            self.verde = np.copy(self.image)    # Copia de la imagen a modificar
            self.verde[:, :, 0] = 0             # Capa azul en 0
            self.verde[:, :, 2] = 0             # Capa rojo en 0
            return self.verde                   # Retornar la imagen Verdosa

    # Hue de la Imagen:
    def makeHue(self):
        self.Img_Hue = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)  # Transfomacion de BGR a HSV
        self.hue = np.copy(self.Img_Hue)                            # Copia de la imagen a modificar
        self.hue[:, :, 1] = 255                                     # Capa S en 255
        self.hue[:, :, 2] = 255                                     # Capa V en 255
        self.Img_RGBhue = cv2.cvtColor(self.hue, cv2.COLOR_HSV2BGR) # Transformacion de HSV a BGR
        return self.Img_RGBhue                                      # Retornar la imagen en tonos resaltados







