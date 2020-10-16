tutor = "Codi"
print(tutor)

# listas
listas = ["xxx", "kdkd", "jdjd", "dsadas", "icjid"]

#para ver un elemento, se pone el indice
lista = listas[0]
print(lista)

#sublista, aqui me mostraria desde el indice 1, hasta el 2, no coge el utilmo
sub= listas[1:3]

#para ordenar una lista de forma ascendente
listas.sort()
print(listas)

##descendente
listas.sort(reverse=True)
print(listas)

#numero menor o mayor
menor= min(listas)
print(menor)

mayor= max(listas)
print(mayor)

#longitud
longitud = len(listas)
print(longitud)

#para ver si un numero esta incluido
resultado="dfsdfs" in listas
print(resultado)

#contador, cuantas veces esta un dato en esa lista
contador = listas.count("ddf")
print(contador)

