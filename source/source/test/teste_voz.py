import pyttsx3

maquina = pyttsx3.init()
vozes = maquina.getProperty('voices')
for voz in vozes:
    print(voz.id)
