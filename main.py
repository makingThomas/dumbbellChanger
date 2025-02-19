####### codecademy project ######
# Create a system to automatically change the weights on my adjustable dumbbells for workouts at home
# Use Stepper motors for accurate number of turns
# Create specific workouts that will automatically change dumbbell weights based on recipe data

######################################################################################################


# import libraries
import json
import os
import msvcrt


### Constants ###
# Set program run constants
main_run = True
display_error = False

# all workout routines in dictionary format. Pairs are Workout Name : Weight 
push = {"Chest Flys": 10, "Chest Press": 20, "Seated Shoulder Press": 10, "Skullcrushers": 15, "Lateral Shoulder Raise": 10}
pull = {"Bent over rows": 20, "Pull Ups": 0}
legs = {"Goblet Squats": 30, "Deadlift": 40, "Bulgarian Split Squat": 15, "Farmer Carry": 30}

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

def dict_to_list(dict : dict):
    keys = []
    values = []
    items = dict.items()
    for item in items:
        keys.append(item[0]), values.append(item[1])
    return keys, values

def get_user_input(message : str):
    user_input = input(message)
    return user_input

def execute_routine(routine_name : str, routine : dict):
    exercise_count = 0
    exercise_names, weights = dict_to_list(routine)
    exercise_number = len(exercise_names)
    for i in range(len(exercise_names)):
        exercise_count += 1
        clear_screen()
        print(routine_name + "\n")
        print("Exercise {count} of {num}\n\n".format(count = exercise_count, num = exercise_number))
        key_pressed = False
        print("Exercise: {exercise}\nWeight: {weight}\n".format(exercise = exercise_names[i], weight = weights[i]))
        while not key_pressed:
            get_user_input("Press any button to move on to the next exercise")
            key_pressed = True
    

while main_run:
    clear_screen()
    print_menu(main_menu_message, main_menu_options)
    if display_error == False:
        input_message = 'Select which routine to start. Type "exit" to close the program\nUser selection: '
    else:
        input_message = 'Select which routine to start. Type "exit" to close the program\nInvalid input!\nUser selection: '
    user_input = get_user_input(input_message).upper()
    match user_input:
        case "PUSH":
            display_error = False
            execute_routine("Push Routine", push)
        case "PULL":
            display_error = False
            execute_routine("Pull Routine", pull)
        case "LEGS":
            display_error = False
            execute_routine("Legs Routine", legs)
        case "EXIT":
            #exit main loop
            display_error = False
            print("Exiting Program...")
            main_run = False
        case _:
            display_error = True

    
    