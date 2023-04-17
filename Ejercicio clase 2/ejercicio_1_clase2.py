"""
-  Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo 
mostrar por pantalla su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo
"""

def main():
    numbers(2,5)

def numbers(num1, num2):
    
    if (num1 >= num2):
        print(f"Suma =  {num1+ num2}")
        print(f"Diferencia =   {num1 - num2}")
    else:
        print(f"Producto = {num1*num2}")
        print(f"Division = {num1/num2}")



if __name__ == "__main__":
    main()