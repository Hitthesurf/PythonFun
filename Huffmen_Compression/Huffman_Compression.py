def binary_splitter(string, number):
    string += "0" * (len(string) % number)
    split_string = []
    for i in range(0, len(string), number):
        temp_add = string[i:i + number]
        temp_add = int(temp_add, 2)
        split_string.append(temp_add)
    return split_string


def get_binary_string(byte_array):
    binary_string = ""
    for byte in byte_array:
        temp_array = list(bin(byte))
        del temp_array[0:2]
        temp_array.insert(0, '0' * (8 - len(temp_array)))
        binary_string += ''.join(temp_array)
    return binary_string


class Huffman:
    def __init__(self, uncompressed_file="Hello.txt"):
        self.uncompressed_file = uncompressed_file
        self.compressed_file = "Byte_File"
        self.chars = []
        self.all_letters = []
        self.numbers = []
        self.binary_tree = []
        self.binary_string = []

    def add_letter(self, letter):
        self.all_letters.append(letter)
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
        file = open(self.uncompressed_file, "r")
        for elements in file.read():
            self.add_letter(elements)
        file.close()

    def make_tree(self):
        temp_chars = self.chars[:]  # So it passes by value
        temp_num = self.numbers[:]
        while len(self.chars) > 2:
            total_number = self.numbers[0] + self.numbers[1]
            add_section = [self.chars[0], self.chars[1]]
            del self.chars[0:2]
            del self.numbers[0:2]
            self.chars.insert(0, add_section)
            self.numbers.insert(0, total_number)
            self.bubble_sort()

        self.binary_tree = self.chars
        self.chars = temp_chars
        self.numbers = temp_num

    def write_compressed_file(self):
        file = open(self.compressed_file, 'wb')

        byte_array = binary_splitter(self.binary_string, 8)
        file.write(bytes(byte_array))
        file.close()
        self.binary_string = ""

    def read_compressed_file(self):
        file = open(self.compressed_file, 'rb')
        byte_array = file.read()
        self.binary_string = get_binary_string(byte_array)
        file.close()

    def save_binary_tree(self):
        pass

    def read_binary_tree(self):
        pass

    def write_uncompressed_file(self):
        file = open(self.uncompressed_file, "w")
        for element in self.all_letters:
            file.write(element)
        file.close()

    def create_binary_store_string(self):
        pass

    def read_stored_binary_string(self):
        temp_tree = self.binary_tree[:]
        for digit in self.binary_string:
            temp_tree = temp_tree[:][int(digit)]
            if type(temp_tree) == str:
                self.all_letters.append(temp_tree)
                temp_tree = self.binary_tree[:]
