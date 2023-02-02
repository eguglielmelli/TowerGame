import random


def instructions():
    # '''This function returns the instructions for the game'''
    instruct = "\nWelcome to Tower Blaster! Tower Blaster is a game that involves rearranging bricks in order to build a sequence of ascending numbers.\nTower Blaster is often played with 2 human players, but we will keep this simple and just play the user versus the computer.\nYou will first be given a brick from the discard pile, and you may choose to use this brick if you want to replace it with another in your tower.\nHowever, if you do not use it, you can choose to draw a random brick from the main pile. You may choose to replace a brick in your tower with it, but \ndeclining the main pile brick ends your turn.\nThe first player to get a sequence of ascending numbers wins. Good Luck!"
    return instruct


def setup_bricks():
    '''This function returns a tuple with integers from 1-60 and an empty list'''
    main_pile = [i for i in range(1, 61)]
    discard_pile = []
    return (main_pile, discard_pile)


def shuffle_bricks(bricks):
    """This function shuffles the given bricks"""
    bricks = [i for i in range(1, 61)]
    random.shuffle(bricks)


def check_bricks(main_pile, discard_pile):
    """Check if there are any bricks left in the given main pile of bricks. If not, shuffle the discard pile (using the shuffle function) and move those bricks to the
main pile. Then turn over the top brick to be the start of the new discard pile."""
    if len(main_pile) == 0: # checks if main pile is empty
        random.shuffle(discard_pile) #shuffles discard
        main_pile[0:] = discard_pile
        discard_pile.clear()
        add_brick_to_discard(get_top_brick(main_pile), discard_pile)
    return (main_pile, discard_pile)


def check_tower_blaster(tower):
    """This function checks the user or computer's tower to see if stability (bricks in ascending order) has been achieved"""
    if tower == sorted(tower):
        return True
    else:
        return False


def get_top_brick(brick_pile):
    """Remove the top brick from a given pile and returns the first element of a given list"""
    top_brick = brick_pile.pop(0)
    return int(top_brick)


def deal_initial_bricks(main_pile):
    """This function assigns 10 bricks to both the computer and human, with the computer going first"""
    human_pile = []
    computer_pile = []
    for i in range(10):
        computer_pile.insert(0, main_pile.pop(0))
        human_pile.insert(0, main_pile.pop(0))

    return (computer_pile, human_pile)


def add_brick_to_discard(brick, discard_pile):
    """add the top brick given to the top of the given discard pile"""
    int(brick)
    discard_pile.insert(0, brick)


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard_pile):
    """finds the given brick to be replaced in given tower and replace it with new brick, checks if brick is in tower, gets put on top of discard pile, and then returns True if it is replaced or false if it is not"""
    if brick_to_be_replaced in tower: #checks that brick to be replaced is in tower
        position = tower.index(brick_to_be_replaced)  # finds the index of brick to be replaced
        add_brick_to_discard(tower[position], discard_pile)  # takes the replaced brick and puts it in discard pile
        tower[position] = new_brick
        return True
    else:
        return False


def computer_play(tower, main_pile, discard_pile):
    """This function determines the computer's strategy and the programmer is responsible for how the computer works. The computer will begin with reading its first brick and
    if the discard brick is less than or equal to 10, then it will replace that brick with the first brick in the list. If the discard brick is greater than 10, it will pull from the main pile
    and follow a similar strategy. If not those two conditions, then the computer will pull each brick and compare each index with one another and replace
    them accordingly in order to create the sorted tower."""


    if tower[0] % 2 == 0: # if the first index number is even, and the discard pile is less than or equal to tower[0], then replace the first brick in the tower
        brick_1 = get_top_brick(discard_pile) #top of discard pile
        if brick_1 < tower[0]:
                find_and_replace(brick_1, tower[0], tower, discard_pile)
                print("The computer used",brick_1,"from the discard pile.")
        else:
            brick_2 = get_top_brick(main_pile) # get brick from main if above criteria is not met

            if brick_2 <= 10: # if the main pile brick is less than or equal to 10, replace the first brick in the tower
                find_and_replace(brick_2, tower[0], tower, discard_pile)
                print("The computer used",brick_2,"from the main pile.")
            else:
                add_brick_to_discard(brick_2, discard_pile) # if neither condition, then put the brick from main into discard

    return tower


def replace_bricks(number, user_pile, discard_pile):
    """This function is used to replace the given brick in the users tower, if the inputted number is not in their tower, it outputs a message accordingly."""
    brick_replace = input("Please select the brick you want to replace in your tower:") #user selects brick
    check_number = [str(i) for i in range(1, 61)] #set critera for brick to be between 1-60
    while brick_replace not in check_number:  # if the brick is not between 1 and 60, this will say invalid
        brick_replace = input("This value is not in the range. Try again.")
    brick_replace = int(brick_replace)
    while not (find_and_replace(number, brick_replace, user_pile,discard_pile)):  # if brick is not in the tower, this will output to user
        print("Brick does not exist in your tower.")
        brick_replace = int(input("Where do you want to place this brick? Type a brick number to replace in your tower:"))
        continue
    return user_pile


def user_input(user_choice, tower, main_pile, discard_pile):
    """This function evaluates user input and allows them to answer whether discard/main pile and if they want to use the given number"""
    while user_choice.upper() != "D" and user_choice.upper() != "M": #user must input m/M or d/D
        user_choice = input("That is invalid. Please enter D/M")

    if user_choice.upper() == "D": #allows the user to start replacing bricks when they input D/d to use the discard pile number
        num = get_top_brick(discard_pile)
        tower = replace_bricks(num, tower, discard_pile)

    elif user_choice.upper() == "M": #pulls from main pile
        num = get_top_brick(main_pile)
        print("The number pulled from the main pile is " + str(num) + ".")
        choice = input("Would you like to use " + str(num) + "." + " " + "Enter y/n.")
        while choice.upper() != "Y" and choice.upper() != "N":
            choice = input("That is invalid. Please enter y/n") #user must enter y/n
        if choice.upper() == "N":  # this skips the users turn and adds the brick from the main pile to discard
            add_brick_to_discard(num, discard_pile)
        elif choice.upper() == "Y":  # if yes, this prompts the replace bricks function
            tower = replace_bricks(num, tower, discard_pile)

    return tower


def main():
    pass
    print()
    print(instructions())
    print()
    print("Let's play the game!")

    main_pile = [i for i in range(1, 61)]
    computer_tower = []
    user_tower = []
    discard_pile = []

    random.shuffle(main_pile)
    user_tower, computer_tower = deal_initial_bricks(main_pile)  # gives the first lists to computer and user

    discard_pile.append(get_top_brick(main_pile))  # takes first brick from main and puts into discard

    print("Computer Tower:", computer_tower)
    print("Your tower:", user_tower)

    while True:  # continuously runs the code while neither player has won
        print()
        check_bricks(main_pile, discard_pile)
        print("The computer will be taking it's turn now.")
        print()
        computer_play(computer_tower,main_pile,discard_pile)
        print()
        print("Your tower:", user_tower)

        if check_tower_blaster(computer_tower):  # code block for when computer wins
            print()
            print("The computer has won.")
            print()
            print("The computer's tower:", computer_tower)
            print()
            print("Your tower:", user_tower)
            break

        else:  # code block shows top brick in discard pile, and takes user input to potentially replace bricks
            print()
            print("It is your turn now.")
            print()
            discard_top = discard_pile[0]
            #discard_pile_number = discard_pile[0]
            print("The top brick from the discard pile is " + "" + str(discard_top))
            user_choice = input("Type 'D' to take the discard brick, 'M' for a mystery brick.")
            user_tower = user_input(user_choice, user_tower, main_pile, discard_pile)

            if check_tower_blaster(user_tower) == True: #if user has won the game, this will break the above code block and end the game
                print("Your tower is:", user_tower)
                print()
                print("The computer's tower:", computer_tower)
                print()
                print("You won the game.")
                break

            print()


if __name__ == "__main__":
    main()
