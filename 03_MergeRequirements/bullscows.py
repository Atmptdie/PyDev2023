import random


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
        word = input(prompt)

    return word


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


def gameplay(ask: callable, inform: callable, words: "list[str]") -> int:
    attempts = 0
    secret = random.choice(words)
    word = ask("Введите слово: ", words)

    while word != secret:
        bulls, cows = bullscows(word, secret)
        inform("Быки: {}, Коровы: {}")

        word = ask("Введите слово: ", words)

    print(f"Да, это и правда '{secret}'. Количество попыток: {attempts}")

