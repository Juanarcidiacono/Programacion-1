def main():
    print_word_and_number_of_letters()

def input_word():
    # El usuario ingresa una palabra. Lo convierto 
    # a una lista para que sea mas facil contar los caracteres.
    word = list(input("Ingrese una palabra >> ").lower())
     
    return word

def count_letters(word, number_of_letters=0):
    for letter_pos in range(len(word)+1):
        number_of_letters =+  letter_pos

    return number_of_letters

def print_word_and_number_of_letters(word_is_not_salir=True, salir=list("salir")):
    while word_is_not_salir:
        word = input_word()
        if word == salir:
            word_is_not_salir = False
        else:
            for letter in word:
                print(letter)

            print(f"La cantidad de letras es: {count_letters(word)}") 

            '''
            Se pudo haber utilizado el metodo len() directamente. 
            Supuse que la idea del ejercicio era usar un ciclo for con contador. 
            Se pudo haber utilizado len(word) en lugar de count_letters(word)
            '''
    else:
        print("Saliendo del programa")


if __name__ == "__main__":
    main()