# time_now = datetime.now()
# print(time_now)
# # %D gives full date dd-mm-yyyy but %d only gives dd
# formatted_time = time_now.strftime("%D")
# print(f"The last time you were here was {formatted_time}")
#
# # assignment submission
# api = "adklfhalgfiawbfnkdsbaoue"

# # when time to submit - keep it empty
# api = "<your-api-here>"
#
# # in your readme
#
# """
# This is my project
# To use it you need an API key
# populate your api key on line 13 intp vairable api
#
# api = "<you-api-key-goes-here>"
# """




"""
LOOPS 
1 - For Loop
 - loop over anything that it iterable, i.e. a sequence of sorts
 - lists, dictionaries, strings , other types such as range(5)
2 - While Loop
"""
#
# #  FOR LOOP
# collection = [1, 2, 3, 4, 5, 6]
# total = 0
#
# for item in collection:
#     total = total + item
#
# # print(total)
#
#
# # WHILE LOOP
# # KEY NOTE - ALWAYS have a breaking condition
#
# flag = True
#
# while flag:
#     service = input('Hello welcome to x spa? What service would you like?\n1 - Massage\n2 - Pedicure\n3- exit')
#     # check if string is numeric - if so continue the code if not print a message
#     if not service.isnumeric():
#         print('We only accept 1 or 2. Please try again?')
#         # continnue - allows the while loop to immediately restart
#         # break - will break out of the while loop immediately
#         continue
#
#     service = int(service)
#     if service  == 1:
#         print('That will be £20 -  Thanks')
#     elif service == 2:
#         print('That will be £5 - Thanks')
#     elif service == 3:
#         print('Come back again soon!')
#         flag = False
#     else:
#         print('We accept options 1 or 2 only. Enjoy the rest of your day!')
#         flag = False













"""
WITH()
& writing out results to a text file
"""

"""
program xxxx
its function is to provide a user with pokemon iunofrmation and write it out to a log boook
author
    Fatma El
Date
    15/09/2025
version
    0.1
"""
import requests


def pokemon_id_request(pokemon_number, user_name):
    """
    Send a request to poke api on a pokemon id to retrieve information about that pokemon
    :param pokemon_number: int
    :return: A string summary of the pokemon
    """
    endpoint = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

    response = requests.get(endpoint)
    pokemon = response.json()

    print(f'We have processed your pokemon id {user_name}')
    poke_data = f"{pokemon['name'].capitalize()} captured with a height of {pokemon['height']} and weight of {pokemon['weight']}."

    return poke_data


def write_poke_data(data, user_name):
    """
    Write out pokemon data into a log book
    :param user_name: string - user name accepted from the user
    :param data: string - summary line of a pokemon
    """
    with open('Pokemon_Logbook.txt', 'a') as poke_file:
        data = f'{user_name}: {data}'
        poke_file.write(data + '\n')


def main():
    """
    Entry point of the pokemon script to summarise and log a pomekon from a user input
    """

    flag = True

    while flag:
        pokemon_number = input("What is the Pokemon's ID? Type exit to close program: ")
        user_name = input('What is your username? ')

        # if exit then close program
        if pokemon_number == 'exit':
            print("Goodbye!")
            flag = False

        # run a request to pokemon api to get pokemon summary
        poke_data= pokemon_id_request(pokemon_number, user_name)

        # log summary into log book
        write_poke_data(poke_data, user_name)



if __name__ == '__main__':
    #  run app
    main()






""""
STRING SLICING
"""

#idx  0123456
# slicing is inclusive - exclusive
msg = "I am learning to code with CFG!"

# slice at specific indexes inclusive - exclusive
print(msg[2:5])
# takt n number of characters from the back
print(msg[-4:])
# slice and add a step to the slicing
print(msg[5:13:2])
# get the first few characters
print(msg[:5])
# get the last few character
print(msg[-5:])
# reverse a string
print(msg[::-1])






















