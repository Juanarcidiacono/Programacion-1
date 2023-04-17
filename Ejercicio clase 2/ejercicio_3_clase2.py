"""Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) 
    mostrar un mensaje indicando si el número tiene uno o dos dígitos.
 (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)
"""

def main():
    cantidad_digitos(5)

def cantidad_digitos(num):
    if (num >= 10):
        print("Tiene 2 digitos")
    else:
        print("Tiene 1 digito")


if __name__ == "__main__":
    main()