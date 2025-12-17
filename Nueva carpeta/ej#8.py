def solicitar_edad():
    return int(input("Edad del participante (0 para terminar): "))

def analizar_edades():
    objetivo = 0
    total_edades = 0
    cantidad_personas = 0

    edad = solicitar_edad()

    while edad != 0:
        cantidad_personas += 1
        total_edades += edad

        if 25 <= edad <= 45:
            objetivo += 1
            print("Registrado dentro del grupo objetivo")

        edad = solicitar_edad()

    return objetivo, total_edades, cantidad_personas

def mostrar_resultados(objetivo, total_edades, cantidad_personas):
    promedio = total_edades / cantidad_personas if cantidad_personas > 0 else 0

    print("Grupo objetivo:", objetivo)
    print("Promedio de edad:", promedio)
