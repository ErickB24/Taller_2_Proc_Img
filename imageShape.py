"""#-----------------------------TALLER 2: imageShape-------------------------------------------------------------------
                              Erick Steven Badillo Vargas
                                Ingenieria Electronica
                           Procesamiento de imagenes y vision
                                    Julian Quiroga
                                         2020
#----------------------------------------------------------------------------------------------------------------------#"""

# Imports
import numpy as np
import cv2

import random

class imageShape:

    def __init__(self):
        print ("Inserte el ancho")
        self.width= int(input())            # Ancho de la imagen
        print ("inserte el alto")           # Alto de la imagen
        self.height = int(input())          # Alto de la imagen
        self.fig=random.randrange(0,4,1)    # seleccion de poligono aleatorio distribuido uniformemente

        self.color = (180, 190, 0)          # COLOR CYAN
        self.shape = np.zeros((self.height, self.width, 3), np.uint8)   #imagen negra

    def generateShape(self):

       if self.fig == 0:                # T R I A N G L E
           #GEOMETRIA PARA HALLAR COORDENADAS
           min_t= min(self.height,self.width)               # valor minimo
           lado_t = min_t/2                                 # valor del lado especificado
           altura_t = (((lado_t)**2)-(lado_t/2)**2)**(.5)   # ALTURA, h = raiz(hipotenusa^2-cateto^2)
           r_t=(altura_t)/((3)**(.5))                       # Radio del circulo para hallar coordenadas r = h / raiz(3)

           # COORDENADAS
           self.c_t= (round(self.width/2),round((self.height/2)+r_t))                           # coordenada superior
           self.a_t =(round((self.width/2)-(lado_t/2)),round((self.height/2)-(altura_t-r_t)))   # coordenada izquierda
           self.b_t =(round((self.width/2)+(lado_t/2)),round((self.height/2)-(altura_t-r_t)))   # coordenada derecha

           #DIBUJAR TRIANGULO
           self.triangle_cnt = np.array([self.a_t, self.b_t, self.c_t])
           self.shape=cv2.drawContours(self.shape, [self.triangle_cnt], 0, self.color, -1)      # Triangulo



       if self.fig == 1:                # S Q U A R E 45°

           # GEOMETRIA PARA HALLAR COORDENADAS
           min_s = min(self.height, self.width) #el minimo valor de los dos
           lado_s = min_s / 2                   # lado
           r_s = lado_s/((2)**(.5))             #distancia del centro a los vertices (pitagoras)

           # COORDENADAS
           self.a_s = (round((self.width/2)+r_s),round(self.height/2))      # esquina superior
           self.b_s = (round(self.width/2),round((self.height/2)+r_s))      # esquina derecha
           self.c_s = (round((self.width/2)-r_s),round(self.height/2))      # esquina izquierda
           self.d_s = (round(self.width/2),round((self.height/2)-r_s))      # esquina inferior

           # DIBUJAR SQARE
           self.square_cnt = np.array([self.a_s, self.b_s, self.c_s,self.d_s])
           self.shape = cv2.drawContours(self.shape, [self.square_cnt], 0, self.color, -1)  # SQUARE     # cuadrado



       if self.fig == 2:             # R E C T A N G L E

           # COORDENADAS DE INICIO Y FIN
           self.ini=(round(self.width/4),round(self.height/4))
           self.fin=(round((self.width*3/4)+2),round(self.height*3/4)) #rectangular
           # Se le añaden dos pixeles para hacer la imagen rectangular cuando Width y Height son iguales

           self.shape = cv2.rectangle(self.shape,self.ini,self.fin,self.color,-1)


       if self.fig == 3:                # C I R C L E

           # PARAMETROS DEL CIRCULO
           self.centro = (round(self.width / 2), round(self.height / 2))  # centro, ancho/2 y alto/2
           min_s = min(self.height, self.width)                           # minimo de ancho y largo
           r_c = round(min_s/4)                                           # radio del circulo especificado

           #DIBUJANDO EL CIRCULO
           self.shape =cv2.circle(self.shape,self.centro,r_c ,self.color , -1)

       return self.shape

    def showShape(self):
        cv2.imshow('Shape', self.shape)     # MOSTRAR IMAGEN 5s
        cv2.waitKey(5000)

    def getShape(self):


        if self.fig == 0:               # si es triangulo
            self.polig='Triangle'

        if self.fig == 1:               # si es cuadrado
            self.polig='Square'

        if self.fig == 2:               # si es rectangulo
            self.polig='Rectangle'

        if self.fig == 3:               # si es circulo
            self.polig='Circle'

        return self.shape,self.polig    # retorna la imagen y el string del poligono

    def whatShape(self,imagen):             #deteccion de poligonos

        cont, jera = cv2.findContours(imagen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # hallar contorno de la imagen
        epsilon = 0.01 * cv2.arcLength(cont[0], True)                 # hallando epsilon. True (img cerrada)
        approx = cv2.approxPolyDP(cont[0], epsilon, True)             # poligono aproxximado
        self.lados = len(approx)                                      # numero de vertices
        x,y,w,h= cv2.boundingRect(approx)                             # separando x, y, ancho y alto


        if self.lados == 3:                                           # si el poligono aproximado tiene 3 vertices
            self.poligono = 'Triangle'                                # Triangulo

        if self.lados == 4:                                           # si el poligono aproximado tiene 4 vertices
            aspect_ratio=float(w)/float(h)                            # relacion de aspecto si es 1 es cuadrado
            if aspect_ratio == 1:                                     # Es cuadrado o rectangulo
                self.poligono = 'Square'                              # cuadrado
            else :
                self.poligono = 'Rectangle'                           # rectangulo

        if self.lados > 10:                                           # si el poligono aproximado tiene mas de 10 vertices
            self.poligono = 'Circle'                                  # circulo
            
        return self.poligono                                          # retorna la figura


