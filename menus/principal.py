from ejercicios.ejercicio_1 import ejercicio_1
from ejercicios.ejercicio_2 import ejercicio_2
from ejercicios.ejercicio_3 import ejercicio_3
from ejercicios.ejercicio_4 import ejercicio_4

def menu_principal():
    while True:
        print("Menú principal")
        print("1.- Ejercicio 1")
        print("2.- Ejercicio 2")
        print("3.- Ejercicio 3")
        print("4.- Ejercicio 4")
        print("5.- Salir")
        op = int(input("Elija opcion: "))
        match(op):
            case 1:
                ejercicio_1()
            case 2:
                ejercicio_2()
            case 3:
                ejercicio_3()
            case 4:
                ejercicio_4()
            case 5:
                break
            case _:
                print("Opcion no válida")
            


       