def pedir_venta():
    monto = float(input("monto de venta del vendedor: "))
    return monto

def evaluar_ventas(monto):
    objetivo = 5000
    alcanzados = 0
    total_vendedores = 0
    venta_actual = pedir_venta()

    while venta_actual > 0:
        total_vendedores = total_vendedores + 1
        if venta_actual >= objetivo:
            alcanzados = alcanzados + 1
            print("meta alcanzada, FELICITACIONES")
        venta_actual = pedir_venta()

    return alcanzados, total_vendedores

def mostrar_resumen(alcanzados, total_vendedores):
    print("vendedores con meta cumplida:", alcanzados)
    print("total de vendedores procesados:", total_vendedores)

# ******** PROGRAMA PRINCIPAL ********

venta_inicial = pedir_venta()
cumplidos, total = evaluar_ventas(venta_inicial)
mostrar_resumen(cumplidos, total)
