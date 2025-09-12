# Programming Language Guessing Game

A simple command-line guessing game where players try to identify a programming language within a limited number of attempts.

## How it Works

The game selects a secret programming language and gives you 3 chances to guess it correctly. All guesses are converted to lowercase for easier comparison.

## Game Rules

- You have 3 attempts to guess the correct programming language
- Guesses are case-insensitive
- Win by guessing correctly within the limit
- Lose if you run out of guesses

## Running the Game

1. Make sure you have Python installed
2. Run the script in your terminal or command prompt
3. When prompted, enter your guess for the programming language
4. The game will tell you if you won or lost

## Code Structure

- `secret_word`: The target programming language to guess
- `guess_limit`: Maximum number of allowed guesses (set to 3)
- `guess_count`: Tracks current number of attempts
- `out_of_guesses`: Flag to determine if the guess limit has been reached

The game uses a while loop to continue until either the correct answer is guessed or the attempt limit is reached.
