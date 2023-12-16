# DATA LINE COMPOSITION
#Game 5: 3 green, 7 blue, 7 red; 6 green, 3 red, 4 blue; 7 blue, 4 red

max_red = 12
max_green = 13
max_blue = 14


list_colors = ['green', 'blue', 'red']

def find_color(txt):
    for color in list_colors:
        if txt.find(color) != -1:
            return color

id_sum = 0

with open('aoc02_input.txt') as input_file:

    #CHAQUE PARTIE
    for line in input_file:
        blue = 0
        red = 0
        green = 0


        line = line.replace(" ","")
        line = line.split(":")

        id = int(line.pop(0).replace("Game",""))

        line = line[0].split(";")

        #CHAQUE MAIN
        for hands in line:
            hands = hands.split(",")

            #CHAQUE COULEUR
            for colors in hands:

                color = find_color(colors)
                number = int(colors.replace(color, ""))

                match color:
                    case "blue":
                        if number > blue:
                            blue = number
                    case "green":
                        if number > green:
                            green = number
                    case "red":
                        if number > red:
                            red = number
        
        if blue <= max_blue and red <= max_red and green <= max_green:
            id_sum += id
    
    print(id_sum)
        
