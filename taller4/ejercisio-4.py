mensual = float(input("Salario mensual: "))

if mensual == 0:
    print("Sin trabajadores")
else:
    while mensual != 0:
        dias = int(input("Días trabajados: "))
        bonos = float(input("Bonos: "))
        deducciones = float(input("Otras deducciones: "))
        
        salario_proporcional = mensual * dias / 30
        devengado = salario_proporcional + bonos
        neto = (devengado * 0.83) - deducciones
        
        print("Neto:", neto)
        
        mensual = float(input("Salario mensual: "))
    
    print("Sin trabajadores")