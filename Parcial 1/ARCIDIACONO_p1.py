def main():
    sum_and_print_even_numbers()

def input_number():
    number = int(input("Ingrese un numero >> "))
    return number

def calculate_even_numbers_given_a_number():
    # Solicitar al usuario un valor de tipo entero y guardarlo en una variable.
    number = input_number()
    # Calculo los numeros pares y los coloco en una lista.
    even_numbers = [i for i in range(number + 1) if i % 2 == 0]
    # Elimino el 0 por ser numero neutro.
    even_numbers.pop(0)

    return even_numbers

# Imprimo cada uno de los numeros. Creo un contador que contiene 
# la suma acumulada de cada uno de los elementos de la lista de numeros pares.
def sum_and_print_even_numbers(sum=0):
    list_even_numbers = calculate_even_numbers_given_a_number()

    for number in list_even_numbers:
        print(number)
        sum +=  number

    print(f"La suma de los numeros pares es {sum}")


if __name__ == "__main__":
    main()