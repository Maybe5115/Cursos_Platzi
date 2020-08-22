def run(numero, maximo):
    total = numero
    while total <= (maximo)*(1/4):
        total = total*2
        print(str(total))
    total = total*2
    print("Listo, su total es: " + str(total))
    return total


if __name__ == "__main__":
    numero = int(input("Ingrese un numero: "))
    maximo = int(input("Ingrese un maximo: "))
    run(numero, maximo)