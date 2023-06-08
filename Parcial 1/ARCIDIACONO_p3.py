# ARCIDIACONO JUAN IGNACIO DNI:38.684.730

def main():
    print_word_and_number_of_letters()

# El usuario ingresa una palabra. Lo convierto 
# a una lista para que sea mas facil contar los caracteres.
def input_word():

    word = list(input("Ingrese una palabra >> ").lower())
     
    return word

# Este metodo pudo haber sido reemplazo por el metodo len(). 
# Supuse que el objetivo del ejercicio era crear un ciclo for con un contador.
def count_letters(word, number_of_letters=0):

    for pos in word:
        number_of_letters += 1
    
    return number_of_letters

# Mientras la palabra ingresada NO sea 'salir', 
# entonces que imprima en pantalla cada una de las letras de la palabra ingreada. 
# Al final del bucle, mostrará la cantidad de letras de la palabra.
# Si la palabra ingresada es salir, entonces se finaliza el programa y se imprime un mensaje.
def print_word_and_number_of_letters(word_is_not_salir=True, salir=list("salir")):

    while word_is_not_salir:
        word = input_word()
        if word == salir:
            word_is_not_salir = False
        else:
            for letter in word:
                print(letter)

            print(f"La cantidad de letras es: {count_letters(word)}") 
    else:
        print("Saliendo del programa")


if __name__ == "__main__":
    main()