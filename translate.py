# from deep_translator import GoogleTranslator
#
# #to_translate = 'I want to translate this text'
# #translated = GoogleTranslator(source='en', target='tr').translate(to_translate)
# """with open("out_text1.txt","rb") as f:
#     content = f.read()
#     #print(content)
#     translated = GoogleTranslator(source='en', target='tr').translate(content)
#     print(translated)"""
# # translated = GoogleTranslator(source='en', target='tr').translate_file("out_text.txt")
# # print(translated)
# def translate(text):
#     translated = GoogleTranslator(source='en', target='tr').translate(text)
#     return translated

from googleTranslate import Translator
def translate(text):
    translated_text = Translator('ja', 'auto')