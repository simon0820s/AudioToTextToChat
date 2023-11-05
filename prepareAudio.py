import base64
import wave
import io

def useConverter(audio_b64):
  audio_bytes = base64.b64decode(audio_b64)

  with wave.open('audio.wav', 'wb') as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(44100)
    wav_file.setnframes(len(audio_bytes) // 2)

  return wav_file