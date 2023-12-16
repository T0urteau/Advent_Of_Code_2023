import sys

with open('aoc05_input.txt') as f:
    groups = f.read().split("\n\n")
    
    seeds = groups.pop(0).split(" ")[1:]
    seeds = [int(val) for val in seeds]
    map_seeds = []
    for n in range(0, len(seeds), 2):
        map_seeds.append([seeds[n], seeds[n]+seeds[n+1] -1])
    #map_seeds = sorted(map_seeds, key= lambda seed: seed[0])


    groups = [val.split("\n")[1:] for val in groups]
    for n in range(len(groups)):
        groups[n] = [list(map(int, val.split())) for val in groups[n]]
        #groups[n] = sorted(groups[n], key= lambda val: val[1])
        for i in groups[n]:
            i[0] = i[0] - i[1]
            i[2] = i[1] + i[2] -1


    tmp_seeds = []

    print(len(groups))

    for group in groups:
        while len(map_seeds) > 0:
            s = map_seeds.pop(0)
            updated = False
            for k in group:
                if s[0] < k[1] and s[1] >= k[1]: #Seed commence hors range mais fini apres debut range
                    map_seeds.append([s[0],k[1]-1])
                    if s[1] <= k[2]: #Partie restante entierement dans la range
                        tmp_seeds.append([k[1]+k[0], s[1]+k[0]])
                    else:
                        tmp_seeds.append([k[1]+k[0], k[2]+k[0]])
                        map_seeds.append([k[2]+1, s[1]])
                    update = True
                    break
                elif s[0] >= k[1] and s[0] <= k[2]: #Seed commence en range
                    if s[1] <= k[2]: #Seed fini en range
                        tmp_seeds.append([s[0]+k[0], s[1]+k[0]])
                    else: #Seed fini hors range
                        tmp_seeds.append([s[0]+k[0], k[2]+k[0]])
                        map_seeds.append([k[2]+1, s[1]])
                    updated = True
                    break
            if updated == False:
                tmp_seeds.append(s)
        map_seeds = tmp_seeds
        tmp_seeds = []
    
    ans = sys.maxsize
    for s in map_seeds:
        if s[0] < ans:
            ans = s[0]
    
    print(ans)


                




    
