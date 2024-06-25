import os
os.system("cls")

def principal():
    autos = []

    while True:
        print("\nAuto Seguro - Registro de Vehículos")
        print("--------------------------------------------------------")
        print("1. Grabar (registro de vehículo)")
        print("2. Buscar")
        print("3. Imprimir certificados")
        print("4. Salir")

        opcion = input("Elija su opción: ")
        if opcion not in ("1", "2", "3", "4"):
            print("Elección inválida. Favor de ingresar una opción entre 1 y 4.")
            continue
    
        if opcion == "1":
            registrar_vehiculo(autos)
        elif opcion == "2":
            buscar_vehiculo(autos)
        elif opcion == "3":
            imprimir_certificados(autos)
        elif opcion == "4":
            print("Saliendo del programa, ¡hasta pronto!")
            break
                    
def registrar_vehiculo(autos):
    tipo_vehiculo = input("Ingrese tipo de vehículo (automóvil, camión, camioneta, moto): ")     
    placa_patente = input("Ingrese placa patente (ingrese 4 letras seguido de 2 números): ")
    marca = input("Ingrese la marca del vehículo (de 2 a 15 caracteres): ")
    precio = float(input("Ingrese valor del vehículo (valor mayor a $5.000.000): "))
        
    if not validar_patente(placa_patente):
        print("Formato de placa patente inválido.")
        return
    if not 2 <= len(marca) <= 15:
        print("Largo de marca inválido.")
        return 
    if precio <= 5000000:
        print("Valor inválido, ingrese igual o sobre $5.000.000.")
        return
    
    rut = input("Ingrese RUT: ")
    nombre = input("Ingrese nombre: ")
    num_multas = int(input("Ingrese número de multas (0, 1, 2): "))
    multas = []

    for i in range(num_multas):
        multa_cantidad = float(input(f"Ingrese cantidad de la multa {i+1}: "))    
        multa_fecha = input(f"Ingrese fecha de la multa {i+1} (DD-MM-AAAA): ") 
        multas.append((multa_cantidad, multa_fecha))
    
    fecha_registro = input("Ingrese fecha de registro del vehículo (DD-MM-AAAA): ")    

    auto = {
        "tipo": tipo_vehiculo,
        "patente": placa_patente,
        "marca": marca,
        "precio": precio,
        "multas": multas,
        "fecha de registro": fecha_registro,
        "rut": rut,
        "dueño": nombre
    }

    autos.append(auto)       
    print("Vehículo registrado exitosamente.")

def validar_patente(placa_patente):
    if len(placa_patente) != 6:
        return False
    for i in range(4):
        if not placa_patente[i].isalpha() or placa_patente[i] in "MNH":
            return False
    for i in range(4, 6):        
        if not placa_patente[i].isdigit():
            return False
    return True

def buscar_vehiculo(autos):
    placa_patente = input("Ingrese placa patente para buscar: ")    
    for auto in autos:
        if auto["patente"] == placa_patente:
            mostrar_vehiculo(auto)
            return
    print("Vehículo no encontrado.")

def mostrar_vehiculo(auto):
    print("\nDetalles del Vehículo:")
    print("-------------------------------------")
    print(f"Tipo: {auto['tipo']}")
    print(f"Patente: {auto['patente']}")
    print(f"Marca: {auto['marca']}")
    print(f"Precio: {auto['precio']}")
    print(f"RUT del dueño: {auto['rut']}")
    print(f"Nombre del dueño: {auto['dueño']}")
    print(f"Fecha de registro: {auto['fecha de registro']}")
    print("Multas:")
    for multa in auto["multas"]:
        print(f"  Cantidad: {multa[0]}, Fecha: {multa[1]}")

def imprimir_certificados(autos):
    # Funcionalidad para imprimir certificados, por definir según requerimientos
    print("Funcionalidad de impresión de certificados aún no implementada.")

if __name__ == "__main__":
    principal()
    
        




























