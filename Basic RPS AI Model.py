# // Basic RPS AI Model By Manav.M 2022 //
# There may be some bugs so keep that in mind.

import random
from collections import Counter
ai = "aiRPS-v1.2"
epochs = 12
data = []
options = ["rock", "paper", "scissors"]
assignInfo = int(input("How many iterations do you want the AI to learn from? "))
aiplay = ""

for i in range(assignInfo):
    newval = input(f"\nIteration {i+1}: What are you going to play? Rock, paper, or scissors? ")
    if newval.lower() == "rock":
        data.append(newval.lower())
        print("Data value successfully stored.")
    elif newval.lower() == "paper":
        data.append(newval.lower())
        print("Data value successfully stored.")
    elif newval.lower() == "scissors":
        data.append(newval.lower())
        print("Data value successfully stored.")
    else:
        print("Error, not a sufficient data value. Please enter rock, paper or scissors.")
        newval2 = input(f"\nIteration NIL: What are you going to play? Rock, paper, or scissors? ")
        if newval.lower() == "rock" or "paper" or "scissors":
            data.append(newval2.lower())
            print("Data value successfully stored.")
        else:
            print("You made another mistake? Restart the program for it to be functional.")
    

countR = data.count("rock")
countP = data.count("paper")
countS = data.count("scissors")

least_common = Counter(data).most_common()[-1]
most_common = most_common = Counter(data).most_common(1)[0][0]


class branch():
    def learn():
        print(f"Initiate ({ai})")
        global totalvals
        totalvals = countR + countP + countS
        global chanceR
        chanceR = countR / totalvals
        global chanceP
        chanceP = countP / totalvals
        global chanceS
        chanceS = countS / totalvals
            
    def think():
        highChance = max(chanceR, chanceP, chanceS)
        lowChance = min(chanceR, chanceP, chanceS)
        medChance = 1
        if highChance == chanceR and lowChance == chanceP:
            medChance = chanceS
        if highChance == chanceP and lowChance == chanceS:
            medChance = chanceR
        if highChance == chanceR and lowChance == chanceS:
            medChance = chanceP

        if least_common == "rock" and most_common == "paper":
            common = "scissors"
        if least_common == "paper" and most_common == "scissors":
            common = "rock"
        if least_common == "rock" and most_common == "scissors":
            common = "paper"
        choose = random.randint(1, epochs)
        # Change the amount of `if` statements depending on the epochs.
        if choose == 1:
            print(f"AI's Play: {most_common}")
            aiplay = choose
        if choose == 2:
            print(f"AI's Play: {most_common}")
            aiplay = choose
        if choose == 3:
            print(f"AI's Play: {most_common}")
            aiplay = choose
        if choose == 4:
            print(f"AI's Play: {most_common}")
            aiplay = choose
        if choose == 5:
            print(f"AI's Play: {most_common}")
            aiplay = choose
        if choose == 6:
            print(f"AI's Play: {most_common}")
            aiplay = choose
        if choose == 7:
            print(f"AI's Play: {common}")
            aiplay = choose
        if choose == 8:
            print(f"AI's Play: {common}")
            aiplay = choose
        if choose == 9:
            print(f"AI's Play: {common}")
            aiplay = choose
        if choose == 10:
            print(f"AI's Play: {common}")
            aiplay = choose
        if choose == 11:
            print(f"AI's Play: {least_common}")
            aiplay = choose
        if choose == 12:
            print(f"AI's Play: {least_common}")
            aiplay = choose


branch.learn()

loops = int(input("How many rounds would you like to play?: "))

def mainGame():
    aiScore = 0
    playerScore = 0
    name = input("Enter your name: ")
    if name == "":
        name = "Player"

    print(f"AI vs {name}")
    play = input("Now's your time to shine! Rock, paper or scissors?: ")
    # ROCK SECTION
    if play.lower() == "rock":
        print("Your Play: Rock")
        branch.think()
        # IF THE PLAY IS ROCK:
        if aiplay == "rock":
            print("DRAW!")
            print(f"{aiScore} - {playerScore}")
        if aiplay == "paper":
            print("AI wins!")
            aiscore += 1
            print(f"{aiScore} - {playerScore}")
        if aiplay == "scissors":
            print("{name} wins!")
            playerScore += 1
            print(f"{aiScore} - {playerScore}")
            print(f"{aiScore} - {playerScore}")
    if play.lower() == "paper":
        print("Your Play: Paper")
        branch.think()
        # IF THE PLAY IS PAPER:
        if aiplay == "rock":
            print("{name} wins!")
            playerScore += 1
            print(f"{aiScore} - {playerScore}")
        if aiplay == "paper":
            print("DRAW!")
            print(f"{aiScore} - {playerScore}")
        if aiplay == "scissors":
            print("AI wins!")
            aiScore += 1
    if play.lower() == "scissors":
        print("Your Play: Scissors")
        branch.think()
        # IF THE PLAY IS SCISSORS:
        if aiplay == "rock":
            print("AI wins!")
            aiScore += 1
            print(f"{aiScore} - {playerScore}")
        if aiplay == "paper":
            print("{name} wins!")
            playerScore += 1
            print(f"{aiScore} - {playerScore}")
        if aiplay == "scissors":
            print("DRAW!")
            print(f"{aiScore} - {playerScore}")

for i in range(loops):
    mainGame()
