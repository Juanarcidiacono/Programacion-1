def main():
    print_word()

def input_word():
    word = list(input("Ingrese una palabra >> "))
    return word

def count_letters(word, number_of_letters=0):
    for letter_pos in range(len(word)):
        number_of_letters = + letter_pos
    return number_of_letters

def print_word(word=None, key=list("salir")):
    while word != key:
        word = input_word()
        for letter in word:
            print(letter)

        print(f"La cantidad de letras es: {count_letters(word)}") #se pudo haber utilizado el metodo len directamente. Supuse que la idea del ejercicio era usar un ciclo for con contador. Se pudo haber utilizado len(word)

    print("Saliendo del programa")


if __name__ == "__main__":
    main()
