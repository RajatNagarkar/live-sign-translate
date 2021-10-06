from gtts import gTTS
import os
from io import BytesIO
from playsound import playsound
class TextToAudio:
    def __init__(self):
        self.lang = 'en',
        self.accent = 'co.in'
        self.sentence = "Nothing to Play"
        if os.path.exists('audio/') is False:
            os.mkdir('audio/')

        self.mp3File = open('audio/audio.mp3', 'wb')
        self.audioPath = 'audio/audio.mp3'
    
    def setLang(self, lang):
        self.lang = lang

    def setText(self, sentence):
        self.sentence = sentence

    def toSpeech(self):
        speech=gTTS(self.sentence, lang=self.lang, tld=self.accent)
        speech.write_to_fp(self.mp3File)
        self.mp3File.close()
    
    
    def playAudio(self):
        playsound(self.audioPath)
    
    def __del__(self):
        os.remove(self.audioPath)
        os.rmdir('audio')

# obj=TextToAudio()
# obj.setLang('gu')
# obj.setText('હાય નાના તમે કેવી રીતે છો')
# obj.toSpeech()
# obj.play_audio()