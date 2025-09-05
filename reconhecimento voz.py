import speech_recognition as sr

def ouvir_microfone(tempo=10):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.record(source, duration=tempo)
        print("Escutando...")
        try:
            texto = r.recognize_google(audio, language='pt-BR')
            print(f"Transcrição: {texto}")
        except sr.UnknownValueError:
            print("Não foi possível transcrever o que foi falado.")

ouvir_microfone(10)