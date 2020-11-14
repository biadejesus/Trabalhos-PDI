import numpy as np
import cv2 as cv

def openImg(filename):
    imagem = cv.imread(filename, 0)
    if imagem is None:
        print('Imagem inválida')
        return None
    else:
        print('Imagem carregada')
        return imagem


imagem = openImg('kakashi.jpg')
# aux =  imagem.reshape(2,2)
altura, largura = imagem.shape[0], imagem.shape[1]
taxa = 8
taxa2 = 8
print("Fazendo box filter....")
boxfilter = np.vstack([np.c_[imagem[:altura, :largura ].reshape( altura//taxa, taxa, largura//taxa2, taxa2).mean(axis=(1, 3)), imagem[:altura, largura:].reshape(altura//taxa, taxa, -1).mean(axis=1)], np.c_[imagem[altura:, :largura ].reshape(-1, largura//taxa2, taxa2).mean(axis=2), imagem[altura:, largura:]]])

downsampling= imagem[::taxa,::taxa2]
zoombox = (np.repeat((np.repeat(boxfilter,taxa,axis=0)),taxa2,axis=1))
zoomdown = (np.repeat((np.repeat(downsampling,taxa,axis=0)),taxa2,axis=1))

print(imagem)
print("Gerando imagens....")
cv.imwrite('boxfilter.png', boxfilter)
cv.imwrite('img.png', imagem)
cv.imwrite('downsampling.png', downsampling)
cv.imwrite('zommboxfilter.png', zoombox)
cv.imwrite('zommdown.png', zoomdown)
