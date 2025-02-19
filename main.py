####### codecademy project ######
# Create a system to automatically change the weights on my adjustable dumbbells for workouts at home
# Use Stepper motors for accurate number of turns
# Create specific workouts that will automatically change dumbbell weights based on recipe data

# TO DO
# navigate menu with only up arrow, down arrow, and enter (simulate button input for raspberry pi)

######################################################################################################


# import libraries
import json
import os

# Set program run constants
main_run = True
display_error = False

# all workout routines in dictionary format. Pairs are Workout Name : Weight 
push = {"Chest Flys": 10, "Chest Press": 20, "Seated Shoulder Press": 10, "Skullcrushers": 15, "Lateral Shoulder Raise": 10}
pull = {"Bent over rows": 20, "Pull Ups": 0}
legs = {"Goblet Squats": 30, "Deadlift": 40, "Bulgarian Split Squat": 15, "Farmer Carry": 30}

# strings of routine file names
push_file_name = "push.json"
pull_file_name = "pull.json"
legs_file_name = "legs.json"

# Set Menu constants
main_menu_message = "Which workout would you like to start?"
main_menu_options = ["Push", "Pull", "Legs", "Save"]

# clear terminal screen. No args, no return
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    return

# prints a menu title/message followed by a list of menu options. Args(message : str, options : list), no return
def print_menu(message : str, options : list):
    print(message + "\n")
    for i in options:
        print(i)
    return

# converts a dictionary variable into a keys list and values list. Args(dictionary : dict), returns tuple (keys list, values list)
def dict_to_list(dict : dict):
    keys = []
    values = []
    items = dict.items()
    for item in items:
        keys.append(item[0]), values.append(item[1])
    return keys, values

# Displays a message and prompts user for a keyboard response. Args(message : str), returns the user_input : str
def get_user_input(message : str):
    user_input = input(message)
    return user_input

# display error message for incorrect input in main menu. Args(display_error : bool), return error_message : str
def eval_display_error(display_error):
    if display_error == False:
        return '\nSelect which routine to start. Type "exit" to close the program\nUser selection: '
    else:
        return 'Select which routine to start. Type "exit" to close the program\nInvalid input!\nUser selection: '

# pulls routine dictionary and converts to lists. Displays exercise names and weights and cycles through them in order. Args (routine_name :str, routine : dict), no return
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
    return

# takes the push, pull, and legs dicts and writes them to .json files to be read later on startup
def save_data():
    # save push routine
    with open(push_file_name, 'w') as data_json:
        json.dump(push, data_json)

    # save pull routine
    with open(pull_file_name, 'w') as data_json:
        json.dump(pull, data_json)

    # save legs routine
    with open(legs_file_name, 'w') as data_json:
        json.dump(legs, data_json)

# takes the push, pull, legs .json files and loads them into the program. Overwrites previous push, pull, legs dicts
def load_data():
    # load push routine
    with open(push_file_name) as data_json:
        push = json.load(data_json).copy()
        #new_push = json.load(data_json)
        #push = new_push.copy()

    with open(pull_file_name) as data_json:
        pull = json.load(data_json).copy()
        #new_pull = json.load(data_json)

    with open(legs_file_name) as data_json:
        legs = json.load(data_json).copy()
        #new_legs = json.load(data_json)
    return push, pull, legs


##### STARTUP #####
# load data from .json files
push, pull, legs = load_data()

##### MAIN LOOP #####
while main_run:
    clear_screen()
    print_menu(main_menu_message, main_menu_options)
    input_message = eval_display_error(display_error)
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
        case "SAVE":
            save_data()
        case _:
            display_error = True

    
    