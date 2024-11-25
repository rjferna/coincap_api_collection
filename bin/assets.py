import requests
import time
import csv
import json


def dict_to_json(my_dict, json_filename):
    """
    Converts a dictionary to a JSON file.
    Args: my_dict (dict): The input dictionary;  json_filename (str): The desired filename for the JSON output.
    Returns: None
    """
    try:
        # Write the dictionary to a JSON file
        with open(json_filename + ".json", 'w') as json_file:
            json.dump(my_dict, json_file, indent=4)  # Indent for readability (optional)

        return f"JSON file '{json_filename}' created successfully!"
    except Exception as e:
        return f"Error: {e}"

def get_unix_timestamp(date_str):
    try:
        timestamp = int(time.mktime(time.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ'))) * 1000
        return timestamp
    except ValueError:
        print(f"Invalid date format: {date_str}")
        return None

def get_asset(key, url, encoding):
    api_key = key
    base_url = url
    accepted_encoding = encoding

    print(base_url)

    headers = {
        'Accept-Encoding': accepted_encoding, # Enables Compression
        'Authorization': f'bearer {api_key}'
    }

    response = requests.get(base_url, headers=headers)
    response_json = response.json()

    if response.status_code == 200:
        return response_json['data']
    else:
        return f"Error: {response_json.get('error', 'Unknown error')}"
    

def get_asset_history(key, url, encoding, start, end, interval):
    api_key = key
    base_url = url
    accepted_encoding = encoding
    interval = interval


    start_timestamp = start
    end_timestamp = end

    start_date = get_unix_timestamp(start_timestamp)
    end_date = get_unix_timestamp(end_timestamp)

    if start_date is None or end_date is None:
        return None
    
    param = {
        #'Accept-Encoding': accepted_encoding, # Enables Compression
        'start': start_date,
        'end': end_date,
        'interval': interval #
    }

    response = requests.get(base_url, params=param)
    response_json = response.json()

    if response.status_code == 200:
        #dict_to_csv(response_json, file_path + file_name)
        return response_json
    else:
        return f"Error: {response_json.get('error', 'Unknown error')}"   
