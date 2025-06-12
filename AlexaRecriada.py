# pip install speechrecognition pyttsx3 pyaudio

import speech_recognition as sr
import os
import pyttsx3

# Inicia reconhecimento e fala
recon = sr.Recognizer()
fala = pyttsx3.init()

# Lista os microfones disponíveis pra confimar e usar
print("Microfones disponíveis:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microfone {index}: {name}")

# Ajustar o índice do microfone conforme a lista acima
MICROFONE_INDEX = 1 

# apps e seus respectivos comandos no pc
comandos = {
    "chrome": "start chrome",
    "word": "start winword",
    "excel": "start excel",
    "visual studio code": "code",
    "vs code": "code",
    "bloco de notas": "notepad",
    "calculadora": "calc",
    "sair": None  # comando pra sair do programa
}

def falar(texto):
    fala.say(texto)
    fala.runAndWait()

def ouvir_microfone():
    with sr.Microphone(device_index=MICROFONE_INDEX) as mic:
        print("Ajustando para ruído ambiente...")
        recon.adjust_for_ambient_noise(mic, duration=1)
        print("Escutando...")
        try:
            audio = recon.listen(mic, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("⏰ Tempo esgotado. Nenhum som detectado.")
            return ""
    try:
        comando = recon.recognize_google(audio, language="pt-BR")
        print("Você disse:", comando.lower())
        return comando.lower()
    except sr.UnknownValueError:
        print("😕 Não entendi o que você disse.")
        return ""
    except sr.RequestError as e:
        print(f"Erro ao se conectar com o serviço: {e}")
        return ""

def executar_comando(comando):
    if "sair" in comando:
        falar("Encerrando o programa. Até mais!")
        print("Programa encerrado pelo usuário.")
        exit(0)

    for chave in comandos:
        if chave in comando:
            if comandos[chave]:  # Se o comando não for None
                os.system(comandos[chave])
                falar(f"Abrindo {chave}")
            else:
                falar("Comando não configurado.")
            return
    falar("Não conheço esse aplicativo.")

# Loop principal
if __name__ == "__main__":
    falar("Olá, pode falar o nome do aplicativo que deseja abrir ou diga sair para encerrar.")
    while True:
        comando_voz = ouvir_microfone()
        if comando_voz:
            executar_comando(comando_voz)
