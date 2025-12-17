def solicitar_uso_cpu():
    valor = float(input("uso de cpu "))
    return valor

def evaluar_cpu():
    conteo_alertas = 0
    total_registros = 0
    lectura = solicitar_uso_cpu()

    while lectura >= 0:
        total_registros = total_registros + 1

        if lectura > 90:
            print("alerta uso critico")
            conteo_alertas = conteo_alertas + 1

        lectura = solicitar_uso_cpu()

    return conteo_alertas, total_registros

def mostrar_reporte(conteo_alertas, total_registros):
    print("total de mediciones", total_registros)
    print("alertas criticas", conteo_alertas)

# PROGRAMA PRINCIPAL
alertas, registros = evaluar_cpu()
mostrar_reporte(alertas, registros)
