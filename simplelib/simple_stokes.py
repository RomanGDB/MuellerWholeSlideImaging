import sys
import numpy as np
import gzip
import os

sys.path.append('../')
from camaralib.take_mueller_stokes import take_mueller_stokes
from camaralib.guardar_stokes import guardar_stokes

# Ruta carpeta en dónde guardar
IMG_SAVE_PATH = 'stokes/'  

if not os.path.exists(IMG_SAVE_PATH): 
    os.makedirs(IMG_SAVE_PATH)

# Exposicion
exposure_time = 5000

# Numero de promedios
N = 1

#Decimador 
decimador = 1

#Angulos de polarizacion de entrada
thetas_list = [0,30,60,90,120,150]  

def main():

    #Nombre
    name = 'Sin_inv.npy.gz'

    #Toma vectores de Stokes
    S_in_stat = take_mueller_stokes(exposure_time, N, thetas_list)

    #Guarda numpy stokes comprimido
    print("Guardando array...")
    f = gzip.GzipFile(IMG_SAVE_PATH + name, 'wb')
    np.save(f, np.linalg.pinv(S_in_stat))

    return True

if __name__ == '__main__':

    if main():
        sys.exit(0)
    else:
        sys.exit(1)
