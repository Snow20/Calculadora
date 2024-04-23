#exercices calculator

print("calcula")
print("suma, resta, multiplicar, dividir")
print()

n1 = float(input("ingresa el primer numero: "))
n2 = float(input("ingresa el segundo numero: "))
operacion = input("que operacion: ?")

def funcionSuma(n1,n2):
    sumar = n1 + n2
    print()
    print("resultado es: " + str(sumar))
    return

def funcionResta(n1,n2):
    restar = n1 - n2
    print()
    print("resultado es: " + str(restar))
    return

def funcionMultiplica(n1,n2):
    multiplicar = n1 * n2
    print()
    print("resultado es: " + str(multiplicar))
    return

def funcionDivision(n1,n2):
    dividir = n1 / n2
    print()
    print("resultado es: " + str(dividir)) 
    return     

if operacion == "suma":
        funcionSuma(n1,n2)
elif operacion == "resta":
        funcionResta(n1,n2)
elif operacion == "multiplica":
        funcionMultiplica(n1,n2)
elif operacion == "divide":
        funcionDivision(n1,n2)
else:
        print()
        print("opcion no es valida")

