"""
Client side, "Requests" goes here.
"""
import requests
import json


def get_all_character_front_end():
    endpoint = "http://127.0.0.1:5000/characters"
    result = requests.get(endpoint).json()
    return result


def add_new_character_front_end(new_student_dict):
    endpoint = "http://127.0.0.1:5000/characters/add"
    result = requests.post(
        endpoint,
        headers={'content-type': 'application/json'},
        data=json.dumps(new_student_dict)
    )

    return result.json()


def delete_character_by_id(an_id):
    endpoint = f"http://127.0.0.1:5000/characters/remove/{an_id}"
    result = requests.delete(endpoint).json()
    return result


def collect_student_data():
    # Prompt the user for input with appropriate questions
    name = input("Enter the student's name: ").strip()

    # Prompt for student class, avoiding 'class' as a reserved word
    student_class = input("Enter the student's class (e.g., Potions): ").strip()

    # Prompt for IQ, ensuring it's an integer
    iq = int(input("Enter the student's IQ (as a number): ").strip())

    # Prompt for house, converting it from a string name to an associated number
    # Assuming house corresponds to a predefined mapping
    house_mapping = {"Gryffindor": 1, "Hufflepuff": 2, "Ravenclaw": 3, "Slytherin": 4}
    house_name = input("Enter the student's house (Gryffindor, Hufflepuff, Ravenclaw, Slytherin): ").strip()
    house = house_mapping.get(house_name, None)

    # Prompt for quidditch participation, ensuring it's a boolean (yes/no)
    quidditch_input = input("Does the student play Quidditch? (yes/no): ").strip().lower()
    quidditch = True if quidditch_input == 'yes' else False

    # Return the collected data as a dictionary
    new_student_dict = {
        "name": name,
        "class": student_class,
        "IQ": iq,
        "house": house,
        "quidditch": quidditch
    }

    return new_student_dict


def run():
    pass
    # print(get_all_character_front_end())

    # new_student = collect_student_data()
    # print(add_new_character_front_end(new_student))

    # print(delete_character_by_id(8))


if __name__ == "__main__":
    run()
