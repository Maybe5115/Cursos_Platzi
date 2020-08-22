import random
import collections

PALOS =  ["Espada", "Corazon", "Rombo", "Trebol"]
VALORES = ["as", "2", "3", "4", "5", "6", "7" ,"8", "9", "10", "J", "Q", "K"]

def crear_baraja():
    barajas =[]

    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas


def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano


def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for __ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)
    
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        contador = dict(collections.Counter(valores))
        for val in contador.values():
            if val == 2:
                pares += 1
                break
    
    p_par = pares/intentos
    print(f'p de tener un par en una mano de {tamano_mano} cartas es de {p_par}')



if __name__ == "__main__":
    tamano_mano = int(input("Tamaño para la mano: "))
    intentos = int(input("Cuantos intentos quieres hacer: "))

    main(tamano_mano, intentos)
