import pandas as pd
from helper import read_file

# file_path = 'input.txt'
file_path = 'test_input.txt'

lines = read_file(file_path = file_path)

list_of_hands = {x.split()[0]:int(x.split()[1]) for x in lines}
print(f'list_of_hands: {list_of_hands}')

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456



first_key, first_value = next(iter(list_of_hands.items()))

def get_draw_rank(draw):

    card_types = {
    (5,): 7,
    (4,1): 6,
    (3,2): 5,
    (3,1,1): 4,
    (2,2,1):3,
    (2,1,1,1): 2,
    (1,1,1,1,1): 1
    }

    temp = dict()
    for card in draw:
        if card in temp:
            temp[card] += 1
        else:
            temp[card] = 1
    sorted_dict = dict(sorted(temp.items(), key=lambda item: item[1], reverse=True))
    values_tuple = tuple(sorted_dict.values())
    return card_types[values_tuple]

def sort_hands_by_type(list_of_hands):
    draws_ranked_by_type = dict()
    for draw in list_of_hands:
        draw_rank = get_draw_rank(draw)
        draws_ranked_by_type[draw] = draw_rank
    return dict(sorted(draws_ranked_by_type.items(), key=lambda item: item[1]))

def create_type_clusters(draws_ranked_by_type):
    same_rank_type_clusters = dict()
    for key in draws_ranked_by_type:
        if draws_ranked_by_type[key] in same_rank_type_clusters:
            same_rank_type_clusters[draws_ranked_by_type[key]].append(key)
        else:
            same_rank_type_clusters[draws_ranked_by_type[key]] = [key]
    return same_rank_type_clusters


draws_ranked_by_type = sort_hands_by_type(list_of_hands)
# print(f'The rank for draw {draw} is: {draw_rank}')
print(f'draws_ranked_by_type: {draws_ranked_by_type}')

same_rank_type_clusters = create_type_clusters(draws_ranked_by_type)
print(f'same_rank_type_clusters: {same_rank_type_clusters}')


#-------------------------------------------------------------------------
cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
card_strength = dict()

for i in range(len(cards)):
    card_strength[cards[i]] = len(cards) - i
# print(card_strength)
#-------------------------------------------------------------------------

final_sorted_cluster = []
for key in same_rank_type_clusters:
    list_to_sort = same_rank_type_clusters[key]

    temp = dict()
    for draw in list_to_sort:
        draw_score = 0
        for i in range(5):
            draw_score +=card_strength[draw[i]]*(13**(4-i))
            # print(f'Card: {draw[i]} with score {card_strength[draw[i]]*(10**(4-i))}', end=' ')
        temp[draw] = draw_score
    temp = dict(sorted(temp.items(), key=lambda item: item[1]))

    sorted_cluster = []
    for key in temp:
        sorted_cluster.append(key)

    final_sorted_cluster += sorted_cluster


print(f'final_sorted_cluster: {final_sorted_cluster}')

total_score = 0
for i in range(len(final_sorted_cluster)):
    # print(final_sorted_cluster[i], draws_ranked_by_type[final_sorted_cluster[i]],(i+1),list_of_hands[final_sorted_cluster[i]])
    total_score += (i+1)*list_of_hands[final_sorted_cluster[i]]

print(total_score)

# PART 1

# PART 2
