
import numpy as np


#a = np.array([1, 0, 0, 0])
#b = np.array([0, 1, 0, 0])

#print(np.dot(a,b))
#print(a.T@b)

#def p(x):
#    return  np.array([1,2])@np.array([1,x])

#print(p(5))

tweet1 = "Gran mexicano y excelente en su área, su muerte es una enorme perdida y debería ser luto nacional!!!"

tweet2 = "Vaya señora que bueno que se asesora por alguien inteligente no por el ignorante del Gatt"

tweet3 = "Se me ocurre y sin ver todos los videos de Plazti que me informéis por dónde empiezo. Entiendo que os tendría que decir quién soy y que quiero, vamos conocerme para asesorarme bien. Un saludo"

tweet4 = "Soy docente universitario, estoy intentando preparar mis clases en modo platzi bien didáctico, (le llamo modo noticiero), descargue una plataforma gratuita de grabación y transmisión de vídeo, se llama Obs estudio!bueno la sigo remando con sus funciones pero sé que saldrá algo!"

Tweets = [tweet1, tweet2, tweet3, tweet4]

palabrasBuenas = ["gran", "excelente", "bueno", "inteligente", "bien", "didáctico"]
palabrasMalas = ["muerte", "perdida", "luto", "ignorante"]
palabrasNeutras = ["nacional", "asesora", "platzi", "conocerme", "docente", "clases", "plataforma", "remando"]

def sentimientos(Tuit):
    tuit = (Tuit.replace("!", "").replace(",", "").lower().split(" "))
    pBuenas = 0
    pMalas = 0
    pNeutras = 0
    for palabra in tuit:
        for buenas in palabrasBuenas:
            if palabra == buenas:
                pBuenas += 1
        for neutras in palabrasNeutras:
            if neutras == palabra:
                pNeutras += 1
        for malas in palabrasMalas:
            if malas == palabra:
                pMalas += 1
    
    s = np.array([pBuenas, pNeutras, pMalas])
    avg = (s.dot(np.array([1, 1, 1])))/len(tuit)
    puntaje = np.array([1, 0, -1]).dot(s)    
    print(avg, puntaje)
    return avg, puntaje, tuit

for Tweet in Tweets:
    sentimientos(Tweet)