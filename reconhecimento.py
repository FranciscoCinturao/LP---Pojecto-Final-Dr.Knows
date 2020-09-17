import speech_recognition as sr

rec = sr.Recognizer()
with sr.Microphone(0) as fala:
    frase = rec.listen(fala)

print("Falou: " + rec.recognizer_sphinx(frase))
