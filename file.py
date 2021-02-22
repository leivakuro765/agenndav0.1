import wikipedia

#consulta un busqueda en wikipedia
busqueda = wikipedia.search("Manga")
busqueda = wikipedia.search("Manga", results=3)

# sugerecia de busquedad

gerencia = wikipedia.suggest("Mang", results=10)

# Extracion de; resumen del articulo

resumen = wikipedia.summary("Manga")

#recuperar datos conpletos de wikipedia

recuperar = wikipedia.page("Manga")

#Extraer metadatos de una página

extraer = wikipedia.page("Manga").content
#Extraer url de la pagina de wikipedia

extraer = wikipedia.page("Manga").url

#Extraer las referecia de la pagina de wikipedia

ref = wikipedia.page("Manga").references

#Extraer el titulo de la pagina de wikipedia

titulo = wikipedia.page("Manga").title

#Extraer categoria de la pagina de wikipedia

categoria = wikipedia.page("Manga").categories


#Extraer links de la pagina de wikipedia

links = wikipedia.page("Manga")

# Encotrar pagina basado en cordenadas 

cordenado = wikipedia.geosearch(37.787,  -122.4)


# Ajustar idioma de busqueda 

idoma = wikipedia.set_lang("es")

#Extraer imagenes de una pagina de la pagina de wikipedia

imagen wikipedia.page("Manga").images[0]


#Extraer el HTML de la pagina de wikipedia

HTML = wikipedia.page("").html()