import unittest
from guessing_game import play_game


class TestGuessingGame(unittest.TestCase):

    def test_game_returns_attempts_or_none(self):
        """
        play_game should return either an int (attempts) or None.
        """
        result = play_game(1, 1, max_guesses=1)
        self.assertTrue(result is None or isinstance(result, int))


if __name__ == "__main__":
    unittest.main()
