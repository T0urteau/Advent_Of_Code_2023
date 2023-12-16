import re

result = 0

with open('aoc03_input.txt') as input_file:

    line_array = input_file.readlines()
    original = line_array.copy()
    
    for n in range(len(line_array)):
        line_array[n] = line_array[n][:-1]
        original[n] = original[n][:-1]


    #POUR CHAQUE LIGNE
    for n in range(len(line_array)):
        #TANT QU'ON TROUVE UN SYMBOLE
        while True:
            reg = re.search("[^a-zA-z0-9\.]", line_array[n])

            if reg:
                index = reg.span()[0]

                #ON CHERCHE SI NUMERO DANS LES LIGNES n-1, n, n+1
                for x in range(-1,2):

                    string = list(line_array[n+x])
                    tmpLen = len(string)

                    for y in range(-1,2):
                        
                        tmpIndex = index+y
                        if tmpIndex >= 0 and tmpIndex < tmpLen and string[tmpIndex].isnumeric():
                    
                            nb = string[tmpIndex]
                            string[tmpIndex] = "."

                            tmp = tmpIndex
                            while True:
                                tmp = tmp-1
                                if(tmp >= 0 and string[tmp].isnumeric()):
                                    nb = string[tmp] + nb
                                    string[tmp] = "."
                                else:
                                    break
                            
                            tmp = index+y

                            while True:
                                tmp = tmp+1
                                if(tmp < tmpLen and string[tmp].isnumeric()):
                                    nb = nb + string[tmp]
                                    string[tmp] = "."
                                else:
                                    break
                            
                            result += int(nb)
                            nb = ""

                    line_array[n+x] = "".join(string)


                string = list(line_array[n])
                string[index] = "."
                line_array[n] = "".join(string)
            else:
                break
    
    '''for n in range(len(line_array)):
        print(original[n] + " " + line_array[n])'''

    print(result)




        
