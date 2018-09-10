

#  ---  Blibliotecas auxiliares  ---
import cv2 as cv
import os 
import numpy as np
#  ---  ---

#  --- Método para binarizar a imagem  ---
def img_binary():

    #caminho das imagens contidas na pasta
    path = [os.path.join('imgs', f) for f in os.listdir('imgs')]
    

    pictures = []# Vetor que guardara as imagens binarizadas
    ids = []# ids das imagens

    for path_img in path:# for que percorre as imagens da pasta

        img = cv.imread(path_img, 0)# Transforma a imagem em uma matriz do numpy
        img = cv.medianBlur(img, 5)# Suaviza a imagem para evitar erros

        # Binariza a imagem, adaptando os valores 
        img_bin = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv.THRESH_BINARY, 11, 2)

        pictures.append(img_bin)# Adiciona a imagem a lsita
        
    return pictures
#  ---  ---

pictures = img_binary()
#  ---  ---
for img in pictures:
    cv.imshow('img', img)
    cv.waitKey(1000)