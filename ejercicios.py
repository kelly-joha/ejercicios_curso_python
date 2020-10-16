# Ejercicio 1 Area de un triángulo
# while True:
#     try:
#         b = int(input("Ingrese el valor de la Base del triángulo  "))
#         h = int(input("Ingrese el valor de la altura del triángulo "))
#         area = (b*h)/2
#         print("El área del triángulo es ", area)
#         break
#     except ValueError:
#         print("Por favor ingrese solo números")
    
# Ejercicio 2 convertir dólares en pesos

# while True:
#     try:
#         dolarInput = float(input("Ingrese la cantidad de dólares "))
#         valorDolar = 3850
#         total = dolarInput * valorDolar
#         print("En pesos colombianos se tienen ", total)
#         break
#     except ValueError:
#         print("Por favor ingrese solo números")
    

#ejercicio 3 convertir de grados centrigrados a farenheit
    # while True:
    # try:
    #     Centigrado = float(input("Ingrese el valor de grados centrigrados"))
    #     farenheit = (Centigrado * (9/5)) + 32
    #     print("en grados farenheit corresponden a", farenheit)
    #     break
    # except ValueError:
    #     print("Por favor ingrese solo números")

# ejercicio 4 cantidad de segundos que tiene un lustro

    # lustro = 5 * 365 *24 *60 *60
    # print("un lustro tiene", lustro, "segundos")

# ejercicio 5 segundos que tarda la luz del sol a marte
    
# veloLuz = 3000
# distancia = 227388762
# segundos = distancia/veloLuz
# print("tarda", segundos, "segundos")

# ejercicio 6 numero de vueltas que da una llanta en 1 km, diametro de 50cm

# import math

# pi= math.pi
# diametro = 50
# radio = diametro/2
# perimetro = 2 * pi * radio
# numVueltas = int(100000 / perimetro)
# print("la llanta da ", numVueltas, "vueltas")



#ejercicio 8 True o False si la edad ingresada es la misma

#  while True:
#     try:
#         edad1 = int(input("Ingrese la primer edad"))
#         edad2 = int(input("Ingrese la segunda edad"))
#         if edad1 == edad2:
#             print("True ")
#         else:
#             print("False ")
#         break
#     except ValueError:
#         print("Por favor ingrese solo números")


# ejercicio 9 meses transcurridos desde la fecha de nacimiento

# from  datetime import datetime
# from  datetime import timedelta

#  while True:
#     try:
#         fecha = input("Ingrese la fecha de nacimiento así: YYYY/MM/DD")
#         fecha = datetime.strptime (fecha, '%Y/%m/%d')
#         today = datetime.date.today()
#         hoy = datetime.datetime.now()
#         diferencia = hoy - fecha
#         print("Now", now)
#         break
#     except ValueError:
#          print("ingrese YYYY/MM/DD") 

# print(fecha)
# print(today)
# print(hoy)
# print(int(diferencia.days /30))



# ejercicio 10 promedio alumno

#  while True:
#     try:
#         espanol = float(input("Ingrese la nota de español"))
#         matematicas = float(input("Ingrese la nota de matematicas"))
#         economia = float(input("Ingrese la nota de economia"))
#         programacion = float(input("Ingrese la nota de programacion"))
#         ingles = float(input("Ingrese la nota de ingles"))
#         promedio = (espanol + matematicas + economia + programacion + ingles)
#         print("el promedio es: ", promedio)
#         break
#     except ValueError:
#         print("Por favor ingrese solo números")
