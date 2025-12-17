def solicitar_producto():
    producto = int(input("qué producto lleva: "))
    return producto

def solicitar_cantidad():
    cantidad_pedidos = int(input("cuántos pedidos son: "))
    return cantidad_pedidos

def procesar_calificaciones(cantidad_pedidos):
    suma = 0
    contador = 0
    for i in range(cantidad_pedidos):
        print("calificación del pedido:")
        nota = int(input("Del 1 al 5: "))
        if nota > 5:
            nota = 5
        if nota < 1:
            nota = 1
        if nota == 5:
            print("excelente")
        suma = suma + nota
        contador = contador + 1
    return suma, contador

def calcular_promedio(suma, contador):
    if contador > 0:
        promedio = suma / contador
    else:
        promedio = 0
    return promedio

def mostrar_promedio(promedio):
    print("El promedio es:", promedio)

# ************ PROGRAMA PRINCIPAL ************

articulo = solicitar_producto()
cantidad = solicitar_cantidad()
total, conteo = procesar_calificaciones(cantidad)
promedio_final = calcular_promedio(total, conteo)
mostrar_promedio(promedio_final)
