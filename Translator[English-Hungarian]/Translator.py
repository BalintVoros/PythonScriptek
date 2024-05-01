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
        direction = input("Enter 'en-hu' for English to Hungarian or 'hu-en' for Hungarian to English translation: ")
        if direction == 'en-hu':
            translation = translator.translate(text, src='en', dest='hu')
        elif direction == 'hu-en':
            translation = translator.translate(text, src='hu', dest='en')
        else:
            print("Invalid direction! Please enter 'en-hu' or 'hu-en'.")
            continue
        print(translation.text)

if __name__ == "__main__":
    main()
