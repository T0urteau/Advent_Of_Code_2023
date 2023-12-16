with open('aoc05_input.txt') as input_file:

    result = -1

    input_file = input_file.read()
    data = input_file.split("\n\n")

    #ARRAY SEED NUMBER
    seeds = data.pop(0)
    seeds = seeds[6:].strip().split(" ")

    for n in range(len(data)):
        data[n] = data[n].split("\n")
        data[n].pop(0)

        for i in range(len(data[n])):
            data[n][i] = data[n][i].split(" ")
            for j in range(len(data[n][i])):
                data[n][i][j] = int(data[n][i][j])

        data[n] = sorted(data[n], key=lambda converter: converter[1])

    for n in seeds:
        n = int(n)
        for type in data:
            if n < type[0][1]:
                continue
            else:
                for i in range(len(type)):
                    if n >= type[i][1] and n <= type[i][1]+type[i][2]:
                        n = type[i][0] + (n - type[i][1])
                        break
        
        if result == -1:
            result = n
        elif n < result:
            result = n
    
    print(result)