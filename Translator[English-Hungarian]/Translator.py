import os
import sys
from googletrans import Translator

def main():
    translator = Translator()
    print("Welcome to the Translator!")
    print("Type 'exit' to quit the program.")
    while True:
        text = input("Enter the text you want to translate: ")
        if text == "exit":
            break
        direction = input("Enter the direction of the translation (en-hu, hu-en, en-de, de-en, hu-de, de-hu, hu-fr, fr-hu): ")
        if direction == 'en-hu':
            translation = translator.translate(text, src='en', dest='hu')
        elif direction == 'hu-en':
            translation = translator.translate(text, src='hu', dest='en')
        elif direction == 'en-de':
            translation = translator.translate(text, src='en', dest='de')
        elif direction == 'de-en':
            translation = translator.translate(text, src='de', dest='en')
        elif direction == 'hu-de':
            translation = translator.translate(text, src='hu', dest='de')
        elif direction == 'de-hu':
            translation = translator.translate(text, src='de', dest='hu')
        elif direction == 'hu-fr':
            translation = translator.translate(text, src='hu', dest='fr')
        elif direction == 'fr-hu':
            translation = translator.translate(text, src='fr', dest='hu')

        else:
            print("Invalid direction! Please enter 'en-hu' or 'hu-en'.")
            continue
        print(translation.text)

if __name__ == "__main__":
    main()
