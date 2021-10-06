from googletrans import Translator, constants
from pprint import pprint

class TextTranslate:

    def __init__(self):
        self.translator = Translator()

    def initialize(self, lang_ab='hi', text='Nothing to Transalate'):
        self.lang_abb=lang_ab #langabbrivation-to convert
        self.translate_sentence=text #sentense to convert
        
    def transalteText(self):
        # self.detection = self.translator.detect(self.translate_sentence) #for detectipon
        self.translation = self.translator.translate(self.translate_sentence, self.lang_abb) #conversion
        self.translated_sentence = self.translation.text 

        return self.translated_sentence

# abc = translate_lang()
# abc.initialize(lng_ab='gu', text='When You see me sakshi You will hug me')
# print(abc.transalte())
