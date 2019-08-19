class Huffman:
    def __init__(self, action_file="Hello.txt"):
        self.action_file = action_file
        self.store_location = ""
        self.chars = []
        self.numbers = []

    def add_letter(self, letter):
        if self.chars.count(letter) == 1:
            index_of_element = self.chars.index(letter)
            self.numbers[index_of_element] += 1
        else:
            self.chars.append(letter)
            self.numbers.append(1)

    def bubble_sort(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(0, len(self.numbers) - 1):
                if self.numbers[i] > self.numbers[i + 1]:
                    temp_number = self.numbers[i]
                    temp_char = self.chars[i]
                    self.numbers[i] = self.numbers[i + 1]
                    self.chars[i] = self.chars[i + 1]
                    self.numbers[i + 1] = temp_number
                    self.chars[i + 1] = temp_char
                    swapped = True

    def read_uncompressed_file(self):
        file = open(self.action_file, "r")
        for elements in file.read():
            self.add_letter(elements)

    def make_tree(self):
        pass
