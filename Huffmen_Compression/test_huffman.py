from unittest import TestCase
from Huffmen_Compression import Huffman_Compression


class TestHuffman(TestCase):
    def test_add_letter_adds_new_letter_to_array_and_stores_one_as_number(self):
        comp = Huffman_Compression.Huffman()
        comp.add_letter("m")
        self.assertEqual("m", comp.chars[0])
        self.assertEqual(1, comp.numbers[0])

    def test_add_letter_adds_to_count_of_letter_with_letter_already_in_array(self):
        comp = Huffman_Compression.Huffman()
        comp.add_letter("M")
        comp.add_letter("M")
        comp.add_letter("M")
        self.assertEqual("M", comp.chars[0])
        self.assertEqual(3, comp.numbers[0])

    def test_bubble_sort_sorts_data_into_increasing_order_on_number_of_elements(self):
        comp = Huffman_Compression.Huffman()
        comp.chars = ["d", "e", "J", "5", "u", "f", "0"]
        comp.numbers = [10, 8, 2, 2, 15, 12, 5]
        expected_chars = ["J", "5", "0", "e", "d", "f", "u"]
        expected_numbers = [2, 2, 5, 8, 10, 12, 15]
        comp.bubble_sort()
        self.assertEqual(expected_chars, comp.chars)
        self.assertEqual(expected_numbers, comp.numbers)

    def test_reading_text_file_and_adding_and_ordering_arrays(self):
        comp = Huffman_Compression.Huffman("Hello.txt")
        comp.read_uncompressed_file()
        comp.bubble_sort()
        self.assertEqual(["H", "e", " ", "\n", "w", "r", "d", "o", "l"], comp.chars)
        self.assertEqual([1, 1, 1, 1, 1, 1, 1, 2, 3], comp.numbers)

    def test_make_tree_creates_the_correct_array_to_store_the_tree_in(self):
        comp = Huffman_Compression.Huffman()
        comp.chars = ["a", "b", "c", "d", "e"]
        comp.numbers = [1, 2, 3, 4, 5]
        comp.make_tree()
        self.assertEqual([[["a", "b"], "c"], ["d", "e"]], comp.binary_tree)

    def test_make_tree_does_not_modify_chars_and_numbers_once_finished(self):
        comp = Huffman_Compression.Huffman()
        comp.chars = ["a", "b", "c", "d", "e"]
        comp.numbers = [1, 2, 3, 4, 5]
        comp.make_tree()
        self.assertEqual(["a", "b", "c", "d", "e"], comp.chars)
        self.assertEqual([1, 2, 3, 4, 5], comp.numbers)
