import random
from urllib.request import urlopen
import os
import argparse


def bullscows(guess: str, secret: str) -> "tuple[int, int]":
    cows = bulls = 0
    letters_cnt = {}
    guess_cows = ""

    for i in range(len(secret)):
        if i < len(guess):
            if guess[i] == secret[i]:
                bulls += 1
                continue
            else:
                guess_cows += guess[i]

        if secret[i] in letters_cnt:
            letters_cnt[secret[i]] += 1
        else:
            letters_cnt[secret[i]] = 1

    for i in range(min(len(secret), len(guess_cows))):
        if guess_cows[i] in letters_cnt:
            if letters_cnt[guess_cows[i]] > 0:
                cows += 1

    return (bulls, cows)


def ask(prompt: str, valid: "list[str]" = None) -> str:
    word = input(prompt)
    while not (valid is None or word in valid):
        print(f"{word} is not a valid word! Try again\n")
        word = input(prompt)

    return word


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


def gameplay(ask: callable, inform: callable, words: "list[str]") -> int:
    attempts = 0
    secret = random.choice(words)
    word = ask("Enter word: ", words)

    while word != secret:
        bulls, cows = bullscows(word, secret)
        inform("Bulls: {}, Cows: {}", bulls, cows)
        print("----------------------------\n")

        word = ask("Enter word: ", words)

    print(f"Congratulations! It was '{secret}'. Attempts: {attempts}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="bullscows")

    parser.add_argument("words_source")
    parser.add_argument("length", type=int, default=5, nargs='?')

    parsed_args = parser.parse_args()

    words_source = parsed_args.words_source
    length = parsed_args.length

    is_local_file = os.path.isfile(words_source)
    words = None
    if is_local_file:
        with open(words_source, "r", encoding='utf-8') as f:
            words = [w.strip() for w in f.readlines()]
    else:
        print("Trying to open url...")
        try:
            with urlopen(words_source) as f:
                words = f.read().decode().split("\n")
                print("Successfully loaded words from url")
        except ValueError:
            raise ValueError("Source is neither a path nor URL. Try again!")

    words = [word for word in words if len(word) == length]
    if not words:
        raise ValueError("There's no words with such length! Try again")
    print(f"Starting game!")
    gameplay(ask, inform, words)
