import json
with open("data.json", "r") as f:
        data = json.load(f)
with open("data.json", "w") as f:
            data['Data']['Bob']['Profession'] = input('Set Bob\'s profession: \n')
            data['Data']['Bob']['Age'] = input('Set Bob\'s age: \n')
            data['Data']['Bob']['Gender'] = input('Set Bob\'s gender: \n')
            json.dump(data, f, indent=4)
print(data['Data']['Bob']['Profession']+data['Data']['Bob']['Age']+ data['Data']['Bob']['Gender'])