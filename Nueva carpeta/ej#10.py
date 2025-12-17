# ===== zona funciones =====
def solicitar_horas():
    h = int(input("Horas extra trabajadas: "))
    return h

def calcular_bonos():
    acumulado = 0
    empleados = 0
    horas = solicitar_horas()

    while horas >= 0:
        if horas > 5:
            pago = horas * 15
            acumulado = acumulado + pago
            empleados = empleados + 1
        else:
            if horas > 0:
                pago = horas * 10
                acumulado = acumulado + pago
                empleados = empleados + 1

        horas = solicitar_horas()

    return acumulado, empleados

def mostrar_resultado(acumulado, empleados):
    print("Bonificación total:", acumulado)
    print("Empleados con bonificación:", empleados)


# ===== PROGRAMA PRINCIPAL =====
h = solicitar_horas()
total_bonos, cantidad_emp = calcular_bonos()
mostrar_resultado(total_bonos, cantidad_emp)
