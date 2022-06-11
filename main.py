print ("Hi Player, I'm Computer. Let's play Rock, Paper, Scissors!")
import random
Running = True
while Running:
    print ("Rock = R")
    print ("Paper = P")
    print ("Scissors = S")
    Options = ("R", "P", "S")
    UserChoice = input("Rock, Paper, Scissors?\nSHOOT!!! ('R', 'P', 'S'):").upper()
    if UserChoice not in Options:
        print ("Invalid input, please try again.\n")
        continue   
    ComputerChoice = random.choice(Options)
    print (f"\nPlayer ({UserChoice}): CPU ({ComputerChoice}).")

    if UserChoice == ComputerChoice:
            print ("Both players picked " + UserChoice + ". It's a draw.\nPlay again.\n")
            continue
    elif UserChoice == "R":
        if ComputerChoice == "S":
            print ("Rock crushes scissors, YOU WIN. Hippie!")
        else:
            print("Paper covers rock. COMPUTER WINS, sowie.")
    elif UserChoice == "S":
        if ComputerChoice == "P":
            print ("Scissors cuts paper. YOU WIN. Yaay!")
        else:
            print ("Rock crushes scissors. COMPUTER WINS, sowie.")
    elif UserChoice == "P":
        if ComputerChoice == "R":
            print ("Paper covers rock, YOU WIN. Swoosh!")
        else:
            print ("Scissors cuts paper. COMPUTER WINS, sowie.")
    Running = False
