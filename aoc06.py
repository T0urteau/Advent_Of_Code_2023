import sys
import re

with open('aoc06_input.txt') as f:
    f = re.sub((' +')," ",f.read())

def part1(input):
    ans = 1


    time, distance = [val.split(" ")[1:] for val in f.split("\n")[:2]]
    time = [int(val) for val in time]
    distance = [int(val) for val in distance]

    for n in range(len(time)):
        for i in range(time[n]):
            if (i * (time[n]-i) > distance[n]):
                ans = ans * ((time[n]+1)-(i*2))
                break
    
    return("Part 1:" + str(ans))

def part2(input):
    ans = 1


    time, distance = [val.split(" ")[1:] for val in f.split("\n")[:2]]
    time = int(''.join(time))
    distance = int(''.join(distance))

    for i in range(time):
        if (i * (time-i) > distance):
            ans = ans * ((time+1)-(i*2))
            break
    
    return("Part 2:" + str(ans))

print(part1(f))
print(part2(f))



    