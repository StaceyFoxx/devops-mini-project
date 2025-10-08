# NOTE students, that this file called "client_side" could also be called "main" or anything else.
import requests
import json


def get_root():
    endpoint = "http://127.0.0.1:5000/"
    data = requests.get(endpoint).json()
    return data


def get_all_characters():
    endpoint = "http://127.0.0.1:5000/characters"
    data = requests.get(endpoint).json()
    return data


def get_character_by_id(an_id: int):
    endpoint = f"http://127.0.0.1:5000/characters/{an_id}"
    char = requests.get(endpoint).json()
    return char


def add_character(char):
    endpoint = "http://127.0.0.1:5000/characters/add"
    headers = {'content-type': 'application/json'}
    result = requests.post(
        endpoint, headers=headers, data=json.dumps(char)
    )
    return result.json()


def run():
    # print(get_root())
    # print(get_all_characters())
    # print(get_character_by_id(1))  # this should give you back Harry's dictionary

    new_char = {
        "id": 5,
        "first_name": "Hamed",
        "last_name": "Pour",
        "house": "Slytherin",
        "wand": "Cheese and Pizza core",
        "IQ": 110
    }

    all_characters = (add_character(new_char))
    print(all_characters)

    for char in all_characters:
        print("First Name:", char["first_name"])


if __name__ == "__main__":
    run()
