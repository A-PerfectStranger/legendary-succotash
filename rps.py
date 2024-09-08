import random

def play():
    options = ["rock", "scissors", "paper"]
    print("*---------*")
    print("\t Welcome to ✂️ 📜 🗿")
    print("*---------*")
    x = input("Choose (S)cissor (P)aper (R)ock: ")
    winner(random.choice(options), x.strip().lower())


def winner(compu, p):
    print("Computer choose: ", compu)
    if compu == "rock" and p == "s":
        print("Computer wins!")
    elif compu == "scissors" and p == "p":
        print("Computer wins!")
    elif compu == "paper" and p == "r":
        print("Computer wins!")
    elif compu[0] == p:
        print("Tie!")
    else:
        print("You lose!")
    return 



if __name__ == "__main__":
    play()