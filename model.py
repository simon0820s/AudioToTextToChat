import speech_recognition as sr
import openai

def useModels(audio):
  audio = sr.AudioFile('luisAudio.wav')
  text = useRecognizer(audio)
  print(text)
  response = useGPT(text)
  print(response)
  

def useRecognizer(audio):

  r = sr.Recognizer()

  with audio as source:
    audio_to_analyze = r.record(source)

  text = r.recognize_google(audio_to_analyze, language='es')

  return text

def useGPT(text):
  text = "que piensas acerca de lo siguiente: " + text + "?"
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    prompt=(text)

)
  return response

if __name__=='__main__':
  audio = sr.AudioFile('luisAudio.wav')
  useModels(audio)