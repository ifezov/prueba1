import os

def principal():
    autos= []

    while True:
        print("\nAuto seguro registro de vehiculos")
        print("--------------------------------------------------------")
        print("1.-Grabar(registro de vehiculo)")
        print("2.-Buscar ")
        print("3.-imprimir certificados ")
        print("4.-Salir ")

        opcion=input("elija su opcion :")
        if opcion not in ("1","2","3","4"):
            print("eleccion invalida favor de ingresar una opcion entre 1 y 4")
            continue
    
        if   opcion == "1":
             registrar_vehiculo(autos)
        elif opcion == "2":    
            buscar_vehiculo(autos)
        elif opcion =="3":
            mostrar_vehiculo(autos) 
        elif opcion =="4":
            print("saliendo del programa ,hasta pronto":)
                    
    
def registrar_vehiculo(autos):
    tipo_vehiculo = input("ingrese tipo vehiculo: (automovil , camion ,camioneta ,moto):")     
    placa_patente = int(input("ingrese placa patente (ingrese 4 letras seguido de 2 numeros)"))  
    marca         = input("ingrese la marca del vehiculo (de 2 a 15 caracteres):")
    precio        = float(input("ingrese valor de vehiculo(valor mayor $ 5.000.000 )"))
        
        
    if not validar_patente(placa_patente):
       print("formato de placa patente invalida")
       return
    if not 2 <= len(marca) <=15:
       print("largo de marca invalido")
       return 
    if precio <= 5000000:
       print("valor invalido ,ingrese igual o sobre $5.000.000")
       
    rut = int(input("ingrese rut:"))
    nombre =input("ingrese nombre :")
    num_multas = int(input("ingrese numero de multas (0,1,2):"))  
    multas=[]

    for i in range(num_multas):
        multa_cantidad = float(input(f"ingrese cantidad de multas por multa{i+1}:"))    
        multa_fecha    = input(f"ingrese fecha de la multa por multa {i+1}(DD,MM,AAAA):") 
        multas.append((multa_cantidad,multa_fecha))
    
    fecha_registro = input("ingrese fecha registro de vehiculo (DD-MM-AAAA):")    

    autos = {
            "tipo"   : tipo_vehiculo,
            "patente": placa_patente,
            "marca"  : marca,
            "precio" : precio,
            "multas" : multas,
            "fecha de registro":fecha_registro,
            "rut":rut,
            "dueño":nombre
            }   

    autos.append(autos)       
    print("vehiculo registrado exitosamente:")  
def validar_patente(placa_patente):
    if len(placa_patente) !=6:
        return False
    for i in range(4):
        if not placa_patente[i].isalpha() or placa_patente[i] in "MNH":
            return False
    for i in range (4,6):        
        if not placa_patente[i].isdigit():
            return False
    return True
def buscar_vehiculo(autos):
    placa_patente =input("ingrese placa patente para buscar")    
    for auto in autos:
        if auto["placa_patente"]== placa_patente:
            mostrar_vehiculo(autos)
            return
    print("vehiculo no encontrado")
def mostrar_vehiculo(autos):
    print("\n detalles vehiculo:")
    print("-------------------------------------")
    print(f" Tipo:{autos["tipo"]}:")
    print(f" Patente :{autos["patente"]}:")
    print(f"Marca::"{autos["marca"]})
    
        




























