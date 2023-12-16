result = 0
tmp = ""
found = False

with open('aoc01_input.txt') as input_file:

    for line in input_file:

        tmp = ""
        found = False
        all_char = list(line)
        
        for c in all_char:
            if c.isnumeric():
                tmp += c
                break

        size = len(all_char)
        while found == False:
            size -= 1
            if all_char[size].isnumeric():
                tmp += all_char[size]
                break
        
        result += int(tmp)
    
    print(result)

                

