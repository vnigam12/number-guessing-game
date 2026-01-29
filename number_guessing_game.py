from random import randint
from typing import Optional

def get_valid_integer(prompt: str) -> int:
    """
    Prompt the user for an integer input.
    Keep asking until a valid integer is entered.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def play_game(min_value: int, max_value: int, max_guesses: int = 10) -> Optional[int]:
    """
    Runs a single round of the number guessing game.

    Args:
        min_value (int): Lower bound of the guessing range.
        max_value (int): Upper bound of the guessing range.
        max_guesses (int, optional): The maximum number of guesses allowed. Defaults to 10.

    Returns:
        Optional[int]: The number attempts taken to guess the correct number.
        None: If the user fails to guess within allowed attempts.
    """
    target = randint(min_value, max_value) # Randomly select a target number within the range
    attempts = 0

    print(f"\n[Computer]: I am thinking of a number between {min_value} and {max_value}.")
    print(f"You have {max_guesses} attempts to guess it.\n")

    # Loop until the user runs out of attempts
    while attempts < max_guesses:
        guess = get_valid_integer(f"Attempt {attempts + 1}/{max_guesses} - Enter your guess: ")

        # Ensure the guess is within the allowed range
        if not min_value <= guess <= max_value:
            print(f"Guess out of range. Please guess a number between {min_value} and {max_value}.\n")
            continue

        attempts += 1

        # Check the user guess against the target number
        if guess == target:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            return attempts
        elif guess < target:
            print("Too low! Try again.\n")
        else:
            print("Too high! Try again.\n")

    # Executed if the loop completes without a correct guess
    print(f"Out of attempts! The correct number was {target}.")
    return None

def main() -> None:
    """
    Main function to control game flow.
    Handles replay logic and tracks the best score.
    """
    best_score: Optional[int] = None # Tracks fewest attempts across games

    while True:
        # Get a valid number range from the user
        min_value = get_valid_integer("Enter the start range number: ")
        max_value = get_valid_integer("Enter the end range number: ")

        if min_value >= max_value:
            print("Start range must be less than the end range.\n")
            continue

        # Play one game round
        attempts = play_game(min_value, max_value)

        # Update best score if the user won
        if attempts is not None:
            if best_score is None or attempts < best_score:
                best_score = attempts
                print("New best score!")
            print(f"Best score so far {best_score} attempts.")

        # Ask the user if they want to play again
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thank you for playing!")
            if best_score is not None:
                print(f"Your best score: {best_score} attempts.")
            break

# Ensures the game runs only when the file is executed directly
if __name__ == '__main__':
    main()
