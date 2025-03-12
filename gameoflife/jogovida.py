import numpy as np
import matplotlib.pyplot as fig 
from matplotlib import animation, cm 
import random 

fig.close('all')

r = 80 #linhas
c = 80 #colunas

matriz = np.zeros((r+1, c+1))
novo_matriz = np.zeros((r+1, c+1))


matriz[4,1] = 1
matriz[4,2] = 1
matriz[6,2] = 1
matriz[5,3] = 1
matriz[5,4] = 1
matriz[4,5] = 1
matriz[6,5] = 1
matriz[6,1] = 1
matriz[5,6] = 1

for ger in range(50):
    for i in range(1,r):
        for j in range(1,c):
            vizinho = 0
            if matriz[i-1, j-1]==1:
                vizinho += 1
            if matriz[i, j-1]==1:
                vizinho += 1
            if matriz[i+1, j-1]==1:
                vizinho += 1
            if matriz[i+1, j]==1:
                vizinho += 1
            if matriz[i+1, j+1]==1:
                vizinho += 1
            if matriz[i-1, j+1]==1:
                vizinho += 1
            if matriz[i, j+1]==1:
                vizinho += 1
            if matriz[i-1, j]==1:
                vizinho += 1
            
            if matriz[i,j] == 1:
                if (vizinho == 2) or (vizinho == 3):
                    novo_matriz[i,j] = 1
                else:
                    novo_matriz[i,j] = 0
            else:
                if vizinho == 3:
                    novo_matriz[i,j] = 1
                else:
                    novo_matriz[i,j] = 0
    matriz = novo_matriz
    novo_matriz = np.zeros((r+1, c+1))
    
    
    fig.title("GERAÇÃO %d" % ger, fontsize = 20)
    fig.xticks([])
    fig.yticks([])
    im = fig.imshow(matriz, interpolation = "nearest", cmap = "Greys", animated = True)
    mgr = fig.get_current_fig_manager()
    mgr.window.setGeometry = (20,20,1000,1000)
    fig.pause(0.5)