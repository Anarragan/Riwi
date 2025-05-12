import sys
n = int(input("¿Cuantas calificaciones quiere ingresa? "))
notas = []

if 2 <= n <= 10:
    print("Por favor ingrese las notas...")

    for i in range(n):
        num = int(input(f"Nota {i+1}: "))
        notas.append(num)

else:
    print("Error: el numero de notas debe estar entre 2 y 10")
    sys.exit()
#funcion para calcular promedio de notas---------------
def promedio(): 
    promedio = 0

    for i in range(len(notas)):
        promedio += notas[i]
    
    promedio = promedio / n

    print(f"El promedio de notas es de: {promedio}")

#funcion para calificaciones mayores-------------------
def mayores():
    nota = int(input("Ingrese la nota que quiere comparar: "))
    cont = 0
    for i in range(len(notas)):
        if nota < notas[i]:
            cont += 1
    
    print(f"Hay {cont} nota/notas que son mayores")

    
#funcion para verificar estado aprobado/reprobado------
def verificacion():
    nota = int(input("Ingrese la nota que quiere verificar: "))
    if 0 < nota <= 100:
        if nota >= 60:
            print("Aprobado")
        
        else:
            print("Reprobado")
    
    else:
        print("Error: la nota debe estar en el rango de 0 a 100")

def mostrar_menu():

    print("¿Que accion desea realizar?\n")
    print("1. Determinar estado aprobado/reprobado")
    print("2. Saber las calificaciones mayores")
    print("3. Calcular el promedio")
    print("4. Terminar")

def salir():
    print("Hasta pronto...")
    sys.exit()


while True:
    mostrar_menu()
    accion = int(input("Seleccione una opcion (1/2/3/4): \n"))

    if accion == 1:
        verificacion()

    elif accion == 2:  
        mayores()

    elif accion == 3:
        promedio()

    elif accion == 4:
        salir()

    else:
        print(f"{accion} no es una opcion valida")