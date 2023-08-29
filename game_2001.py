import random
def game():
    print("""
    Here is a 2001 game.
    We have to fight each other to collect 2001 points faster by using dice.
    Let's begin!
    """)
    user_points = 0
    comp_points = 0
    while user_points <= 100 and comp_points <= 100:
        user_input = input("Press 'Enter' to roll a dice")
        roll_dice = random.randint(1, 12)
        comp_roll_dice = random.randint(1, 12)

        user_points += roll_dice
        comp_points += comp_roll_dice
        print(f"You rolled: {roll_dice}")
        print(f"Your current points: {user_points}")
        print("")
        print(f"I rolled: {comp_roll_dice}")
        print(f"My current points: {comp_points}")
        print("")
        if roll_dice == 7:
            int(user_points) // 7
        if roll_dice == 11:
            int(user_points) * 11

        if comp_roll_dice == 7:
            int(comp_points) // 7
        if comp_roll_dice == 11:
            int(comp_points) * 11

        if user_points >= 100 and comp_points >= 100:
            print("It's a draw")
            break
        if user_points >= 100:
            print("You won! (user)")
        if comp_points >= 100:
            print("I won! (comp)")

game()