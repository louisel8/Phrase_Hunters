import random

class Phrase:
    def __init__(self, phrases):
        self.phrase = random.choice(phrases).lower()

    def display(self, guessed_letters):
        display_phrase = ""
        for char in self.phrase:
            if char in guessed_letters:
                display_phrase += char
            elif char == " ":
                display_phrase += " "
            else:
                display_phrase += "_ "
        print(display_phrase.strip())

    def check_letter(self, letter):
        return letter in self.phrase

    def check_complete(self, guessed_letters):
        return all(char in guessed_letters or char == " " for char in self.phrase)
