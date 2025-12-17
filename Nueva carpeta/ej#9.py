def solicitar_vendido():
    cantidad = int(input("Cantidad vendida hoy: "))
    return cantidad

def controlar_inventario():
    existencias = 50
    limite = 10

    vendido = solicitar_vendido()

    while vendido >= 0:
        existencias = existencias - vendido

        if existencias <= limite:
            print("Aviso de Reposición Urgente")
            break

        vendido = solicitar_vendido()

    return existencias

def mostrar_stock(existencias):
    print("Stock final:", existencias)


# ---- zona código principal ----
v = solicitar_vendido()
stock_final = controlar_inventario()
resultado = mostrar_stock(stock_final)
