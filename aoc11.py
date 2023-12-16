import re
with open('aoc11_input.txt') as f:
    grid = [val for val in f.read().rstrip().split("\n")]

    col = [1]* len(grid[0])
    row = [1] * len(grid)
    list_galaxies = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                list_galaxies.append([i,j])
                col[i] = 0
                row[j] = 0            
    
    def getNbExpandedBetween(pos1, pos2, older = False):
        ans = 0
        for i in range(min(pos1[0],pos2[0])+1, max(pos1[0],pos2[0])):
            ans += col[i] if older == False else col[i]*999999
        for j in range(min(pos1[1],pos2[1])+1, max(pos1[1],pos2[1])):
            ans += row[j] if older == False else row[j]*999999
        return ans
        


    def part1():
        ans = 0
        galaxies = list_galaxies.copy()
        while len(galaxies) > 0:
            gal = galaxies.pop(0)
            for tgt in galaxies:
                ans += abs(tgt[0]-gal[0]) + abs(tgt[1]-gal[1])
                ans += getNbExpandedBetween(gal, tgt)
        return ans
    
    def part2():
        ans = 0
        galaxies = list_galaxies.copy()
        while len(galaxies) > 0:
            gal = galaxies.pop(0)
            for tgt in galaxies:
                ans += abs(tgt[0]-gal[0]) + abs(tgt[1]-gal[1])
                ans += getNbExpandedBetween(gal, tgt, True)
        return ans
    
    print(part1())
    print(part2())
    

    




    

    



    



    