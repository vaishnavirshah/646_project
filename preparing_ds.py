import json

# Specify the path to your JSON file
json_file_path = 'lamp2_trainQs.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
    # Load JSON data into a Python object
    data = json.load(file)

# Print the result
#print(data[0])

content = []

for i in range(len(data[0]['profile'])):
    content.append(data[0]['profile'][i]['text'])

# print(len(content))
# print(content[0])

