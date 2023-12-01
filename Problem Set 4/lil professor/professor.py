import random

def main():
    level = get_level()
    
    # score starts at 0
    score = 0
    # loop 10 times == 10 questions
    for i in range(10):
        # get current ints
        x, y = generate_integer(level)
        # get current answer
        answer = x + y
        # prompt user for answer
            # only three tries per questions
        for j in range(3):
            while True:
                try:
                    user_answer = int(input(f"{x} + {y} = "))
                except ValueError:
                    continue
                finally:
                    break
            
            if user_answer == answer:
                score += 1
                break
            elif j == 2:
                print(f"{x} + {y} = {answer}")
            else:
                print("EEE")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
    if level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    if level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

main()
