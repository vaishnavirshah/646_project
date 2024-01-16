import requests
import json

def download_json(url, save_path):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded JSON from {url} and saved to {save_path}")
    else:
        print(f"Failed to download JSON. Status code: {response.status_code}")

# Replace 'your_json_url' with the actual URL of the JSON file
json_url = 'https://ciir.cs.umass.edu/downloads/LaMP/LaMP_2/train/train_questions.json'
# Replace 'output.json' with the desired local file name to save the JSON
output_path = '/Users/vaishnavishah/Documents/COMPSCI 646/project/646_project/lamp2_trainQs.json'

download_json(json_url, output_path)
