from contextlib import nullcontext


result = 0

wordNumber = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

wordToNumber = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9

}



with open('aoc01_input.txt') as input_file:

    for line in input_file:
        line = line[:-1]

        startNumber = 0
        startPart = line
        startIndex = -1

        endNumber = 0
        endPart = line
        endIndex = -1

        all_char = list(line)

        #PREMIER NUMERO
        for n in range(len(all_char)):
            c = all_char[n]
            if c.isnumeric():
                startNumber = c
                startPart = line[:n]
                break
        
        for word in wordNumber:
            tmpIndex = startPart.find(word)
            if tmpIndex > -1:
                if startIndex == -1:
                    startIndex = tmpIndex
                    startNumber = wordToNumber[word]
                elif tmpIndex < startIndex:
                    startIndex = tmpIndex
                    startNumber = wordToNumber[word]




        #DERNIER NUMERO
        size = len(all_char)
        while True:
            size -= 1
            if all_char[size].isnumeric():
                endNumber = all_char[size]
                endPart = line[size+1:]
                break
        
        for word in wordNumber:
            tmpIndex = endPart.rfind(word)
            if tmpIndex > -1:
                if tmpIndex > endIndex:
                    endIndex = tmpIndex
                    endNumber = wordToNumber[word]

        result += int(str(startNumber) + str(endNumber))
    print(result)


     

