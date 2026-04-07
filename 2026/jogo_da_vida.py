import numpy as np
import matplotlib.pyplot as fig
from matplotlib import animation, _cm
import random

fig.close("all")



#spaceship
# a[4, 1] = 1
# a[4, 2] = 1
# a[6, 2] = 1
# a[5, 3] = 1
# a[5, 4] = 1
# a[4, 5] = 1
# a[6, 1] = 1
# a[6, 5] = 1
# a[5, 6] = 1



def update(data):
    global a
    global count

    novo_a = np.zeros((n + 1, m + 1))

    for ger in range(20):
        for i in range(1, n):
            for j in range(1, m):
                vizinho = 0

                if a[i - 1, j - 1] == 1:
                    vizinho += 1
                if a[i, j - 1] == 1:
                    vizinho += 1
                if a[i + 1, j - 1] == 1:
                    vizinho += 1
                if a[i - 1, j + 1] == 1:
                    vizinho += 1
                if a[i, j + 1] == 1:
                    vizinho += 1
                if a[i + 1, j + 1] == 1:
                    vizinho += 1
                if a[i + 1, j] == 1:
                    vizinho += 1
                if a[i - 1, j] == 1:
                    vizinho += 1

                if a[i, j] == 1:
                    if (vizinho == 2) or (vizinho == 3):
                        novo_a[i, j] = 1
                    else:
                        novo_a[i, j] = 0
                else:
                    if vizinho == 3:
                        novo_a[i, j] = 1
                    else:
                        novo_a[i, j] = 0

        a = novo_a
        im.set_data(a)
        s = 0
        for i in range(n):
            for j in range(m):
                s += a[i,j]
        count += 1
        vivo[count] = s

        fig.figure(2)

        fig.title("GERAÇÃO %d" % ger, fontsize=20)
        fig.plot(vivo[:count],'-k')
        fig.xlabel('GERAÇÃO', fontsize=12)
        fig.ylabel('POPULAÇÃO', fontsize=20)
        im = fig.imshow(a, interpolation="nearest", cmap="Greys", animated=True)
        mgr = fig.get_current_fig_manager()
        mgr.window.setGeometry(800, 20, 1000, 500)
        fig.pause(0.1)
        return im

#glider
a[3,1] = 1
a[1,2] = 1
a[3,2] = 1
a[2,3] = 1
a[3,3] = 1

n,m = 80
vivo = np.zeros((300))
a = np.zeros((n+1,m+1))