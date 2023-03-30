"""
Ejercicio 1:

Existen al menos dos metodos ampliamente utilizados para medir la temperatura ambiente. Uno es usando grados Farenheit, y otro usando grados Celsius. Codifiquen dos programas: Uno que convierta un numero ingresado de grado Celsius a Farenheit, y otro que convierta de Farenheit a Celsius.

Formula:
ºF = ºC x 1.8 + 32


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ejercicio 2:

Una practica cotidiana en desarrollo de software es mirar programas de otros. En este ejercicio, van a tener acceso al codigo, pueden probarlo con distintos numeros y verificar el resultado. Lo que les pido es que cuenten en sus palabras, lo que hace el programa.


num1 = int(input("primer numero: "))
num2 = int(input("segundo numero: "))

producto = num1 * num2

if producto < 1000:
    print(producto)
elif (num1 == 50) and (num2 == 50):
    print("50 y 50")
else:
    print(num1 + num2)
    """

#Ejercicio 1
import math

def to_farenheit(temp):
    return temp * 1.8 + 32

def to_celcius(temp):
    return (math.floor((temp - 32) / 1.8))

def main():
    num1 = float(input("Grado °F "))
    num2 = float(input("Grado °C "))
    to_farenheit(num2)
    to_celcius(num1)

if __name__ == "__main__":
    main()

