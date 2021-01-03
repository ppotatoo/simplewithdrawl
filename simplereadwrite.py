import json
import time
def start():
    with open("data.json", "r") as f:
        data = json.load(f)
    choice = input('Do you want to read or do you want to write?\n')
    choice = choice.capitalize()
    if choice == 'Write':
        user = input('Please Type Your Name: \n')
        user = user.capitalize()
        with open("data.json", "w") as f:
            data[user] = input('Set your status: \n')
            json.dump(data, f, indent=4)
        print(f'{user}\'s status set to: '+data[user])
    if choice == 'Read':
        read = input('Whose status would you like to read?\n')
        read = read.capitalize()
        if read not in data:
            print('It looks like that person is not in our data. Please try again.')
        else: 
            print(f'{read}\'s status is set to: '+data[read])
    def startover():
        over = input('Would you like to start over? Type \'1\' for Yes and \'2\' for No \n')
        if over == '1':
            start()
        if over == '2':
            return
        else:
            print('It looks like you did not pick either of the answers you dumbo')
            time.sleep(1.5)
            startover()
    startover()
start()