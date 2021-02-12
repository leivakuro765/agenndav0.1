import time
import os 
def agenda(): # este programa sirve para agregar, modificar, eliminar y consutar contactos.
	contactos={}
	salir=True
	while (salir):
		
		print (' \'Bienvenido a este programa\'\n ')
		print ('''1.) Ver contacto\n2.) Agregar contacto\n3.) Buscar contacto\n4.) Modificar contacto\n5.) Eliminar contacto\n6.) Salir''')

		opcion =input('Digite el numero de la opcione que desea ver: ')	
		os.system('clear') 
		if opcion == '1': # <--------  Muestra los contacto
			for contacto in contactos:
				for numero in contactos:
					print ('contacto / numero')
					print (numero, contactos[contacto])
		
			time.sleep(4)
			os.system('clear')

		elif opcion == '2':# <------ Registra de contacto
			nombre= input('Nombre: ')
			if nombre in contactos:
				print ('contacto ya exitente')
				time.sleep(3)
				os.system('clear')
				continue
			try:
				numero= input('Numero: ')
				if numero >   9999999999:
					print ('El numero demaciado corto')
					time.sleep(3)
					os.system('clear')
					continue
				elif nuemro < 10000000000:
					print ('El numero demaciado largo.\n Deben de ser 10 digitos')
					time.sleep(2)
					os.system('clear')
					continue

			except:
				print('Valor no valido')
				time.sleep(3)
				os.system('clear')
			contactos[(nombre)] = numero
			print('Contacto agregado')
			print(contactos)
			time.sleep(3)
			os.system('clear')

		elif opcion == '3': # <----- Buscar Contacto
			buscar=input('Contacto a Buscar: ')
			print (contactos[buscar])
			time.sleep(3)
			os.system('clear')
			if buscar not in contactos:
				print('El contacto no existe., agreguelo desde el menu')

		elif opcion == '4': # <------- Modificar contacto
			contacto = input('contacto a modificar')
			if contacto not in contactos:
				print ('Contacto no exitente')
				continue
			try:
				nuevo=int(input('Nuevo Numero: '))
				contactos[contacto]=nuevo
				if numero>9999999999:
					print('El numero es de maciado largo')
					time.sleep(3)
					os.system('clear')
					continue
				elif numero<1000000000:
					print('El numero es muy corto\nDeben de ser 10 digitos')
				print('Contacto modificado con exito')
				time.sleep(3)
				os.system('clear')
				continue

			except:
				print ('Valor no valido')
				time.sleep(3)
				os.system('clear')
				continue

		elif opcion == '5':
			eliminar=input('Contacto a eliminar: ')
			if eliminar not in contactos:
				print ("El contacto no existe")
				continue
			del(contactos[eliminar])
			print('Contacto',eliminar,'eliminado con exito')
			time.sleep(4)
			os.system('clear')
			continue
		elif opcion == '6':  #
			os.system('exit')
		else:
			print ('opcione no valida,\n Elija un opcion del 1 al 6')
			time.sleep(3)
			os.system('clear')
agenda()
