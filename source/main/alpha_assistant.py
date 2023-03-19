import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit


audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            maquina.say('Hello')
            maquina.runAndWait()
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'adam' in comando:
                comando = comando.replace('adam', '')
    except:
        maquina.say('Não escutei direito. Pode repetir?')
        maquina.runAndWait()
        print('finalizando e repetindo')

    return comando


def comando_voz_usuario():
    #condições
    comando = executa_comando()

    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()

    elif 'pesquise por' in comando:
        procurar = comando.replace('pesquise por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        maquina.say(resultado)
        maquina.runAndWait()

    elif 'reproduza' in comando:
        musica = comando.replace('reproduza','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Reproduzindo...')
        maquina.runAndWait()

    else:
        print('Se não')

comando_voz_usuario()