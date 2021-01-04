import json
import os

def wipe():
    os.system("cls")

with open("data.json", "r") as f:
        data = json.load(f)

def start():
    choice = input('Select your choice. Type \'1\' for Reading, and \'2\' for Editing. \n')
    if choice == '1':
        name = input('Select a person to read information from. \n')
        if name not in data['Data']:
            wipe()
            print('It looks like you did not enter a valid name. Please try again.')
            startover()
        else:
            info = input(f'What information would you like to read from {name}? You may choose \'Age\', \'Gender\', or \'Profession\'. You may also type \'All\' to view all information \n')
            info = info.capitalize()
            if info == 'Age':
                print(f'{name}\'s age is set to '+data['Data'][name][info])
            if info == 'Gender':
                print(f'{name}\'s gender is set to '+data['Data'][name][info])
            if info == 'Profession':
                print(f'{name}\'s profession is set to '+data['Data'][name][info])
            if info == 'All':
                print(data['Data'][name])
            else:
                wipe()
                print('It looks like you did not select one of the available categories.' )
                startover()
    if choice == '2':
        name = input('Select a person to edit: \n')
        if name not in data['Data']:
            wipe()
            print('It looks like you did not enter a valid name. Please try again.')
            startover()
        else:
            with open("data.json", "w") as f:
                info = input(f'What information would you like to edit from {name}? You may choose \'Age\', \'Gender\', or \'Profession\'. \n')
                info = info.capitalize()
                if info == 'Age':
                    data['Data'][name][info] = input(f'What would you like to set {name}\'s age to? \n')
                    json.dump(data, f, indent=4)
                    print(f'Set {name}\'s age to '+data['Data'][name][info])
                if info == 'Gender':
                    data['Data'][name][info] = input(f'What would you like to set {name}\'s gender to? \n')
                    json.dump(data, f, indent=4)
                    print(f'Set {name}\'s gender to '+data['Data'][name][info])
                if info == 'Profession':
                    data['Data'][name][info] = input(f'What would you like to set {name}\'s profession to? \n')
                    json.dump(data, f, indent=4)
                    print(f'Set {name}\'s profession to '+data['Data'][name][info])
                else:
                    wipe()
                    print('It looks like you did not select a valid category. Try again.')
                    json.dump(data, f, indent=4)
    startover()

def startover():
    startchoice = input('Would you like to restart? Type \'Yes\' or \'No\' \n')
    startchoice = startchoice.capitalize()
    if startchoice == 'Yes':
        start()
    if startchoice == 'No':
        print('Bye. Hope you enjoyed.')
    else:
        print('You did not enter any of the choices you poophead. I\'m not going to be kind now. You have to restart the code.')

start()

