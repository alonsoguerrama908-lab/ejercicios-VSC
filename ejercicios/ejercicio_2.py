def ejercicio_2():
    password = "lunes"
    intentos = 0
    palabra = ""

    while palabra != password:
        palabra = input("Contraseña:")
        intentos += 1
        if intentos == 5:
            print("Excediste las oportunidades")
            break