def solicitar_cantidad():
    cantidad = int(input("Ingrese la cantidad de unidades del lote: "))
    return cantidad

def solicitar_condicion():
    condicion = input("Condición (D defectuosa / O correcta): ")
    return condicion

def evaluar_lotes():
    falladas = 0
    correctas = 0
    continuar = input("Escriba stop para finalizar o Enter para continuar: ")

    while continuar != "stop":
        cantidad = solicitar_cantidad()
        contador = 0

        while contador < cantidad:
            condicion = solicitar_condicion()

            if condicion == "D":
                falladas = falladas + 1
            else:
                if condicion == "O":
                    correctas = correctas + 1
                else:
                    print("Condición no válida")
                    contador = contador - 1

            contador = contador + 1

        continuar = input("Escriba stop para finalizar o Enter para continuar: ")

    return falladas, correctas

def mostrar_resultados(falladas, correctas):
    total = falladas + correctas

    if total > 0:
        porcentaje = (falladas * 100) / total
    else:
        porcentaje = 0

    print("Unidades defectuosas:", falladas)
    print("Unidades correctas:", correctas)
    print("Porcentaje defectuosas:", porcentaje)

# ******** PROGRAMA PRINCIPAL ********
defectos, buenas = evaluar_lotes()
mostrar_resultados(defectos, buenas)
