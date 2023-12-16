import math
import re


def find_gcd(x, y):
    while(y):
        x, y = y, x % y
 
    return x


def equal(arr):
    for n in range(1,len(arr)):
        if arr[n][0] != arr[0][0]: return False
    return True


def end(word):
    return(bool(re.search('^[A-Z]{2}Z', word[0])))

def loop(arr):
    if arr[0] == arr[1]:
        print(str(arr[0])+" "+str(arr[1]))
    return(arr[0] == arr[1])

with open('aoc08_input.txt') as f:
    f = re.sub((' +')," ",f.read())

    instruction, map = [val.split("\n") for val in f.rstrip().split("\n\n")]
    instruction = instruction.pop()

    dir_dict = { "L": {}, "R": {}}

    for m in map:
        dir = re.findall('[A-Z]{3}', m)
        dir_dict["L"][dir[0]] = dir[1]
        dir_dict["R"][dir[0]] = dir[2]
    
    step = 'AAA'
    step_nb = 0

    while step != 'ZZZ':
        step = dir_dict[instruction[step_nb%len(instruction)]][step]
        step_nb += 1
    
    print("part 1: "+str(step_nb))

    steps = []
    loop_steps = []

    for m in map: #ON RECUPERE TOUT LES START
        dir = re.findall('^[A-Z]{2}A', m)
        if dir: steps.append(dir[0])

    for n in steps:
        step_nb = 0
        while bool(re.search('^[A-Z]{2}Z', n)) == False:
            n = dir_dict[instruction[step_nb%len(instruction)]][n]
            step_nb += 1
        loop_steps.append(step_nb)

    print("part 2: "+str(math.lcm(*loop_steps)))

    

    



    



    