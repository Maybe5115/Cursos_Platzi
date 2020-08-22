import random


def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for __ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append(tiro)
    return secuencia_de_tiros


def main(numero_de_intentos, numero_de_tiros):
    tiros = []
    for __ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)
    
    tiros_con_1 = 0
    for tiro in tiros:
        if 1 in tiro:
          tiros_con_1 += 1

    p_tiro_1 = tiros_con_1/numero_de_intentos  
    print(f'Probabilidad de obtener un 1 en {numero_de_tiros} tiros es igual a la {p_tiro_1}')


if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantos tiros del dado: '))
    numero_de_intentos = int(input('Correr simulación: '))

    main(numero_de_intentos, numero_de_tiros)
