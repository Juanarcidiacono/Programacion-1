def main():
    n1_divisble_by_n2()

def input_numbers():
    n1 = int(input("Ingrese el numero >> "))
    n2 = int(input("Es divisible por >> "))

    return [n1,n2]

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