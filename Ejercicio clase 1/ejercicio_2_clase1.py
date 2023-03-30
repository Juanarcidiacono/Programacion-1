num1 = int(input("primer numero: "))
num2 = int(input("segundo numero: "))

producto = num1 * num2

if producto < 1000:
    print(producto)
elif (num1 == 50) and (num2 == 50):
    print("50 y 50")
else:
    print(num1 + num2)