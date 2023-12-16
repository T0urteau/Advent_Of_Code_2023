import sys
import re

with open('aoc07_input.txt') as f:
    f = re.sub((' +')," ",f.read())

card_val_p1 = {"A":12, "K":11, "Q":10, "J":9, "T":8, "9":7, "8":6, "7":5, "6":4, "5":3, "4":2, "3":1, "2":0}
card_val_p2 = {"A":12, "K":11, "Q":10, "T":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1, "J":0}


def convert_to_base_10(hand, val_dict = card_val_p1):
    val = 0
    for c in range(len(hand)):
        val += val_dict[hand[c]]*pow(13, len(hand)-1-c)
    return val


def typeValue(hand, val_dict = card_val_p1, joker = False):
    hand_cards = [0] * 13
    type = 0

    for c in hand:
        hand_cards[val_dict[c]] += 1

    if(joker):
        bonus = hand_cards[val_dict["J"]]
        hand_cards[val_dict["J"]] = 0
        hand_cards = sorted(hand_cards, key=lambda x: x, reverse=True)
        hand_cards[0] += bonus
    else : hand_cards = sorted(hand_cards, key=lambda x: x, reverse=True)

    if(hand_cards[0] == 1):return "2" #HighCard
    if(hand_cards[0] == 2 and  hand_cards[1] == 1):return "3" #Pair
    if(hand_cards[0] == 2 and  hand_cards[1] == 2):return "4" #DoublePair
    if(hand_cards[0] == 3 and  hand_cards[1] == 1):return "5" #Three of a kind
    if(hand_cards[0] == 3 and  hand_cards[1] == 2):return "6" #Full
    if(hand_cards[0] == 4):return "7" #Four
    if(hand_cards[0] == 5):return "8" #Five
    return False



def part1(input):
    ans = 0

    cards = [val.split(' ') for val in f.rstrip().split("\n")]
    for n in range(len(cards)):
        cards[n] = [convert_to_base_10(typeValue(cards[n][0])+cards[n][0]), int(cards[n][1])]

    cards = sorted(cards, key=lambda x: x[0])

    for n in range(len(cards)):
        ans += (cards[n][1]*(n+1))
    
    return("Part 1: " + str(ans))


def part2(input):
    ans = 0

    cards = [val.split(' ') for val in f.rstrip().split("\n")]
    for n in range(len(cards)):
        cards[n] = [convert_to_base_10(typeValue(cards[n][0], card_val_p2, True)+cards[n][0], card_val_p2), int(cards[n][1])]

    cards = sorted(cards, key=lambda x: x[0])

    for n in range(len(cards)):
        ans += (cards[n][1]*(n+1))
    
    return("Part 2: " + str(ans))

print(part1(f))
print(part2(f))



    