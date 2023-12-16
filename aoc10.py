import re
with open('aoc10_input.txt') as f:
    grid = [val for val in f.read().rstrip().split("\n")]

    start = [0,0]
    all_dir = ["N","S","W","E"]
    
    for i in range(len(grid)): #FIND START
        index = re.search('S', grid[i])
        if(index != None):
            start = [i, index.start()]
            break
    
    dir_dict = {
        "N":[-1,0,"S",1],
        "S":[1,0,"N",4],
        "W":[0,-1,"E",8],
        "E":[0,1,"W",2]
    }



    def isNextValid(dir, pos):
        next_char = getChar(getPos(pos, dir))
        next_dir = findDir(next_char)
        for next in next_dir:
            if next == getOppositeDir(dir):
                return True
        return False

    def getPos(pos, dir):
        return([ pos[0] + dir_dict[dir][0]  , pos[1] + dir_dict[dir][1]   ])
    
    def getChar(pos):
        return(grid[pos[0]] [pos[1]])

    def getOppositeDir(char):
        return dir_dict[char][2]

    def findDir(char):
        if char == "|":
            return(["N","S"])
        if char == "-":
            return(["W","E"])
        if char == "L":
            return(["N","E"])
        if char == "J":
            return(["N", "W"])
        if char == "7":
            return(["W","S"])
        if char == "F":
            return(["E","S"])
        if char == ".":
            return([])
        if char == "S":
            return(["N","S","W","E"])

    def count_enclosed(grid):
        ans = 0
        for line in grid:
            active = False
            char_stt = "."
            for char in line:
                if char == "." and active : ans += 1
                if char == '|' : active = not active
                if char == 'F' or char == 'L': 
                    active = not active
                    char_stt = char
                if char == 'J':
                    if char_stt == 'L': active = not active
                if char == '7':
                    if char_stt == 'F': active = not active             
        return(ans)


                
                

        return "OK"

    def part1():
        ans = 0
        start_dir = all_dir

        for dir in start_dir:
            step = 0
            cur = start

            while isNextValid(dir, cur) == True:

                step += 1
                cur = getPos(cur, dir)
                new_dir = findDir(getChar(cur))
                for i in range(len(new_dir)):
                    if new_dir[i] == getOppositeDir(dir):
                        new_dir.pop(i)
                        break
                dir = new_dir[0]
                if(cur == start):
                    return(step/2)


    
    def part2():
        start_dir = all_dir

        for dir in start_dir:
            _stt_dir = dir
            new_grid = []
            for i in range(len(grid)):
                new_grid.append([])
                for j in range(len(grid[0])):
                    new_grid[i].append(".")

            cur = start

            while isNextValid(dir, cur) == True:
                cur = getPos(cur, dir)
                new_grid[cur[0]][cur[1]] = getChar(cur)
                new_dir = findDir(getChar(cur))

                for i in range(len(new_dir)):
                    if new_dir[i] == getOppositeDir(dir):
                        new_dir.pop(i)
                        break
                
                if(cur == start):
                    char_code = dir_dict[dir][3] + dir_dict[_stt_dir][3]
                    char = ""
                    match char_code:
                        case 3: char = "L"
                        case 6: char = "F"
                        case 9: char = "J"
                        case 12: char = "7"
                        case 10: char = "-"
                        case 15: char = "|"
                    new_grid[cur[0]][cur[1]] = char
                    return(count_enclosed(new_grid))
                
                dir = new_dir[0]
                    
    
    print(part1())
    print(part2())
    

    




    

    



    



    