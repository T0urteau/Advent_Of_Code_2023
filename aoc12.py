import re

def get_pattern(n):
    regex = '^([?#]{'+str(n)+'})[^#]|^([?#]{'+str(n)+'})$|[^#]([?#]{'+str(n)+'})[^#]|[^#]([?#]{'+str(n)+'})$' #4 regex together !
    return re.compile(regex)

#For each possible position of spring call themselve who will handle next spring until all springs are tested, for each last spring who can be positionned : possibilities ++
def find_all_possibilities(n, string):
    ans = 0
    match = re.search(get_pattern(springs[n]), string) #Search springs[n] in string modified to keep only space possible

    while True:
        if match:
            for i in range(1,5): #If match, search the span of the match
                if match.group(i):
                    new_string = string[match.end():] #cut string and keep only space where next springs can be
                    if(string[match.start(i)] == "#"):
                        string = ''
                    else: 
                        string = string[match.start(i)+1:]

            if n < len(springs)-1: #If not last spring recursive for finding next springs position
                ans += find_all_possibilities(n+1, new_string)
            else:
                ans += 1

            match = re.search(get_pattern(springs[n]), string)
        else:
            break
    return ans

with open('aoc12_input.txt') as f:
    f = [val for val in f.read().rstrip().split("\n")]
    f = [val.split(" ") for val in f]
    f = [[val[0],[int(v) for v in val[1].split(',')]] for val in f]

    ans = 0

    for line in f:

        row = line[0]
        springs = line[1]
        
        ans += find_all_possibilities(0, row)

    print('Part1: '+str(ans))

