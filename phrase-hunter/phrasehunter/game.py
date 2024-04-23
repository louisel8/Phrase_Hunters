from phrasehunter import example
from phrasehunter import phrase

class Game:

    def __init__(self):
        self.missed = 0
        self.active_phrase = self.get_random_phrase()
        self.guesses = []
        self.not_in_phrase = []

    def start(self):
        self.welcome()
        while True:
            self.active_phrase.display(self.guesses)
            guess = self.get_guess()
            self.guesses.append(guess)
            if guess not in self.active_phrase.phrase:
                self.missed += 1
                self.not_in_phrase.append(guess)
                print(" - not in phrase: {}".format(", ".join(self.not_in_phrase)))
                print(f" - {5-self.missed} out of 5 lives remaining.\n")

            self.game_over()

    def get_random_phrase(self):
        return phrase.Phrase(example.phrase_options)

    def welcome(self):
        print("Welcome to the Phrase Guessing Game!")
        print("Try to guess the hidden phrase by entering one letter at a time.")
        print("Let's get started!")
        print()

    def get_guess(self):
        while True:
            guess = input("Enter your guess (one letter): ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in self.guesses:
                    print("- you have already guessed this letter, please try another one.\n")
                else:
                    return guess
            else:
                print("Invalid input, please enter a single letter.\n")

    def game_over(self):
        if self.active_phrase.check_complete(self.guesses):
            print("Congratulations! You've nailed it. The phrase is: ")
            self.active_phrase.display(self.guesses)
            print()
            self.play_again()
        elif self.missed >= 5:
            print("Sorry, you've run out of guesses.")
            self.play_again()

    def play_again(self):
        choice = input("Would you like to play again?\n- enter Y or y to continue playing;\n- enter any other keys to quit; ").lower()
        print()
        if choice == 'yes' or choice == 'y':
            self.missed = 0
            self.guesses = []
            self.not_in_phrase = []
            self.active_phrase = self.get_random_phrase()
        else:
            print("Thanks for playing!")
            exit()
