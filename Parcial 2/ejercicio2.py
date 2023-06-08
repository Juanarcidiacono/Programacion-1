def main():
    #palabras = ingresar_palabras()
    letra = input("Ingrese la letra que quiere buscar: ").lower()
    palabras = ['juan','sebastian','ines','pablo','roberto','tomas','agustin']
    print(encontrar_palabras_con_letra(palabras,letra))
    print(ordenar_palabras_longitud(palabras))
    
def encontrar_palabras_con_letra(palabras,letra,match_palabras=[]):
    for palabra in palabras:
        if letra in palabra:
            match_palabras.append(palabra)
            
    return match_palabras

def ordenar_palabras_longitud(palabras):
    for i in range(len(palabras)):
        for j in range(i + 1, len(palabras)):
            if len(palabras[i]) > len(palabras[j]):
                palabras[i], palabras[j] = palabras[j], palabras[i]
                      
    return palabras
# Otra forma:
# return sorted(palabras, key=len)
          
def ingresar_palabras(nombres=[], flag=True, continuar=None):
    while flag:
        if continuar != 'n':
            nombre = input('Ingrese nombre >> ')
            nombres.append(nombre)
            continuar = input("Desea continuar? S/N ").lower()
            
        else:
            flag = False
            
    else:
        print("Saliendo...")
    
    return nombres.lower()

if __name__ == "__main__":
    main()