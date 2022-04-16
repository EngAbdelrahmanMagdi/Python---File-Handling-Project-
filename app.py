from pathlib import Path
from register import registartion
from login import *
import json



print("Please choose registration or login : \n 1) Registration \n 2) Login")
first_choise = input("If there is the first time to login my app choose Register : \n")


if first_choise == "1":

    mypath = Path("D:\Programming\Python\Python Labs\Day02\Lab02\Crowd Funding Console app/users_data.json")
    list = []
    with open('users_data.json') as json_file:
        if mypath.stat().st_size == 0:
            user_id = 0
        else :

            for line in json_file:
                Dict = json.loads(line)
                list.append(Dict)
            json_file.close()
            last_index= len(list)-1
            last_dict= list[last_index]
            user_id = last_dict['user_id']

        registartion(user_id)
        menu(user_id)

elif first_choise == "2":
    login_app()
else:
    print("\nPlease choose From menu")
