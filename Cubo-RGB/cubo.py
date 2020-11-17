import numpy as np
import cv2 as cv
import sys 
import getopt 

argv = sys.argv[1:] 
  
try: 
    opts, args = getopt.getopt(argv, "f:v:") 
    
except: 
    print("Error") 

for opt, arg in opts: 
    if opt in ['-f']: 
        face = arg 
    elif opt in ['-v']: 
        valor = int(arg)

if valor < 0 or valor > 255:
    print("Insira um valor válido!") 
    sys.exit()    

if face == "1":
    cima = np.linspace([255,0,255], [255, 255, 255], 255)
    baixo = np.linspace([255,0,0], [255, 255, 0], 255)
    cubo = np.linspace(cima, baixo, 255).astype(np.uint8)
    cubo[:,:,0] = 255 - valor
elif face == "2":
    cima = np.linspace([0,0,255], [255, 0, 255], 255)
    baixo = np.linspace([0,0,0], [255, 0, 0], 255)
    cubo = np.linspace(cima, baixo, 255).astype(np.uint8)
    cubo[:,:,1] = 255 - valor
elif face == "3":
    cima = np.linspace([255,255,255], [0, 255, 255], 255)
    baixo = np.linspace([255,255,0], [0, 255, 0], 255)
    cubo = np.linspace(cima, baixo, 255).astype(np.uint8)
    cubo[:,:,1] = 255 - valor
elif face == "4":
    cima = np.linspace([0,255,255], [0, 0, 255], 255)
    baixo = np.linspace([0,255,0], [0, 0, 0], 255)
    cubo = np.linspace(cima, baixo, 255).astype(np.uint8)
    cubo[:,:,0] = 255 - valor
elif face == "5":
    cima = np.linspace([0,0,255], [0, 255, 255], 255)
    baixo = np.linspace([255,0,255], [255, 255, 255], 255)
    cubo = np.linspace(cima, baixo, 255).astype(np.uint8)
    cubo[:,:,0] = 255 - valor
elif face == "6":
    cima = np.linspace([0,0,0], [0, 255, 0], 255)
    baixo = np.linspace([255,0,0], [255, 255, 0], 255)
    cubo = np.linspace(cima, baixo, 255).astype(np.uint8)
    cubo[:,:,2] = 255 - valor
else:
    print("Insira uma face válida!")
    sys.exit()

cv.imwrite('resultado.png', cubo)