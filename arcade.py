import rps, guess, sys, os

def start():
    while True:
        game = int(input("""
              Please choose a game: 
              1. Rock Scissor Paper
              2. Guess the number
              """))
        
        if game not in [1,2]:
            print("invalid option")
            continue
        if not game:
            break

        os.system('clear')

        if game == 1:
            rps.play()
        else:
            guess.play()

start()

