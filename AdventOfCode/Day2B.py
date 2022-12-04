# For part B, the elf that gave you the strategy guide comes back to clarify that the second value on each line indicates how the match
# should end, [X - loss, y - tie, z - win]. With this figure out what moves to make to follow these outcomes, and what will your
# points be at the end using this strategy?


def decrypt_strategy(opponent_gesture, suggested_outcome):
    if opponent_gesture == "A":
        decrypted_opponent = "Rock"
    elif opponent_gesture == "B":
        decrypted_opponent = "Paper"
    elif opponent_gesture == "C":
        decrypted_opponent = "Scissors"
    else:
        raise ValueError(f"{opponent_gesture} does not decrypt into a gesture")

    if suggested_outcome == "X":
        decrypted_outcome = "Lose"
    elif suggested_outcome == "Y":
        decrypted_outcome = "Tie"
    elif suggested_outcome == "Z":
        decrypted_outcome = "Win"
    else:
        raise ValueError(f"{suggested_outcome} does not decrypt into an outcome")

    return decrypted_opponent, decrypted_outcome

def rock_paper_scissors(opponent_gesture, player_gesture):
    if opponent_gesture == "Rock":
        if player_gesture == "Rock":
            points = 4
        elif player_gesture == "Paper":
            points = 8
        elif player_gesture == "Scissors":
            points = 3
    elif opponent_gesture == "Paper":
        if player_gesture == "Rock":
            points = 1
        elif player_gesture == "Paper":
            points = 5
        elif player_gesture == "Scissors":
            points = 9
    elif opponent_gesture == "Scissors":
        if player_gesture == "Rock":
            points = 7
        elif player_gesture == "Paper":
            points = 2
        elif player_gesture == "Scissors":
            points = 6

    return points

def select_gesture(opponent_gesture, suggested_outcome):
    if opponent_gesture == "Rock":
        if suggested_outcome == "Lose":
            selected_gesture = "Scissors"
        elif suggested_outcome == "Tie":
            selected_gesture = "Rock"
        elif suggested_outcome == "Win":
            selected_gesture = "Paper"
    elif opponent_gesture == "Paper":
        if suggested_outcome == "Lose":
            selected_gesture = "Rock"
        elif suggested_outcome == "Tie":
            selected_gesture = "Paper"
        elif suggested_outcome == "Win":
            selected_gesture = "Scissors"
    elif opponent_gesture == "Scissors":
        if suggested_outcome == "Lose":
            selected_gesture = "Paper"
        elif suggested_outcome == "Tie":
            selected_gesture = "Scissors"
        elif suggested_outcome == "Win":
            selected_gesture = "Rock"

    return selected_gesture


with open("input/day2.txt", "r") as f:
    points = 0
    for line in f.readlines():
        gestures = line.split()
        opponent_gesture, suggested_outcome = decrypt_strategy(gestures[0], gestures[1])
        selected_gesture = select_gesture(opponent_gesture, suggested_outcome)
        points += rock_paper_scissors(opponent_gesture, selected_gesture)
print(points) # 15442 points
