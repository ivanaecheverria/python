#Hacer un programa que pida un nombre, una edad y una comida.
# Finalmente que imprima por pantalla algo como “Juan tiene 15 años y le gusta el chocolate

#nombre = input("Ingrese su nombre: ")
#edad = input("Ingrese su edad: ")
#comida = input("Ingrese su comida favorita: ")

#print( nombre + " tiene " + edad + " años y le gusta " + comida)

#---------------------------------------------------------------------------------------------
#Hacer un programa que pida un numero, e indique por pantalla si el numero es o no es mayor igual a 10.

#numero = int(input ("ingrese un numero de preferencia:  "))
##if numero > 10:
#    print(numero, "es mayor a 10")

#---------------------------------------------------------------------------------------------
#Hacer un programa que pida un numero, e indique por pantalla, si es o no es múltiplo de 3. 
#Ejemplo: 12 es múltiplo de 3 (3*4) pero 14 no lo es (no es divisible por 3)

#numero = int(input("Ingrese un numero: "))

#if numero%3 == 0:
 #   print(numero, " es multiplo de 3")
#else:
 #   print(numero, " no es multiplo de 3")

#---------------------------------------------------------------------------------------------
#Hacer un programa que pida un numero, y, si el número termina en 7, imprimir “Termina en 7”. 
#Sino imprimir “No termina en 7” (ejemplo: 1234567 -> termina en 7)

#numero = int(input("Ingrese un numero: "))

#numero = numero-7

#if numero%10==0:
#    print("Numero termina en 7")
#
#else:
#    print("Numero no termina en 7")

#---------------------------------------------------------------------------------------------
#Hacer un programa que pida un nombre de usuario. 
#Si el usuario no es “Pepe”, denega el acceso. 
#Si es pepe, pide la contraseña. 
#Si la contraseña coincide con un valor específico, el programa imprime “Bienvenido Pepe”. 
#Si la contraseña es incorrecta, imprime “Acceso denegado”.

#usuario = input("Ingrese su usuario: ")

#if usuario != "Pepe":
#    print("Acceso denegado")

#elif usuario == "Pepe":
#    password = input("Ingrese su contraseña: ")
#    if password != "1234":
#        print("Acceso denegado")
#    elif password == "1234":
#        print("Bienvenido Pepe")

#Hacer un programa que reciba un numero, y haga lo siguiente
#Si el numero es mayor a 100, imprimir “Mayor a 100”
#Pero si es 666, imprimir “Numero del diablo”
#Si es menor a 10, imprimir “Tiene un solo digito”
#Pero si esta entre 10 y 100, y es par, imprimir: “Es numero par”. Si es impar, imprimir “Es numero impar”
#Finalmente, si el numero termina en 5 (e.g. 15, 25, 105) imprimir “Nivel Dios”

numero = int(input("Ingresar un numero: "))
if numero == 666:  
    print("Numero del diablo")

if numero >= 10 and numero <=100:
    if numero%2==0:
        print("Es numero par")
    elif numero%2==1:
        print ("Es numero impar")

if numero > 100: 
    print("mayor a 100")

elif numero < 10:
    print("Tiene un solo digito")

numero = numero-5
if numero%10 == 0:
    print("Nivel Dios")


