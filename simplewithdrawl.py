import json

with open("data.json", "r") as f:
        data = json.load(f)

def start():
    choice = input('Select your choice. Type \'1\' for Reading, and \'2\' for Writing. \n')
    if choice == '1':
        name = input('Who\'s name would you like to read information from? \n')
        if name not in data:
            print('It looks like you did not enter a valid name. Please try again.')
            startover()
        else:
            info = input('What information would you like to read from this person? You may choose \'Age\', \'Gender\', or \'Profession\'. \n')
            info = info.capitalize()
            if info == 'Age':
                print(f'{name}\'s age is set to '+data['Data'][name][info])
            if info == 'Gender':
                print(f'{name}\'s gender is set to '+data['Data'][name][info])
            if info == 'Profession':
                print(f'{name}\'s profession is set to '+data['Data'][name][info])
            else:
                print('It looks like you did not select one of the availible categories.' )
                startover()


def startover():
    startchoice = input('Would you like to restart? Type \'Yes\' or \'No\' \n')
    startchoice = startchoice.capitalize()
    if startchoice == 'Yes':
        start()
    if startchoice == 'No':
        return
    else:
        print('You did not enter any of the choices you poophead. I\'m not going to be kind now. You have to restart the code.')

start()

