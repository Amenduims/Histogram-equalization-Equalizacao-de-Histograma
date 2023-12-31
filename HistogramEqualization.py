# -*- coding: utf-8 -*-
"""Equalização.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YszkImAQOEYvuh7aDD3DEA2boNLLt9c8
"""

# Commented out IPython magic to ensure Python compatibility.
import common #some useful opencv functions
import numpy as np # matrix manipulations

#the following are to do with this interactive notebook code
# %matplotlib inline
from matplotlib import pyplot as plt # this lets you draw inline pictures in the notebooks

# Loading and showing the image
import cv2
import matplotlib.pyplot as plt

img_original = cv2.imread('flower.jpg')
img = cv2.imread('flower.jpg')
plt.imshow(img)

#histogram equalization code
#Código de equalização de histograma

qtd_tons = []
novos_tons = []

altura, largura, canais = img.shape

for i in range(256):
  qtd_tons.append(0)
  novos_tons.append(0)


for i in range (altura):
  for j in range(largura):
    b,g,r = img[i,j]
    qtd_tons[b] += 1


qtd_ideal = int((altura*largura)/len(qtd_tons))

somatorio = 0

for i in range(256):
  somatorio += qtd_tons[i]
  novos_tons[i] = (somatorio/qtd_ideal) - 1


for i in range (altura):
  for j in range(largura):
    b,g,r = img[i,j]
    img[i,j] = novos_tons[b]

plt.imshow(img)

#Showing the histogram before the equalization

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

matriz_imagem = np.array(img_original)
frequencia_pixels, valores_pixels = np.histogram(matriz_imagem, bins=256)

plt.bar(valores_pixels[:-1], frequencia_pixels, width=1)
plt.title('Imagem original')
plt.xlabel('Intensidade do pixel')
plt.ylabel('Frequência')
plt.show()
plt.imshow(img_original)

#Showing the histogram after the equalization

matriz_imagem = np.array(img)
frequencia_pixels, valores_pixels = np.histogram(matriz_imagem, bins=256)

plt.bar(valores_pixels[:-1], frequencia_pixels, width=1)
plt.title('Imagem final')
plt.xlabel('Intensidade do pixel')
plt.ylabel('Frequência')
plt.show()
plt.imshow(img)
