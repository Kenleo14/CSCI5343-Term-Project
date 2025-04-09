import json

with open('data.json', 'r') as file:
    data = json.load(file)

easyCount = 0
medCount = 0
hardCount = 0

algorithm = "binary_search"

for i in range(len(data)):
    try:
        while data[i]['algorithms'][0] != algorithm:
                del data[i]
        if data[i]['algorithms'][0] == algorithm:
            if data[i]['difficulty'] == "Easy":
                easyCount += 1
            elif data[i]['difficulty'] == "Medium":
                medCount += 1
            elif data[i]['difficulty'] == "Hard":
                hardCount += 1
    except IndexError:
        print(f"Reached end of list")
        break

        
with open('data_binary_search.json', 'w') as file:
    json.dump(data, file, indent = 4)

print(f"{algorithm}\nEasy Count: {easyCount}\nMedium Count: {medCount}\nHard Count: {hardCount}")

