import random, sys

def play():
    number = input("Elige un numero (1, 2, 3): ")
    if random.randint(1,3) == number:
        sys.exit("You Win!")
    print("U lose :(")
    return

if __name__ == "__main__":
    play()