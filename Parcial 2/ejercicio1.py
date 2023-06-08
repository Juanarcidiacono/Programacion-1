def main():
   # data = data_input()
   # nombres = data[0]
   # sueldos = data[1]
    nombres = ['PEDRO', 'SOFIA', 'JOSEFINA', 'JOSE', 'ESTEBAN','JUAN']
    sueldos = [1,         10,        9,        10,       5,       6]
    print(f"Sueldo promedio {calcular_promedio_sueldos(sueldos)}")
    print(f"Ordenar por sueldo max {ordenar_por_sueldo(sueldos,nombres)}")
    print(f"Empleados sueldo max {obtener_empleado_sueldo_max(sueldos,nombres)}")
    
def calcular_promedio_sueldos(sueldos):
    # Caluclo promedio usando los metodos sum y len. Redondeo a una cifra decimal
    return round(sum(sueldos)/len(sueldos),1)

def obtener_empleado_sueldo_max(sueldos, nombres,
                                hay_personas_con_el_mismo_sueldo=True,nombres_sueldo_max=[]):
    
    NOMBRES = nombres
    max_sueldo = max(sueldos)
    # Puede haber personas con el mismo sueldo. Contemplo el caso 
    # y retorno el/los nombres de las personas con el sueldo mas alto
    while hay_personas_con_el_mismo_sueldo:
        
        if max_sueldo in sueldos:
            nombre_sueldo_max = NOMBRES[sueldos.index(max_sueldo)]
            sueldos.remove(max_sueldo)
            
            nombres_sueldo_max.append(nombre_sueldo_max)
            nombres.remove(nombre_sueldo_max)
            
        else:
            hay_personas_con_el_mismo_sueldo = False
    
    return nombres_sueldo_max
 
def ordenar_por_sueldo(sueldos,nombres,sueldos_ord=[], nombres_ord=[]):
    
    cant_sueldos = len(sueldos)
    
    # Comparo los valores de la listas y me fijo cual es mayor
    for i in range(cant_sueldos):
        for j in range(0, cant_sueldos-i-1):
            if sueldos[j] < sueldos[j+1]:
                sueldos[j], sueldos[j+1] = sueldos[j+1], sueldos[j]
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]

    nombres_ord = nombres
    sueldos_ord = sueldos

    return sueldos_ord, nombres_ord

def data_input(flag=True,nombres=[],sueldos=[],continuar=None):
    # Ingreso los nombres mientras no se ingrese la letra ´n´
    while flag:
        if continuar != 'n':
            nombre = input('Ingrese nombre >> ')
            sueldo = int(input(f'Ingrese el sueldo de {nombre}: ' ))
            
            nombres.append(nombre)
            sueldos.append(sueldo)
            
            continuar = input("Desea continuar? S/N ").lower()
        else:
            flag = False
            
    else:
        print("Saliendo...")
    
    return nombres, sueldos
 
    
if __name__ == "__main__":
    main()