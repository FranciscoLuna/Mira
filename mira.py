import sys
import cv2
import random

### Colores puros, falta buscar clase que lo haga de cv2 ##
##RED = cv.Scalar(0,0,255)
##GREEN = cv.Scalar(0,255,0)
##BLUE = cv.Scalar(255,0,0)

KEY_ESC = 1048603

imgs = []

def load_images():
    for i in range(7):
        imgs.append(cv2.imread('%d.png' %i))

def random_img():
    cv2.imshow('main', random.choice(imgs[:-1]))

# Pintar circunferencias
#cv.Circle(imgs[-1], (10, 10), 5, BLUE)

load_images()
cv2.namedWindow('main', flags=cv2.WINDOW_NORMAL)
cv2.imshow('main', imgs[-1])
# TODO poner texto en pantalla
#cv.PutText(imgs[-1], 'Press any key', (20,10), cv.InitFont(), RED)
while 1:
    if cv2.waitKey():
        break

while 1:
    random_img()
    key = cv2.waitKey(30)
    if key == KEY_ESC:
        sys.exit()
