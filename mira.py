import sys
import math
import cv2
import numpy as np
import random

### Colores puros, falta buscar clase que lo haga de cv2 ##
##RED = cv.Scalar(0,0,255)
##GREEN = cv.Scalar(0,255,0)
##BLUE = cv.Scalar(255,0,0)

KEY_ESC = 1048603

im_height = 500
im_width = 500

imgs = []

def load_iconos():
    for i in range(7):
        imgs.append(cv2.imread('icono%d.png' %i))

def random_img():
    cv2.imshow('main', random.choice(imgs[:-1]))

## Dibuja numbers circulos aleatorios a una distancia dada del centro
##def draw_circles(img, numbers, radius, distanceToCenter):
##    colorCoding =w[0][0].size
##    width = w[0].size/colorCoding
##    height = w.size/w[0].size
##    for n in range(numbers):
##        
##        random.randrange(0,)


cv2.namedWindow('main', flags=cv2.WINDOW_AUTOSIZE)

## Para cargar en imgs los iconos de la carpeta raiz y mostrarlos
##load_iconos()
##cv2.imshow('main', imgs[-1])

## TODO poner texto en pantalla
##cv.PutText(imgs[-1], 'Press any key', (20,10), cv.InitFont(), RED)
##
##
##while 1:
##    if cv2.waitKey():
##        break
##
##while 1:
##    random_img()
##    key = cv2.waitKey(0)
##    if key == KEY_ESC:
##        sys.exit()
##while 1:
##    if cv2.waitKey():
##        break
##sys.exit()
##=======================



## Para generar imagen en blanco
white_image = np.zeros((im_height, im_width,3), np.uint8)
white_image[:,:] = (255,255,255)

##

# Pintar punto central
cv2.rectangle(white_image, (im_height/2-1, im_width/2-1), (im_height/2+1, im_width/2+1), (0,0,0), -1)
##


# Pintar circunferencias
cv2.circle(white_image, (50, 50), 30, (0,0,0))
##

cv2.imshow('main', white_image)

cv2.waitKey()
