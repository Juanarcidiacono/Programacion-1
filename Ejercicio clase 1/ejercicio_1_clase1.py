"""
Ejercicio 1:

Existen al menos dos metodos ampliamente utilizados para medir la temperatura ambiente. Uno es usando grados Farenheit, y otro usando grados Celsius. Codifiquen dos programas: Uno que convierta un numero ingresado de grado Celsius a Farenheit, y otro que convierta de Farenheit a Celsius.

Formula:
ºF = ºC x 1.8 + 32
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

