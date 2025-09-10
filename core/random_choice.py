# Using random.choice() for random selection from a list of options
# Run with: python random_choice.py

import random

verbose = True

def get_random_name():
    # The pool
    names = [
        "Oliver", "Emma", "Liam", "Ava", "Noah",
        "Isabella", "William", "Sophia", "James",
    ]

    if verbose:
        print("Names:", names)

    # Make a random choice out of the pool
    return random.choice(names)


def get_random_number(max):
    # The pool
    numbers = []

    # Fill in the pool with numbers from 1 to max (upper-limit)
    for i in range(1, max + 1):
        numbers.append(i)

    if verbose:
        print("Numbers:", numbers)
    
    return random.choice(numbers)


if __name__ == "__main__":
    random_name = get_random_name()
    print(f"Random name: {random_name}")

    print()

    random_number = get_random_number(20)
    print(f"Random number: {random_number}")