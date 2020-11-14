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
f1 = 8
f2 = 8
saida = np.vstack([np.c_[imagem[:altura, :largura ].reshape( altura//f1, f1, largura//f2, f2).mean(axis=(1, 3)), imagem[:altura, largura:].reshape(altura//f1, f1, -1).mean(axis=1)], np.c_[imagem[altura:, :largura ].reshape(-1, largura//f2, f2).mean(axis=2), imagem[altura:, largura:]]])
cv.imwrite('saida.png', saida)
cv.imwrite('img.png', imagem)
