cant_operaciones = int(input("Ingrese la cantidad de operaciones a realizar: "))

contador = 0
acumulador = 0

while True:
    try:

        for i in range(cant_operaciones):
            deposito = float(input("Ingrese monto de dinero a depostar: "))
            contador += 1
            acumulador = acumulador + deposito
            
        total = acumulador
        print(f"El usuario ha depositado : {acumulador} en {contador} operaciones.")
        break
        
    except(ValueError):
        print("Solo numeros enteros")
        