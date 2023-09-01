from flask import Flask, render_template, request, session, redirect, url_for
import random
import time

app = Flask(__name__)
app.secret_key = "your_secret_key"

POSSIBLE_DICES = {
    "D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100",
}

def dice_roll(dice_value):
    return random.randint(1, dice_value)

@app.route("/", methods=["GET", "POST"])
def game():
    if "user_points" not in session:
        session["user_points"] = 0
    if "comp_points" not in session:
        session["comp_points"] = 0
    #Sessions are used to keep current points visible for the User

    user_points = session["user_points"]
    comp_points = session["comp_points"]
    user_result = ""
    user_result_2 = ""
    comp_result = ""
    comp_result_2 = ""
    result = ""
    game_over = False #The variable helps show a final message when changed to True.

    if request.method == "POST":
        roll_button = request.form['roll_button']
        if not game_over:
            if roll_button == "Roll Dice":
                chosen_dice = request.form.get("dice_type")
                user_roll = dice_roll(int(chosen_dice[1:]))
                user_result = f"Your 1st roll is: {user_roll}"

                chosen_dice_2 = request.form.get("dice_type_2")
                user_roll_2 = dice_roll(int(chosen_dice_2[1:]))
                user_result_2 = f"Your 2nd roll is: {user_roll_2}"

                comp_dice_code = random.choice(list(POSSIBLE_DICES))
                comp_roll = dice_roll(int(comp_dice_code[1:]))
                comp_result = f"Comp 1st roll: {comp_roll}"

                comp_dice_code_2 = random.choice(list(POSSIBLE_DICES))
                comp_roll_2 = dice_roll(int(comp_dice_code_2[1:]))
                comp_result_2 = f"Comp 2nd roll: {comp_roll_2}"
            #"Roll Dice" button service (the User's choosing 2 specific dice)

            if roll_button == "Roll Random Dice":
                chosen_dice = random.choice(list(POSSIBLE_DICES))
                user_roll = dice_roll(int(chosen_dice[1:]))
                user_result = f"Your 1st roll is: {user_roll}"

                chosen_dice_2 = random.choice(list(POSSIBLE_DICES))
                user_roll_2 = dice_roll(int(chosen_dice_2[1:]))
                user_result_2 = f"Your 2nd roll is: {user_roll_2}"

                comp_dice_code = random.choice(list(POSSIBLE_DICES))
                comp_roll = dice_roll(int(comp_dice_code[1:]))
                comp_result = f"Comp 1st roll: {comp_roll}"

                comp_dice_code_2 = random.choice(list(POSSIBLE_DICES))
                comp_roll_2 = dice_roll(int(comp_dice_code_2[1:]))
                comp_result_2 = f"Comp 2nd roll: {comp_roll_2}"
            #"Roll Random Dice" button service (the User can use random dice)

            user_points += user_roll + user_roll_2
            comp_points += comp_roll + comp_roll_2

            if user_roll == 7:
                user_points = user_points // 7
            if user_roll == 11:
                user_points = user_points * 11

            if user_roll_2 == 7:
                user_points = user_points // 7
            if user_roll_2 == 11:
                user_points = user_points * 11

            if comp_roll == 7:
                comp_points = comp_points // 7
            if comp_roll == 11:
                comp_points = comp_points * 11

            if comp_roll_2 == 7:
                comp_points = comp_points // 7
            if comp_roll_2 == 11:
                comp_points = comp_points * 11
            #Concept to calculate two unique numbers - 7 and 11

            if user_points >= 2001 and comp_points >= 2001:
                result = "It's a draw"
                game_over = True

            if user_points >= 2001:
                result = "You won!"
                game_over = True
            if comp_points >= 2001:
                result = "The computer won!"
                game_over = True
            #End-of-game messages

            if game_over:
                session["user_points"] = 0
                session["comp_points"] = 0
            else:
                session["user_points"] = user_points
                session["comp_points"] = comp_points

    return render_template('main_page.html',
                           user_result=user_result,
                           user_result_2=user_result_2,
                           comp_result=comp_result,
                           comp_result_2=comp_result_2,
                           result=result,
                           user_points=user_points,
                           comp_points=comp_points,
                           game_over=game_over)

@app.route("/reset", methods=["POST"])
def reset_session():
    session.clear()
    time.sleep(0.1)
    return redirect(url_for('game'))
#Session reset - redirecting to url from game function

if __name__ == "__main__":
    app.run(debug=True)
