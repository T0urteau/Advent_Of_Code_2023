import re

result = 0

with open('aoc04_input.txt') as input_file:

    input_file = input_file.readlines()
    cards = [1] * len(input_file)


    for n in range(len(input_file)):
        line = input_file[n]
        win = 0

        line = line.split(":")
        line.pop(0)
        line = line[0][:-1].split("|")

        win_nb = re.sub(' +', ' ', line[0].strip()).split(" ")
        play_nb = re.sub(' +', ' ', line[1].strip()).split(" ")

        for winner in win_nb:
            if winner in play_nb:
                win += 1

        if win > 0:
            for x in range(1,win+1):
                cards[n+x] += cards[n]

        win = 0
    
    print(cards)
    for n in cards:
        result += n

    print(result)
        
