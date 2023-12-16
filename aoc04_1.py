import re

result = 0

with open('aoc04_input.txt') as input_file:

    #CHAQUE PARTIE
    for line in input_file:
        win = 0

        #line = line.replace(" ","")
        line = line.split(":")
        line.pop(0)
        line = line[0][:-1].split("|")

        win_nb = re.sub(' +', ' ', line[0].strip()).split(" ")
        play_nb = re.sub(' +', ' ', line[1].strip()).split(" ")



        for winner in win_nb:
            if winner in play_nb:
                win += 1

        if win > 0:
            tmp = 1
            while win > 1:
                tmp = tmp*2
                win -= 1

        result += tmp
        tmp = 0
        win = 0
        
    print(result)
        
