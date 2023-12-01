import random

def main():
    guess_random_int()

def guess_random_int():
    # level = input("Level: ")
    while True:
        try:
            level = int(input("Level: "))
            # int(level)
        except ValueError:
            continue
        if level <= 0:
            continue

        answer = random.randint(1, level)
        break

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break

main()
