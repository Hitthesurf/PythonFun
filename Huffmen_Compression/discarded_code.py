def make_store_string(self):
    self.binary_string = []
    string_tree = str(self.binary_tree)
    for element in self.all_letters:
        index_of_letter = string_tree.index(element)
        print(index_of_letter)
        right_pointer = index_of_letter
        left_pointer = index_of_letter
        while left_pointer != 0 or right_pointer != len(string_tree) - 1:
            if string_tree[right_pointer + 1] == ",":
                self.binary_string += "0"
            elif string_tree[left_pointer - 1] == ",":
                self.binary_string += "1"
            else:
                print("Error", string_tree[left_pointer - 1], string_tree[right_pointer + 1])

            # Find nearest "]" on right
            while string_tree[right_pointer] != "]":
                right_pointer += 1
            # Find nearest "[" on left
            while string_tree[left_pointer] != "[":
                left_pointer -= 1


def thin_out_array(array):
    string_array = str(array)
    string_array = string_array.replace("'", "")
    string_array = string_array.replace('"', "")
    string_array = string_array.replace(" ", "")
    return string_array


def test_thin_out_array_returns_a_string_of_the_array_without_extra_characters(self):
    actual1 = Huffman_Compression.thin_out_array([[["a", "b"], "c"], ["d", "e"]])
    actual2 = Huffman_Compression.thin_out_array([[['a', ' '], 'c'], ['d', '\n']])
    # actual3 = Huffman_Compression.thin_out_array()
    self.assertEqual("[[[a,b],c],[d,e]]", actual1)
    self.assertEqual("[[[a, ],c],[d,\n]]", actual2)
