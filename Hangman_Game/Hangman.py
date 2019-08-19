import random


class Hangman:
    def __init__(self):
        self.true_word = ""
        self.display_word = ""
        self.letters_used = []
        self.lives = 7

    def update_word(self, letter):
        lower_true_word = self.true_word.lower()
        lower_letter = letter.lower()
        num_of_chars = len(self.true_word)
        display_word_array = list(self.display_word)
        for i in range(0, num_of_chars):
            if lower_letter == lower_true_word[i]:
                display_word_array[2 * i] = lower_letter
        display_word_array[0] = display_word_array[0].upper()
        self.display_word = "".join(display_word_array)

    def pick_random_word(self, file="Hangman.txt"):
        file = open(file, "r")
        word_list = file.read().splitlines()
        self.true_word = random.choice(word_list)

    def create_display_string(self):
        output_display = '_ '
        word_length = len(self.true_word)
        output_display *= word_length - 1
        output_display += '_'
        self.display_word = output_display

    def is_solved(self):
        if self.display_word.count("_") == 0:
            return True
        else:
            return False

    def is_in_word(self, letter):
        if self.true_word.lower().count(letter.lower()) == 0:
            return False
        else:
            return True

    def restart(self):
        self.true_word = ""
        self.display_word = ""
        self.letters_used = []
        self.lives = 7

    def play(self):
        self.restart()
        self.pick_random_word()
        self.create_display_string()
        while self.lives != 0:
            if self.is_solved():
                print("You win")
                break
            else:
                print("Guess Word: ", self.display_word)
                print("Number of Lives: ", self.lives)
                print("Letters Used: ", self.letters_used)
                letter = input("Enter letter: ")
                if self.is_in_word(letter):
                    self.update_word(letter)
                else:
                    self.lives -= 1
                    self.letters_used.append(letter)
        if self.lives == 0:
            print("Game Over")
            print (self.true_word)


if __name__ == '__main__':
    hangman = Hangman()
    hangman.play()
