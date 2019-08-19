from unittest import TestCase
import Hangman_Game.Hangman as Hangman


class TestHangman(TestCase):

    def test_update_word_updates_display_word_correctly_for_given_letter(self):
        word = Hangman.Hangman()
        word.true_word = "Apple"
        word.display_word = "_ _ _ _ _"
        word.update_word("p")
        self.assertEqual("_ p p _ _", word.display_word)

    def test_update_word_updates_display_word_to_upper_case_for_starting_letter_in_word(self):
        word = Hangman.Hangman()
        word.true_word = "Apple"
        word.display_word = "_ _ _ _ _"
        word.update_word("a")
        self.assertEqual("A _ _ _ _", word.display_word)

    def test_is_solved_returns_true_when_hangman_is_solved(self):
        word = Hangman.Hangman()
        word.true_word = "Apple"
        word.display_word = "A p p l e"
        self.assertTrue(word.is_solved())

    def test_is_solved_returns_false_when_hangman_is_not_solved(self):
        word = Hangman.Hangman()
        word.true_word = "Apple"
        word.display_word = "A p _ l e"
        self.assertFalse(word.is_solved())

    def test_create_display_string_outputs_correct_string_for_apple(self):
        word = Hangman.Hangman()
        word.true_word = "Apple"
        word.create_display_string()
        self.assertEqual("_ _ _ _ _", word.display_word)

    def test_create_display_string_outputs_correct_string_for_orange(self):
        word = Hangman.Hangman()
        word.true_word = "Orange"
        word.create_display_string()
        self.assertEqual("_ _ _ _ _ _", word.display_word)

    def test_is_in_word_returns_true_when_letter_in_word(self):
        word = Hangman.Hangman()
        word.true_word = "Apple"
        self.assertTrue(word.is_in_word("l"))
        self.assertTrue(word.is_in_word("L"))
        self.assertTrue(word.is_in_word("a"))
        self.assertTrue(word.is_in_word("A"))

    def test_is_in_word_returns_false_when_letter_is_not_in_word(self):
        word = Hangman.Hangman()
        word.true_word = "Apple"
        self.assertFalse(word.is_in_word("z"))

    def test_pick_random_word_can_read_file_with_one_word_in(self):
        word = Hangman.Hangman()
        word.pick_random_word("Text.txt")
        self.assertEqual("Text", word.true_word)
