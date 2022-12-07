# https://adventofcode.com/2022/day/2
# The elves are having a rock paper scissors contest and you have been given a encrypted strategy guide (the input) for your help with the rations
# the first value of each line is the opponents planned move, second is the move the guide suggests,
# you get points for which gesture you choose [1 - rock, 2 - paper, 3 - scissors] and the outcome of each bout [0 - loss, 3 - tie, 6 - win]
# calculate the points you would get if you were to follow the strategy guide.


def decrypt_strategy(opponent_gesture, player_gesture):
    if opponent_gesture == "A":
        decrypted_opponent = "Rock"
    elif opponent_gesture == "B":
        decrypted_opponent = "Paper"
    elif opponent_gesture == "C":
        decrypted_opponent = "Scissors"
    else:
        raise ValueError(f"{opponent_gesture} does not decrypt into a gesture")

    if player_gesture == "X":
        decrypted_player = "Rock"
    elif player_gesture == "Y":
        decrypted_player = "Paper"
    elif player_gesture == "Z":
        decrypted_player = "Scissors"
    else:
        raise ValueError(f"{player_gesture} does not decrypt into a gesture")

    return decrypted_opponent, decrypted_player

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


with open("input/day2.txt", "r") as f:
    points = 0
    for line in f.readlines():
        gestures = line.split()
        opponent_gesture, player_gesture = decrypt_strategy(gestures[0], gestures[1])
        points += rock_paper_scissors(opponent_gesture, player_gesture)
print(points) # 15422 points
