import random


### BUGS TO FIX:
# paper and scissors player choices cause the result to return 3 extra times, and not print the updated win count, nor update the numbers. --DONE
# "incorrect input" function is no longer working, instead of always activating. --DONE
#  after using an incorrect input, only asks for a new one but doesnt apply it -- DONE

def intToRPS(randomint):
    answer = ""
    if randomint == 1:
        answer = "Rock"
    elif randomint == 2:
        answer = 'Paper'
    elif randomint == 3:
        answer = "Scissors"
    return answer

def whoWins(comp, player):      # takes the variable 'comp' that comes from intToRPS() and variable 'player' from playerChoice() and returns the winner of the game
    answer = ''
    
    if comp == "Rock":
        if player == "Rock":
            answer = "It's a tie!"
        elif player == "Paper":
            answer = "Player wins!"
        elif player == "Scissors":
            answer = "Player loses!"
    elif comp == "Paper":
        if player == "Rock":
            answer = "Player loses!"
        elif player == "Paper":
            answer = "It's a tie!"
        elif player == "Scissors":
            answer = "Player wins!"
    elif comp == "Scissors":
        if player == "Rock":
            answer = "Player wins!"
        elif player == "Paper":
            answer = "Player loses!"
        elif player == "Scissors":
            answer = "It's a tie!"
    return answer

def playerChoice():         ##This allows the player to input their own choice and holds it in the variable p to use later.
    p = input(str("Rock, Paper, or Scissors?"))
    p = p.capitalize()
    #return p
    if p != "Rock" and p != "Paper" and p != "Scissors":
        print("Incorrect input.")
        return(playerChoice())
    else:
       return(p)

def main():
    count = 0
    countlose = 0
    countTie = 0
    op = random.randint(1, 3)

    player = playerChoice()
    cpu = intToRPS(op)
    print("Computer chose:", cpu)

    print(whoWins(cpu, player))
    if whoWins(cpu, player) == "Player wins!":
        count += 1
        print("Player wins:", count, ",", "Player losses:", countlose, ",", "Ties:", countTie)
    elif whoWins(cpu, player) == "Player loses!":
        countlose += 1
        print("Player wins:", count, ",", "Player losses:", countlose, ",", "Ties:", countTie)
    elif whoWins(cpu, player) == "It's a tie!":
        countTie += 1
        print("Player wins:", count, ",", "Player losses:", countlose, ",", "Ties:", countTie)

    
    while input("Play again? (Y/N) ").upper() == "Y":
        op = random.randint(1, 3)

        player = playerChoice()
        cpu = intToRPS(op)
        print("Computer chose:", cpu)

        print(whoWins(cpu, player))
        if whoWins(cpu, player) == "Player wins!":
            count += 1
            print("Player wins:", count, ",", "Player losses:", countlose, ",", "Ties:", countTie)
        elif whoWins(cpu, player) == "Player loses!":
            countlose += 1
            print("Player wins:", count, ",", "Player losses:", countlose, ",", "Ties:", countTie)
        elif whoWins(cpu, player) == "It's a tie!":
            countTie += 1
            print("Player wins:", count, ",", "Player losses:", countlose, ",", "Ties:", countTie)



if __name__ == "__main__":
    main()

