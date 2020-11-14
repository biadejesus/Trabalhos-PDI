import numpy as np
import cv2 as cv

faces = {1:((1,0,1),(1,0,0),(1,1,0),(1,1,1)), 2:((1,1,1),(1,1,0),(0,1,0),(0,1,1)), 3:((1,0,1),(1,1,1),(0,1,1),(0,0,1)) , 4:((0,0,1),(0,1,1),(0,1,0),(0,0,0)) , 5:((1,0,1),(0,0,1),(0,0,0),(1,0,0)), 6:((1,0,0),(1,1,0),(0,1,0),(0,0,0))}

inicio = np.zeros((256, 256, 3), dtype=np.uint8) #pra gerra imagem do tipo certo
print(inicio)
cv.imwrite('teste.png', inicio)

for i in range(256):
    inicio[i,:,0] = i
    inicio[:,-i,2] = i
    

cv.imwrite('teste2.png', inicio)