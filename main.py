####### codecademy project ######
# Create a system to automatically change the weights on my adjustable dumbbells for workouts at home
# Use Stepper motors for accurate number of turns
# Create specific workouts that will automatically change dumbbell weights based on recipe data

######################################################################################################


# import libraries
import json
import os


### Constants ###
# Set program run constants
main_run = True




# all workout routines in json format. Pairs are Workout Name : Weight 
push = {"Bench Flys": 10, "Chest Press": 20, "Seated Shoulder Press": 10, "Skullcrushers": 15, "Lateral Shoulder Raise": 10}
pull = {"Bent over rows": 20, "Pull Ups": 0}
leg = {"Goblet Squats": 30, "Deadlift": 40, "Bulgarian Split Squat": 15, "Farmer Carry": 30}

# one list for all routines
routines = [push, pull, leg]

# Set Menu constants
main_menu_message = "Which workout would you like to start?"
main_menu_options = ["Push", "Pull", "Legs"]

### Functions ###
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    return

def print_menu(message, options):
    print(message + "\n")
    for i in options:
        print(i + "\n")
    return

def get_user_input():
    user_input = input("Select which routine to start:\n")
    return user_input


while main_run:
    #clear_screen()
    print_menu(main_menu_message, main_menu_options)
    user_input = get_user_input().upper()
    print(user_input)
    match user_input:
        case "PUSH":
            #call push routine
            print("Calling push routine\n")
        case "PULL":
            #call pull routine
            print("Calling pull routine\n")
        case "LEGS":
            #call leg routine
            print("Calling leg routine")
        case "EXIT":
            #exit main loop
            print("Exiting Program...")
            main_run = False

    
    