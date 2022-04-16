# from create_project import create
# from view_projects import view
# from edit_project import edit
# from delete_projects import delete
# from search_project import search
# import create_project
import json


def menu(user_id):
    print(
        "\n\n 1) Create Project \n 2) View All Projects \n 3) Edit Project \n 4) Delete Project \n 5) Search For Project")

    choise = input("\nPlease choose from menu :\n")
    if choise == "1":
        from create_project import create
        create(user_id)

    elif choise == "2":
        from view_projects import view
        view(user_id)

    elif choise == "3":
        from edit_project import edit
        edit(user_id)

    elif choise == "4":
        from delete_project import delete
        delete(user_id)

    elif choise == "5":
        from search_project import search
        search(user_id)
    else:
        print("\nPlease choose From menu")
    menu(user_id)