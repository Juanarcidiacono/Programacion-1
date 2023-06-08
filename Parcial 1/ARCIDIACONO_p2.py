# ARCIDIACONO JUAN IGNACIO DNI:38.684.730

def main():
    n1_divisble_by_n2()

# Solicitar al usuario dos numeros enteros.
# Retorna una lista con los numeros ingreados.
def input_numbers():

    n1 = int(input("Ingrese el numero >> "))
    n2 = int(input("Es divisible por >> "))

    return [n1,n2]

# Mientras el numero n2 NO sea igual a cero, 
# entonces que se fije si n1 y n2 son divisbles.
# Si n2 es igual a cero, el programa finaliza e imprime un mensaje.
def n1_divisble_by_n2(n2_is_not_equal_to_zero=True):

    while n2_is_not_equal_to_zero:

        numbers = input_numbers()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n2 != 0:
            if n1 % n2 == 0:
                print("Si")
            else:
                print("No")
        else:
            n2_is_not_equal_to_zero = False

    else:
        print("No es posible dividir por cero")


if __name__ == "__main__":
    main()