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
