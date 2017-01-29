# -*- coding: utf-8 -*-
#Python 2.7

import os
import os.path as path
import time
import sys
from BannerST import Banner

os.system("cls")

Autor = "By: LawlietJH"
Version = "v1.0.0"

#EMCrk - Banner Random
banner = str(Banner()+"{:>71}".format(Version)+"\n\n{:^80}".format("[-] Ordena tus Diccionaros Alfabeticamente para Ataques por Fuerza Bruta [-]"))

ModoDeUso = """\n   Modo De Uso:\n\n\t\t SorText.py [-d][Nombre.ext] | [-v] | [-a] | [-h]
\n\n\t -a, --all \t\t Muestra todos los datos juntos y continua\n\t\t\t\t con la ejecución normal del Script.
\n\t -d, Nombre.ext \t\t Se coloca el nombre del diccionario a\n\t\t\t\t  utilizar añadiendo su extensión.
\n\t -h, --help \t\t Muestra el Modo De Uso.
\n\t -v, --version \t\t Muestra la versión y autor del Script.
"""


def Ordenar(X):

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
    

def main():
	
	os.system("cls")
	
	if len(sys.argv) == 2:
		
		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			print(ModoDeUso)
			exit(0)
			
		elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
			print("\n\n{:^80}\n{:^80}\n{:^80}".format("SorText",Autor[4:],Version[1:]))
			exit(0)
			
		elif sys.argv[1] == "-a" or sys.argv[1] == "--all":
			print("\n\n{:^80}\n{:^80}\n{:^80}".format("SorText",Autor[4:],Version[1:]))			
			NombA=raw_input("\n\n [+] Nombre De Archivo A Ordenar [Con Extension]: ")
			Ordenar(NombA)
		
		elif sys.argv[1] == "-d":
			print("\n\n\t Añade el nombre del diccionario.\n\n\t\t ejemplo: SorText.py -d Nomb_Dic.zion")
			
		elif not sys.argv[1] == "-a" and not sys.argv[1] == "--all"\
		and not sys.argv[1] == "-h" and not sys.argv[1] == "--help"\
		and not sys.argv[1] == "-v" and not sys.argv[1] == "--version":
			print(ModoDeUso)
			
	elif len(sys.argv) == 3:
			
		if sys.argv[1] == "-d":
			NombA = sys.argv[2]
			print(banner)
			Ordenar(NombA)
		else:
			print(ModoDeUso)
			
	
	elif len(sys.argv) > 3:
		print(ModoDeUso)
		
	else:
		print(banner)
		NombA=raw_input("\n\n [+] Nombre De Archivo A Ordenar [Con Extension]: ")
		Ordenar(NombA)

main()
