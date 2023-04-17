"""
Se ingresan tres notas de un alumno, 
si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".
"""

def main():
    promedio(7,8,7)

def promedio(n1,n2,n3):
    
    if((n1+n2+n3)/3 >= 7):
        print("Promocionado")
    else:
        print("No esta promocionado")

if __name__ == "__main__":
    main()

