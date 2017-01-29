# -*- coding: utf-8 -*-
#Python 2.7

import os
import os.path as path
import time
from BannerST import Banner

os.system("cls")

Autor = "By: LawlietJH"
Version = "v1.0.0"

#EMCrk - Banner Random
banner = str(Banner()+"{:>71}".format(Version)+"\n\n{:^80}".format("[-] Ordena tus Diccionaros Alfabeticamente para Ataques por Fuerza Bruta [-]"))

print (banner)

X=raw_input("\n\n [+] Nombre De Archivo A Ordenar [Con Extension]: ")

if not path.exists(X):
    print("\n\n\t\t [!] No Existe El Archivo: "+X)
    os.system('Timeout /nobreak 03 > Nul')
    
else:
    
    FechaI = time.strftime("\n\n\t [!] Iniciado: %d/%m/%Y %H:%M:%S")
    print(FechaI)

    print("\n\n\t [*] Ordenando Palabras...")

    lista_palabras=sorted(file(X), key=str.lower)
    file(X[:-4]+"-Ordenado.txt","w").writelines(lista_palabras)

    print("\n\n    [+] Ordenado Y Guardado En El Archivo: "+X[:-4]+"-Ordenado.txt")

    FechaF = time.strftime("\n\n\t [!] Finalizado: %d/%m/%Y %H:%M:%S")
    print(FechaF)

    os.system("Timeout /nobreak 03 > Nul")
