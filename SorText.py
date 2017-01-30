# -*- coding: utf-8 -*-
# Python 3

import os
import os.path as path
import time
import sys
from BannerST import Banner

os.system("cls")

Autor = "By: LawlietJH"
Version = "v1.0.2"

#~ EMCrk - Banner Random
banner = str(Banner()+"{:>71}".format(Version)+"\n\n{:^80}".format("[-] Ordena tus Diccionaros Alfabéticamente para Ataques por Fuerza Bruta [-]"))

ModoDeUso = """\n   Modo De Uso:\n\n\t\t SorText.py [-d Diccionario.ext] | [-v] | [-a] | [-h]
\n\n\t -a, --all \t\t Muestra todos los datos juntos y continua\n\t\t\t\t con la ejecución normal del Script.
\n\t -d, --diccionario \t Se coloca el nombre del diccionario a\n\t\t\t\t utilizar añadiendo su extensión.
\n\t -h, --help \t\t Muestra el Modo De Uso.
\n\t -v, --version \t\t Muestra la versión y autor del Script.
"""

BST = r"""
                         __   __   __  ___  ___     ___ 
                        /__` /  \ |__)  |  |__  \_/  |  
                        .__/ \__/ |  \  |  |___ / \  |  
"""
#~ Fuente: JS Stick Letters, Página: http://patorjk.com/software/taag

BA = r"""
                            ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
                            ║  ├─┤││││  │├┤  │ ║╠═╣
                            ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩
"""
#~ Fuente: Calvin S, Página: http://patorjk.com/software/taag




def Ordenar(X):
				#~ Comprobamos Si Existe El Archivo
	if not path.exists(X):
		
		print("\n\n\t\t [!] No Existe El Archivo: "+X)
		os.system('Timeout /nobreak 03 > Nul')
	
	else:

		FechaI = time.strftime("\n\n\t [!] Iniciado: %d/%m/%Y %H:%M:%S")
		print(FechaI)

		print("\n\n\t [*] Ordenando Palabras...")
		
		#~ En Python 3.
		
		Archivo = open(X,"r")	#~ Abre el archivo.
		ListA = []		#~ Se crea una lista.
		
		for linea in Archivo:
			ListA.append(linea)	#~ Se añade cada palabra del archivo a la lista .
			
		ListA = sorted(ListA)	#~ Se ordena la Lista.

		Archivo2 = open(X[:-4]+"-Ord.zion","w")		#~ Se Crea un nuevo archivo.
		
		for dato in ListA:
			Archivo2.write(dato)	#~ Se Guardan las palabras de la lista ordenada al nuevo archivo.
		
		Archivo.close()
		Archivo2.close()

		#~ En Python 2.
		#~ lista_palabras=sorted(file(X), key=str.lower)
		#~ file(X[:-4]+"-Ordenado.txt","w").writelines(lista_palabras)

		print("\n\n    [+] Ordenado Y Guardado En El Archivo: "+X[:-4]+"-Ord.zion")

		FechaF = time.strftime("\n\n\t [!] Finalizado: %d/%m/%Y %H:%M:%S")
		print(FechaF)

		os.system("Timeout /nobreak 03 > Nul")	#~ Pausa de 3 segundos, en este tiempo, la ventana no respondera a ninguna acción.


def main():
	
	os.system("cls")
				    #~ Argumentos que puede leer el Script.
	if len(sys.argv) == 2:
		
		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			print(ModoDeUso)
			exit(0)
			
		elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
			print("\n\n{:^80}\n{:^80}\n{:^80}".format(BST,BA,Version[1:]))	#~ Mostrara El Banner SorText, el Banner de Autor
			exit(0)								#~ y la Versión del Script
			
		elif sys.argv[1] == "-a" or sys.argv[1] == "--all":
			print("\n\n{:^80}\n{:^80}\n{:^80}".format(BST,BA,Version[1:]))
			NombA=input("\n\n [+] Nombre De Archivo A Ordenar [Con Extensión]: ")
			Ordenar(NombA)
		
		elif sys.argv[1] == "-d" or sys.argv[1] == "--diccionario":
			print("\n\n\t Añade el nombre del diccionario.\n\n\t\t ejemplo: SorText.py -d Nomb_Dic.zion")
			
		elif not sys.argv[1] == "-a" and not sys.argv[1] == "--all"\
		and not sys.argv[1] == "-h" and not sys.argv[1] == "--help"\
		and not sys.argv[1] == "-v" and not sys.argv[1] == "--version":
			print(ModoDeUso)	#~ Si se agregó un argumento y no es ninguno de estos, Mostrará el Modo De Uso.
			
	elif len(sys.argv) == 3:
			
		if sys.argv[1] == "-d" or sys.argv[1] == "--diccionario":
			NombA = sys.argv[2]
			print(banner)
			Ordenar(NombA)
		else:
			print(ModoDeUso)
			
	
	elif len(sys.argv) > 3:
		print(ModoDeUso)
		
	else:
		print(banner)
		NombA=input("\n\n [+] Nombre De Archivo A Ordenar [Con Extensión]: ")
		Ordenar(NombA)



#~ Aquí Se ejecuta El Programa
main()
