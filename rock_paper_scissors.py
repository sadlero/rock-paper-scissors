import random

def RPS():

    play = ["ROCK", "PAPER", "SCISSORS"]

    print('Enter "ROCK", "PAPER", or "SCISSORS".')

    P1 = random.choice(play)


    P2 = input()
    P2 = P2.upper().strip()



    if P2 not in play:
        print('You can only answer "ROCK" or "PAPER" or "SCISSORS".')
    elif P1 == P2:
        print(f"The computer also played {P1}, it's a tie.")
    elif (P1 == "ROCK" and P2 == "PAPER") or (P1 == "PAPER" and P2 == "SCISSORS") or (P1 == "SCISSORS" and P2 == "ROCK"):
        print(f"The computer played {P1}. {P2} beats {P1}, you win!")
    else:
        print(f"The computer played {P1}. {P1} beats {P2}, you lose.")

while True:    
    RPS()

    again = input("Play again? (Y/N): ").upper().strip()

    if again != "Y":
        break