import numpy as np
import cv2 as cv

import sys 
import getopt 

argv = sys.argv[1:] 
  
try: 
    opts, args = getopt.getopt(argv, "i:t:") 
    
except: 
    print("Error") 

for opt, arg in opts: 
    if opt in ['-i']: 
        img = arg 
    elif opt in ['-t']: 
        taxa = int(arg)

def openImg(filename):
    imagem = cv.imread(filename, 0)
    if imagem is None:
        print('Imagem inválida')
        sys.exit()
        return None
    else:
        print('Imagem carregada')
        return imagem


imagem = openImg(img)
altura, largura = imagem.shape[0], imagem.shape[1]
boxfilter = np.vstack([np.c_[imagem[:altura, :largura ].reshape( altura//taxa, taxa, largura//taxa, taxa).mean(axis=(1, 3)), imagem[:altura, largura:].reshape(altura//taxa, taxa, -1).mean(axis=1)], np.c_[imagem[altura:, :largura ].reshape(-1, largura//taxa, taxa).mean(axis=2), imagem[altura:, largura:]]])

downsampling= imagem[::taxa,::taxa]
zoombox = (np.repeat((np.repeat(boxfilter,taxa,axis=0)),taxa,axis=1))
zoomdown = (np.repeat((np.repeat(downsampling,taxa,axis=0)),taxa,axis=1))

cv.imwrite('boxfilter.png', boxfilter)
cv.imwrite('downsampling.png', downsampling)
cv.imwrite('zommboxfilter.png', zoombox)
cv.imwrite('zommdownsampling.png', zoomdown)
