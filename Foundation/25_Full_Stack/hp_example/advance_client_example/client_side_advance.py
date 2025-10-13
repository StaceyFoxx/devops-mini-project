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


def delete_character_by_id(id):
    endpoint = f"http://127.0.0.1:5000/characters/remove/{id}"
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

    # If the house entered is invalid, prompt again
    while house is None:
        house_name = input("Invalid house. Please enter one of Gryffindor, Hufflepuff, Ravenclaw, Slytherin: ").strip()
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
    # NOTE - I've added more splash here for the Front End example.
    print("\nWelcome to the HP Admin Registry!")
    print("---------------------------------")
    print("Choose an option:")
    print("A: View all character records")
    print("B: Remove a character by ID")
    print("C: Add a NEW character ")
    print("---------------------------------")

    answer = input("What would you like to do? (A, B or C): ").strip().upper()

    if answer == "A":
        if get_all_character_front_end() is None:
            print("Failed to retrieve records.")

        print(get_all_character_front_end())
    elif answer == "B":
        characters = get_all_character_front_end()
        print("Here is the registry: \n")
        print(characters)
        if characters is not None:
            id_to_remove = input("\nEnter the ID of the character you would like to remove: ").strip()
            print("Student removed from registry")
            print("Here is the registry:")
            print(delete_character_by_id(id_to_remove))
        else:
            print("Could not load characters for deletion.")

    elif answer == "C":

        new_student_dict = collect_student_data()

        print("Updated Student Registery: ")
        print(add_new_character_front_end(new_student_dict))

    else:
        print("Invalid option. Please select either A or B.")


if __name__ == "__main__":
    run()
