print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
first_choice = input("Left or Right? ")
first_choice_lower = first_choice.lower()

if first_choice_lower == "left":
    print("You made it safely, proceed.")

    second_choice = input("Swim or Wait? ")
    second_choice_lower = second_choice.lower()

    if second_choice_lower == "swim":
        print("You swam successfully, you not fat! Move on.")

        third_choice = input("Choose a door; Red, Yellow, or Blue? ")
        third_choice_lower = third_choice.lower()

        if third_choice_lower == "red":
            print("You Win!!")
        elif third_choice_lower == "yellow":
            print("Game Over.")
        elif third_choice_lower == "blue":
            print("Game Over.")
        else:
            print("Wrong door, you died, try again.")
    else:
        print("You waited too long and died of starvation, game over.")
else:
    print("You died, try again.")

# Solution
# 1. Create a variable (first_input) and enable input from user
# 2. To be able to capture all the ways a user can type the correct answer, change the format for all typed input to
# .lower (first_choice_lower) converted to .lower()
# 3. Create an if/else statement for the first input that states if a person chose left, to continue, if picked right
# game is over.
# 4. Create a variable inside the if statement for the second choice to highlight the second choices. Do the same method
# of lowering all the options available for the correct answer to enable the computer to pick up.
# 5. Create a variable for the third option, which would be an if/elif statement since it has 3
# options with different ending.
# Capture the choices in lower case to enable the computer to pick up the correct choice no matter how it's typed.
# 6. Else function at every choice to conclude what would happen if user chose the wrong option.
