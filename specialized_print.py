import string
import random
import time


def specialized_print(to_print: str) -> None:
    placeholder: str = ""

    for character in to_print:
        if character != " ":
            for _ in range(5, 7):
                randomized_placeholder: str = placeholder + random.choice(
                    string.ascii_letters
                )
                print(f"\r{randomized_placeholder}", end="\r")
                time.sleep(random.uniform(0.01, 0.3))

        placeholder += character
        print(f"\r{placeholder}", end="\r")
        time.sleep(random.uniform(0.01, 0.2))

    print(f"\r{to_print}")
