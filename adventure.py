import time
import random


WIN_CHANCE_WEAPON = 0.8
WIN_CHANCE_BAREHAND = 0.3


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers." )
    print_pause(
        f"Rumor has it that a {enemy} is somewhere around here,"
        f"and has been terrifying the nearby village."
    )
    print_pause(f"In your hand you hold your trusty {weapon}.")


def valid_input(prompt,option1,option2):
    while True:
        response = input(prompt).lower()
        if response == option1:
            return response
        elif response == option2:
            return response
        else:
            print_pause("Sorry, I don't understand.")


def win():
    print_pause("Congratulation! You're the super star⭐️")
    playagain = valid_input("Would you lime to play again? (y/n)", "y", "n")
    if "y" in playagain:
        return True
    elif "n" in playagain:
        return False


def lose():
    print_pause("GAME OVER")
    playagain = valid_input("Would you lime to play again? (y/n)", "y", "n")
    if "y" in playagain:
        return True
    elif "n" in playagain:
        return False
    
def fight(weapon):
    print_pause(f"Now the {enemy} came against you...!")
    print_pause(f"Would you like to use your weapon {weapon}")
    print_pause("Enter 1 to use.")
    print_pause("Enter 2 not to use, instead fight by yourself.")
    response = valid_input("(Please enter 1 or 2)", "1", "2")
    if "1" in response: 
        if random.random() < WIN_CHANCE_WEAPON:
            return win()
        else:
            print_pause(f"Your {weapon} got broken and defeated")
            return lose()
    elif "2" in response: 
        if random.random() < WIN_CHANCE_BAREHAND:
            print_pause("Fantastic! You defeted the enemy by your body!")
            return win()
        else:
            return lose()

def where_to():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would like to do?")
    response = valid_input("(Please enter 1 or 2.)", "1", "2")
    if "1" in response:
        return house()
    elif "2" in response:
        return cave()

def house():
    print_pause(f"You enter the house and found the {enemy}")
    print_pause("Would you like to fight or escape?")
    print_pause("Enter 1 to fight.")
    print_pause("Enter 2 to escape.")
    response = valid_input("(Please enter 1 or 2.)", "1", "2")
    if "1" in response:
        return fight(weapon)
    if "2" in response:
        return field()

def field():
    print_pause("Again you find yourself standing in an open field, filled with grass and yellow wildflowers.")
    return where_to()


def cave():
    print_pause(f"You enter the cave and found the {enemy}")
    print_pause("Would you like to fight or escape?")
    print_pause("Enter 1 to fight.")
    print_pause("Enter 2 to escape.")
    response = valid_input("(Please enter 1 or 2.)", "1", "2")
    if "1" in response:
        return fight(weapon)
    if "2" in response:
        return field()
    

def play_one_game():
    global enemy,weapon
    enemies = ['ninja', 'ochimusha', 'pirate', 'geisha', 'bear']
    enemy = random.choice(enemies)
    weapons = ['sord', 'dagger', 'rope', 'magic band']
    weapon = random.choice(weapons)
    cave_visited = False

    intro()
    return where_to()


while True:
    should_play_again = play_one_game()

    if not should_play_again:
        print_pause("Thank you for playing!")
        break