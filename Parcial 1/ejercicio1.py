def main():
    sum_even_numbers()

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
    # Imprimir los numeros pares hasta el numero ingresado inclusive
    even_numbers = []
    for i in range(number+1):
        even_numbers.append(i) if i % 2 == 0 else None
    even_numbers.pop(0)
    print(even_numbers)
    
    return even_numbers
        
    
def sum_even_numbers(sum =4 0):
    list_numbers = calculate_even_numbers_given_a_number()

    for i in list_numbers:
        print(i)
        sum += i 
    
    print(f"La suma de los numeros pares es {sum}")

if __name__ == "__main__":
    main()