def solicitar_operacion():
    operacion = input("Ingrese D para deposito, R para retiro o FIN para terminar: ")
    return operacion

def ingresar_valor():
    valor = float(input("Ingrese el valor: "))
    return valor

def ejecutar_movimientos():
    dinero = 1000
    movimientos = 0
    operacion = solicitar_operacion()

    while operacion != "FIN":
        if operacion == "D":
            valor = ingresar_valor()
            dinero = dinero + valor
            movimientos = movimientos + 1
        else:
            if operacion == "R":
                valor = ingresar_valor()
                if dinero - valor >= 0:
                    dinero = dinero - valor
                    movimientos = movimientos + 1
                else:
                    print("retiro no permitido, fondos insuficientes")
            else:
                print("operación inválida")

        operacion = solicitar_operacion()

    return dinero, movimientos

def mostrar_datos_finales(dinero, movimientos):
    print("saldo final:", dinero)
    print("movimientos realizados:", movimientos)

# ******** PROGRAMA PRINCIPAL ********
saldo_final, total_movimientos = ejecutar_movimientos()
mostrar_datos_finales(saldo_final, total_movimientos)
