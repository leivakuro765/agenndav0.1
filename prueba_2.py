import wikipedia 

# idioma, muy importannte
idioma = wikipedia.set_lang("es") # es--> Espa;ol
#para saber cuando esta en ejecucion....

print ("ejecutando, no molestar...")
''''
#busqueda
#busca cada paralabra relacionada
busqueda = wikipedia.search(['Manga','Anime','Boku no hero', ])

print (busqueda)

for i in range(len(busqueda)):
     print (i, end=".\n\n")
     
     # busca cada palabra en un resumen de la busqueda
     resumen = wikipedia.summary(busqueda[i])
     # imprime cada busquedad de la lista.
     print (resumen)

'''

sugerecia= wikipedia.suggest("Ma")

print (sugerecia)


