def pedir_clave():
    clave = input("ingrese su clave de identificación: ")
    return clave

def validar_clave(clave_ingresada, clave_autorizada):
    if clave_ingresada == clave_autorizada:
        return True
    else:
        return False

def gestionar_accesos():
    clave_autorizada = "1403"
    accesos_ok = 0
    accesos_no = 0
    while True:
        clave = pedir_clave()
        if clave == "salir":
            break
        if validar_clave(clave, clave_autorizada):
            print("acceso autorizado")
            accesos_ok = accesos_ok + 1
        else:
            print("acceso rechazado")
            accesos_no = accesos_no + 1
    return accesos_ok, accesos_no

def mostrar_resumen(accesos_ok, accesos_no):
    print("accesos permitidos:", accesos_ok)
    print("accesos denegados:", accesos_no)

# ************ PROGRAMA PRINCIPAL ************

clave = pedir_clave()
permitidos, rechazados = gestionar_accesos()
mostrar_resumen(permitidos, rechazados)
