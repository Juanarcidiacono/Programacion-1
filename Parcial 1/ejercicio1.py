def main():
    sum_and_print_even_numbers()

def input_number():
    is_number_correct = False

    while not is_number_correct:
        try:
            number = int(input("Ingrese un numero >> "))
            is_number_correct = True if number > 0 else False
        # Excepcion numero decimal
        except ValueError as error:
            print("Numero ingresado incorrecto >> ", error)

    return number

def calculate_even_numbers_given_a_number():
    # Solicitar al usuario un valor de tipo entero y guardarlo en una variable.
    number = input_number()
    # Calculo los numeros pares y los coloco en una lista
    even_numbers = [i for i in range(number + 1) if i % 2 == 0]
    # Elimino el 0 por ser numero neutro
    even_numbers.pop(0)

    return even_numbers

def sum_and_print_even_numbers(sum=0):
    list_even_numbers = calculate_even_numbers_given_a_number()

    # Imprimo cada uno de los numeros. Creo un contador que contiene la suma acumulado de cada uno de los elementos de la lista de numeros pares.
    for number in list_even_numbers:
        print(number)
        sum +=  number

    print(f"La suma de los numeros pares es {sum}")


if __name__ == "__main__":
    main()