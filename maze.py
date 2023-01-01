import readchar
import os
from random import randint

ascii_game_over = '''
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
█       █      █  █▄█  █       █  █       █  █ █  █       █   ▄  █  
█   ▄▄▄▄█  ▄   █       █    ▄▄▄█  █   ▄   █  █▄█  █    ▄▄▄█  █ █ █  
█  █  ▄▄█ █▄█  █       █   █▄▄▄   █  █ █  █       █   █▄▄▄█   █▄▄█▄ 
█  █ █  █      █       █    ▄▄▄█  █  █▄█  █       █    ▄▄▄█    ▄▄  █
█  █▄▄█ █  ▄   █ ██▄██ █   █▄▄▄   █       ██     ██   █▄▄▄█   █  █ █
█▄▄▄▄▄▄▄█▄█ █▄▄█▄█   █▄█▄▄▄▄▄▄▄█  █▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄█  █▄█
''' 

obstacle_definition ='''\
#################################################
#                                ################
#                                ################                               
############################     ################
############################     ################
#                                           #####
#                                ########   #####
#     ###################################   #####
#                                  ###         ## 
#                                  ###        ###
#     ################################    #######
#                                         #######
#                                  ##############
#################################################\
'''
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

POS_X = 0
POS_Y = 1
ULTIMATE_POSITION = 1
cordinate = [0,1]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition) 

cordinate[POS_X] = 3
cordinate[POS_Y] = 1
NUM_OF_OBJECTS = 11

map_objects = []
tails = [] 
tail_lenght = 0

char_to_draw = " "
end_game = False
obstacle_in_cell = None

while not end_game:
    os.system("clear")
    # Generador de objetos
    while len(map_objects) <= NUM_OF_OBJECTS:
        new_position = [randint(0,MAP_WIDTH - 1),randint(0,MAP_HEIGHT - 1)]
        if new_position not in map_objects and obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            map_objects.append(new_position)
    print("+"+ ("-" * (MAP_WIDTH)) + "+")
    for coordinate_y in range(MAP_HEIGHT):
            print("|",end=" ")
            for coordinate_x in range(MAP_WIDTH):
                char_to_draw = " "
                tail_in_cell = False
                object_in_cell = False
                for map_object in map_objects:
                    if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                        char_to_draw = "*"
                        object_in_cell = map_object
                
                for tail in tails[ULTIMATE_POSITION:]:#La posicion 0 es la posicion del jugador 
                    if tail[POS_X] == coordinate_x and tail[POS_Y] == coordinate_y:
                        char_to_draw = "@"
                        tail_in_cell = True
                
                if obstacle_definition[coordinate_y][coordinate_x] == "#":
                    char_to_draw = "#"
                
                if cordinate[POS_X] == coordinate_x and coordinate_y == cordinate[POS_Y]:
                    char_to_draw = "@"

                    if tail_in_cell:
                        end_game = True
                    
                    if object_in_cell:
                        map_objects.remove(object_in_cell)
                        tail_lenght += 1
                
                print("{}".format(char_to_draw),end="")
            print("|")
    print("+"+ ("-" * (MAP_WIDTH)) + "+")

    no_hay_muro = True
    if not end_game:
        choose_letter_to_move = readchar.readchar()
        if choose_letter_to_move == "d":
            cordinate[POS_X] += 1
            if obstacle_definition[cordinate[POS_Y]][cordinate[POS_X]] == "#":
                no_hay_muro = False
                cordinate[POS_X] -= 1

            if cordinate[POS_X] > 59:
                cordinate[POS_X] = 0
            
        elif choose_letter_to_move == "a":
            cordinate[POS_X] -= 1
            if obstacle_definition[cordinate[POS_Y]][cordinate[POS_X]] == "#":
                no_hay_muro = False
                cordinate[POS_X] += 1

            if cordinate[POS_X] < 0:
                cordinate[POS_X] = 59

        elif choose_letter_to_move == "w":
            cordinate[POS_Y] -= 1
            if obstacle_definition[cordinate[POS_Y]][cordinate[POS_X]] == "#":
                no_hay_muro = False
                cordinate[POS_Y] += 1

            if cordinate[POS_X] < 0:
                cordinate[POS_Y] = 14
            
        elif choose_letter_to_move == "s":
            cordinate[POS_Y] += 1
            if obstacle_definition[cordinate[POS_Y]][cordinate[POS_X]] == "#":
                no_hay_muro = False
                cordinate[POS_Y] -= 1
            
            if cordinate[POS_Y] > 59:
                cordinate[POS_Y] = 0

        elif choose_letter_to_move in ["q","Q"]:end_game = True
        os.system("clear")

        if no_hay_muro:
            tails.insert(0,[cordinate[POS_X],cordinate[POS_Y]])
            tails = tails[:tail_lenght]

if end_game:
    os.system("clear")
    print(ascii_game_over)
