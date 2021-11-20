import random

def oneTurn():
    turnTotal = 0
    while turnTotal < 20:
        roll = random.randint(1, 6)
        print("Roll: {}".format(roll))
        if roll == 1:
            turnTotal = 0
            break
        turnTotal += roll
    print("Turn total: {}".format(turnTotal))

def holdAt20():
    score = {0: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0}
    simulations = int(input("How many Hold-at-20 turn simulations? "))
    for _ in range(simulations):
        turnTotal = 0
        while turnTotal < 20:
            roll = random.randint(1, 6)
            if roll == 1:
                turnTotal = 0
                break
            turnTotal += roll
        score[turnTotal] += 1
    print("Score \t Estimated Probability")
    for key, item in score.items():
        print("{} \t {}".format(key, item / simulations))

def holdAtX():
    score = {0: 0}
    simulations = int(input("How many Hold-at-20 turn simulations? "))
    hold = int(input("Specify hold value: "))
    for _ in range(simulations):
        turnTotal = 0
        while turnTotal < hold:
            roll = random.randint(1, 6)
            if roll == 1:
                turnTotal = 0
                break
            turnTotal += roll
        if turnTotal in score:
            score[turnTotal] += 1
        else:
            score[turnTotal] = 1
    print("The probability of reaching 100 is {:.4f}".format(1 - (score[0] / simulations)))

def holdAt20GoalTurn():
    score = int(input("Score? "))
    turnTotal = 0
    while turnTotal < 20:
        roll = random.randint(1, 6)
        print("Roll: {}".format(roll))
        if roll == 1:
            turnTotal = 0
            break
        turnTotal += roll
        if score + turnTotal >= 100:
            break
    print("Turn total: {}".format(turnTotal))
    print("New score: {}".format(score + turnTotal))

def holdAt20GoalGame():
    score = 0
    while score < 100:
        turnTotal = 0
        while turnTotal < 20:
            roll = random.randint(1, 6)
            print("Roll: {}".format(roll))
            if roll == 1:
                turnTotal = 0
                break
            turnTotal += roll
            if score + turnTotal >= 100:
                break
        score += turnTotal
        print("Turn total: {}".format(turnTotal))
        print("New score: {}".format(score))

def averageTurns():
    simulations = int(input("Games? "))
    numTurns = 0
    for _ in range(simulations):
        score = 0
        while score < 100:
            turnTotal = 0
            while turnTotal < 20:
                roll = random.randint(1, 6)
                if roll == 1:
                    turnTotal = 0
                    break
                turnTotal += roll
                if score + turnTotal >= 100:
                    break
            score += turnTotal
            numTurns += 1
    print("Average turns: {}".format(numTurns / simulations))

def computerVSComputer():
    playerScores = {1: 0, 2: 0}
    p1Turn = True
    while playerScores[1] < 100 and playerScores[2] < 100:
        player = 1 if p1Turn else 2
        print("Player 1 score: {}".format(playerScores[1]))
        print("Player 2 score: {}".format(playerScores[2]))
        print("It is player {}'s turn.".format(player))
        turnTotal = 0
        while turnTotal < 20:
            roll = random.randint(1, 6)
            print("Roll: {}".format(roll))
            if roll == 1:
                    turnTotal = 0
                    break
            turnTotal += roll
            if playerScores[player] + turnTotal >= 100:
                break
        playerScores[player] += turnTotal
        print("Turn total: {}".format(turnTotal))
        print("New score: {}".format(playerScores[player]))
        p1Turn = not p1Turn

def playerVSComputer():
    user = random.randint(1, 2)
    print("You will be player {}.".format(user))
    print("Enter nothing to roll; enter anything to hold.")
    playerScores = {1: 0, 2: 0}
    p1Turn = True
    while playerScores[1] < 100 and playerScores[2] < 100:
        player = 1 if p1Turn else 2
        print("Player 1 score: {}".format(playerScores[1]))
        print("Player 2 score: {}".format(playerScores[2]))
        print("It is player {}'s turn.".format(player))
        turnTotal = 0
        if player != user:
            while turnTotal < 20:
                roll = random.randint(1, 6)
                print("Roll: {}".format(roll))
                if roll == 1:
                        turnTotal = 0
                        break
                turnTotal += roll
                if playerScores[player] + turnTotal >= 100:
                    break
        else:
           STDin = ""
           while STDin == "":
                roll = random.randint(1, 6)
                print("Roll: {}".format(roll))
                if roll == 1:
                        turnTotal = 0
                        break
                turnTotal += roll
                print("Turn total: {} ".format(turnTotal), end="")
                STDin = input("Roll/Hold? (Enter)")
        playerScores[player] += turnTotal
        print("Turn total: {}".format(turnTotal))
        print("New score: {}".format(playerScores[player]))
        p1Turn = not p1Turn
    print('\033[2;31;43m Player {} wins with {}:{} points! \033[0;0m'.format(2 if p1Turn else 1, playerScores[2 if p1Turn else 1], playerScores[1 if p1Turn else 2]))
        


#init
# oneTurn()
# holdAt20()
holdAtX()
# holdAt20GoalTurn()
# holdAt20GoalGame()
# averageTurns()
# computerVSComputer()
# playerVSComputer()

