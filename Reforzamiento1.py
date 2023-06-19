# Variables
var_1 = '¡Hi'
var_2 = 'Joseph!'

# Concatenando

mi_saludo = var_1 + " " + var_2

# mostrar
print(mi_saludo)

""" Pregunta numero 2 """
# Crear una variable

var_3 = 27

# Calculo
operacion = (var_3 * 10) - 10

# mostrar
print("El valor de mi operacion es de: {}".format(operacion))

""" Pregunta numero  3"""
#variables

var_4 = "Joseph"
var_5 = 1995

#mostrar
print("El valor de mi suma es: {}".format( var_4 + str(var_5)))

"""pregunta numero 4"""

#variable: calcular el radio de una esfera de diametro de 24 cm
"""
Formula para calcular diamentro =
V = 4/3 π r³
"""
diametro = 24
r = 24/2
calcular_volumen = 4/3 * 3.14 * r**3

print("El volumen de mi esfera es: {}".format(calcular_volumen))

"""Pregunta 5"""
sueldo = int(input("Digite el sueldo"))

if sueldo % 2 == 0:
    print("El numero {} es par".format(sueldo))
else:
    print("El numero {} es impar".format(sueldo))

    """ pregunta 6"""
var_6 = float(13.5)
var_7 = float(132.5)
var_8 = float(54.54)
var_9 = float(31.9)
var_10 = float(163.1)

media = (var_6 + var_7 + var_8 + var_9 + var_10)/5
print("La media de mis variables es; {}".format(media))

"""pregunta 7"""
#variables

var_11 = 78
var_12 = 2465
var_13 = 84234896

suma = var_11 + 3 + var_12 + 5 + var_13 + 7
print("El valor de la suma es: {}".format(suma))


"""Pregunta 9"""

var_14 = 12
operacion1 = var_14**4 - (var_14**4)*2
print(operacion1)

"""pregunta 10"""

diccionario = {'nombre':'Joseph', 'carrera' : 'administracion', 'edad': 27 ,  'año de nacimiento': 1995 }
print(diccionario)

"""pregunta 11 """

numero = 10

comprobar = (numero**5)/10

print("El resultado de mi variable es tipo: {}".format(type(comprobar)))