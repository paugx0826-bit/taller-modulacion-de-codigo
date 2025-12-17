def pedir_precio_producto():
    valor_producto = float(input("precio del producto: "))
    return valor_producto

def pedir_cantidad_producto():
    numero_unidades = int(input("cantidad: "))
    return numero_unidades

def procesar_compra(valor_producto, numero_unidades):
    total_parcial = 0
    continuar = input("agregar producto (si/no): ")

    while continuar != "no":
        valor_producto = pedir_precio_producto()
        numero_unidades = pedir_cantidad_producto()
        total_parcial = total_parcial + (valor_producto * numero_unidades)
        continuar = input("agregar otro producto (si/no): ")

    return total_parcial

def obtener_descuento(total_parcial):
    if total_parcial > 1000:
        rebaja = total_parcial * 0.10
    else:
        if total_parcial > 500:
            rebaja = total_parcial * 0.05
        else:
            rebaja = 0

    monto_final = total_parcial - rebaja
    return monto_final, rebaja

def mostrar_total(monto_final, rebaja):
    print("descuento aplicado:", rebaja)
    print("total a pagar:", monto_final)

# ******** PROGRAMA PRINCIPAL ********

precio_unitario = pedir_precio_producto()
cantidad_ingresada = pedir_cantidad_producto()
subtotal = procesar_compra(precio_unitario, cantidad_ingresada)
total_pagar, descuento = obtener_descuento(subtotal)
mostrar_total(total_pagar, descuento)
