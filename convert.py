import json
import csv

def parse_json_data(json_data):
    entries = []
    for key, value in json_data.items():
        entry = {
            'name': value.get('service', ''),
            'url': value.get('url', ''),
            'username': value.get('username', ''),
            'password': value.get('password', ''),
            'note': value.get('notes', ''),
            'totp': '',  # Assuming there is no 'info' field in the JSON
            'vault': 'Personal',  # Assuming there is no 'vault' field in the JSON
        }
        entries.append(entry)
    return entries

def write_to_csv(entries, output_file):
    fieldnames = ['name', 'url', 'username', 'password', 'note', 'totp', 'vault']
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow(entry)

def main(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    entries = parse_json_data(data['data'])
    write_to_csv(entries, output_file)

# Example usage
input_file = 'input.json'  # Path to the input JSON file
output_file = 'output.csv'  # Path to the output CSV file
main(input_file, output_file)
