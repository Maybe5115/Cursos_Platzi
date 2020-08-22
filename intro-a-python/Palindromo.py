def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("es palindromo")
    else:
        print("No es palindromo")


if __name__ == "__main__":
    run()


