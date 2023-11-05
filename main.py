import speech_recognition as sr

def useRecognizer():

  r = sr.Recognizer()
  audio = sr.AudioFile('luisAudio.wav')

  with audio as source:
    audio_to_analyze = r.record(source)

  text = r.recognize_google(audio_to_analyze, language='es')

  print(text)

if __name__=='__main__':
  useRecognizer()