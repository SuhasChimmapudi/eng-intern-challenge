given_string = input()
#removing the quotation marks in the input
given_string = given_string[1: -1]

braille_atoz = {'A': "O.....", 'B': "O.O...", 'C': "OO....", 'D': "OO.O..",
                'E': "O..O..", 'F': "OOO...", 'G': "OOOO..", 'H': "O.OO..",
                'I': ".OO...", 'J': ".OOO..", 'K': "O...O.", 'L': "O.O.O.",
                'M': "OO..O.", 'N': "OO.OO.", 'O': "O..OO.", 'P': "OOO.O.",
                'Q': "OOOOO.", 'R': "O.OOO.", 'S': ".OO.O.", 'T': ".OOOO.",
                'U': "O...OO", 'V': "O.O.OO", 'W': ".OOO.O", 'X': "OO..OO",
                'Y': "OO.OOO", 'Z': "O..OOO"}
braille_nums = {'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
                '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
                '9': ".OO...", '0': ".OOO.."}


def translate_to_english(braille_string):
    #divide braille string into its symbols
    braille_list = [braille_string[i:i+6] for i in range(0, len(braille_string) - 2,
                                                          6)]
    state = 0
    i = 0
    english_string = ''
    
    while i < len(braille_list):
        # if 'capital follows' symbol occurs
        if braille_list[i] == ".....O":
            state = 1
        # if 'number follows' symbol occurs    
        elif braille_list[i] == ".O.OOO":
            state = 2
        # if 'space' symbol occurs  
        elif braille_list[i] == "......":
            state = 0
            english_string += ' '
        else:
            if state == 0:
                english_string += list(braille_atoz.keys())[list(braille_atoz.values()).index(braille_list[i])].lower()
            elif state == 1:
                english_string += list(braille_atoz.keys())[list(braille_atoz.values()).index(braille_list[i])]
                state = 0
            elif state == 2:
                english_string += list(braille_nums.keys())[list(braille_nums.values()).index(braille_list[i])]

        i += 1        
    print(english_string)


def translate_to_braille(english_string):
    braille_string = ''
    i = 0

    while i < len(english_string):
        # if letter is capital
        if english_string[i].isupper():
            braille_string += ".....O" + braille_atoz[english_string[i]]
        # if it is a number
        elif english_string[i].isnumeric():
            #checking if it is the first number
            if i == 0 or not(english_string[i - 1].isnumeric()):
                braille_string += ".O.OOO" + braille_nums[english_string[i]]
            else:
                braille_string += braille_nums[english_string[i]] 
        # if it is a space
        elif english_string[i] == ' ':
            braille_string += "......"
        else:
            braille_string += braille_atoz[english_string[i].upper()]
            
        i += 1
    print(braille_string)
            
done = 0
for char in given_string:
    #if char is a value other than 'O' or '.', then it is in English
    if char != 'O' and char != '.':
        translate_to_braille(given_string)
        done = 1
        break
    
if done == 0:
    translate_to_english(given_string)



    
