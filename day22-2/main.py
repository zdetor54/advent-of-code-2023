import pandas as pd
from helper import read_file

file_path = 'input.txt'
# file_path = 'test_input.txt'

rounds = read_file(file_path = file_path)


def check_round(player1, player2):
    lose = ['AZ', 'BX', 'CY']
    draw = ['AX', 'BY', 'CZ']
    win = ['AY', 'BZ', 'CX']

    win_score = 0
    if player1+player2 in win:
        win_score += 6
    elif player1+player2 in draw:
        win_score += 3

    return(ord(player2)-87+win_score)

def check_round2(player1, player2):
    lose = ['AZ', 'BX', 'CY']
    draw = ['AX', 'BY', 'CZ']
    win = ['AY', 'BZ', 'CX']

    if player2 == 'X':
        win_score = 0
        for combo in lose:
            if combo[0] == player1:
                player2 = combo[1]
    elif player2 == 'Y':
        win_score = 3
        for combo in draw:
            if combo[0] == player1:
                player2 = combo[1]
    elif player2 == 'Z':
        win_score = 6
        for combo in win:
            if combo[0] == player1:
                player2 = combo[1]

    return(ord(player2)-87+win_score)

total_score = 0
for round in rounds:
    # print(round[0], round[2])
    # print(check_round(round[0], round[2]))
    total_score += check_round2(round[0], round[2])

print(total_score)