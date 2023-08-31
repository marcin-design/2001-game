from flask import Flask, render_template, request, session
import random

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

    user_points = session["user_points"]
    comp_points = session["comp_points"]
    user_result = ""
    user_result_2 = ""
    comp_result = ""
    comp_result_2 = ""
    result = ""

    if request.method == "POST":
        chosen_dice = request.form.get("dice_type")
        user_roll = dice_roll(int(chosen_dice[1:]))
        user_result = f"Your first roll is: {user_roll}"

        chosen_dice_2 = request.form.get("dice_type_2")
        user_roll_2 = dice_roll(int(chosen_dice_2[1:]))
        user_result_2 = f"Your second roll: {user_roll_2}"

        comp_dice_code = random.choice(list(POSSIBLE_DICES))
        comp_roll = dice_roll(int(comp_dice_code[1:]))
        comp_result = f"Comp 1st roll: {comp_roll}"

        comp_dice_code_2 = random.choice(list(POSSIBLE_DICES))
        comp_roll_2 = dice_roll(int(comp_dice_code_2[1:]))
        comp_result_2 = f"Comp 2nd roll: {comp_roll_2}"

        if user_roll == 7:
            user_roll = user_roll // 7
        if user_roll == 11:
            user_roll = user_roll * 11

        if user_roll_2 == 7:
            user_roll_2 = user_roll_2 // 7
        if user_roll_2 == 11:
            user_roll_2 = user_roll_2 * 11

        if comp_roll == 7:
            comp_roll = comp_roll // 7
        if comp_roll == 11:
            comp_roll = comp_roll * 11

        if comp_roll_2 == 7:
            comp_roll_2 = comp_roll_2 // 7
        if comp_roll_2 == 11:
            comp_roll_2 = comp_roll_2 * 11

        user_points += user_roll + user_roll_2
        comp_points += comp_roll + comp_roll_2

        if user_points >= 200 and comp_points >= 200:
            result = "It's a draw"

        elif user_points >= 200:
            result = "You won! (user)"
            session["user_points"] = 0
            session["comp_points"] = 0
        elif comp_points >= 200:
            result = "I won! (comp)"
            session["user_points"] = 0
            session["comp_points"] = 0

        session["user_points"] = user_points
        session["comp_points"] = comp_points

    return render_template('main_page.html',
                           user_result=user_result, user_result_2=user_result_2, comp_result=comp_result, comp_result_2=comp_result_2,
                           result=result,
                           user_points=user_points,
                           comp_points=comp_points)

@app.route("/reset", methods=["POST"])
def reset_session():
    session.clear()
    return "Session reset"

if __name__ == "__main__":
    app.run(debug=True)
