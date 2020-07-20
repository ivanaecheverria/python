print("Ivanita")

#print ("Numeros primos: 2,3,5,7,11,13,17,19,23,29")

for num in range (2,30):
    primo = True
    for i in range(2,num):  
        if(num%i==0):
            primo = False
    if primo:
        print (num)     

#Hacer un programa que pida por pantalla ingresar dos numeros, y luego imprima la suma de ambos

print ("ingresar dos numeritos por favorrrr:  ")
num1 = int(input("Ingrese el primer numero"))
num2 = int(input("ingrese el segundo numero"))
total = num1 + num2
print (f"Total = {total} ")


#Hacer un programa que pida un nombre, una edad y una comida. 
# Finalmente que imprima por pantalla algo como “Juan tiene 15 años y le gusta el chocolate