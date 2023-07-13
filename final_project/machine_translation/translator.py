"""
This module's purpose is to translate text from english to french
and from french to english
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This functions translates an english string to french and returns it
    """
    french_translator = MyMemoryTranslator(source="en-US", target="french")
    return french_translator.translate(english_text)

def french_to_english(french_text):
    """
    This functions translates an english string to french and returns it
    """
    english_translator = MyMemoryTranslator(source="fr-FR", target="english")
    return english_translator.translate(french_text)
