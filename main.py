from contacts import *


def show_menu():
    print(
        "\nEnter 1 to add contact"
        "\nEnter 2 to show contacts"
        "\nEnter 3 to update contact"
        "\nEnter 4 to delete contact"
        "\nEnter 5 to exit program"
    )


def menu():
    while True:
        show_menu()
        menu_choice = input("\nEnter here: ")


        if menu_choice == '1':
            name = input("\nEnter name here: ")
            email = input("Enter email here: ")
            add_contact(name, email)
            print("\nContact added")


        elif menu_choice == '2':
            contacts = get_contacts()
            if not contacts:
                print("No contacts")
                continue
            for contact in contacts:
                print(
                    f"\nID: {contact[0]}"
                    f"\nContact name: {contact[1]}"
                    f"\nContact email: {contact[2]}"
                )


        elif menu_choice == '3':
            contacts = get_contacts()
            if not contacts:
                print("No contacts")
                continue
            for contact in contacts:
               print(
                    f"\nID: {contact[0]}"
                    f"\nContact name: {contact[1]}"
                    f"\nContact email: {contact[2]}"
                ) 
            contact_id = int(input("\nEnter contact ID you want to update here: "))
            print(
                "\nEnter 1 to update contact name"
                "\nEnter 2 to update contact email"
                "\nEnter 3 to update contact "
            )
            update_choice = input("\nEnter here: ")
            if update_choice == '1':
                new_name = input("\nEnter new name here: ")
                update_contact_name(contact_id, new_name)
                print("\nContact name updated")
            elif update_choice == '2':
                new_email = input("\nEnter new email here: ")
                update_contact_email(contact_id, new_email)
                print("\nContact email updated")
            elif update_choice == '3':
                new_name = input("\nEnter new name here: ")
                new_email = input("Enter new email here: ")
                update_contact_name_email(contact_id, new_name, new_email)
                print("\nContact name and email updated")


        elif menu_choice == '4':
            contacts = get_contacts()
            if not contacts:
                print("No contacts")
                continue
            for contact in contacts:
                print(
                    f"\nID: {contact[0]}"
                    f"\nContact name: {contact[1]}"
                    f"\nContact email: {contact[2]}"
                )
            contact_id = input("\nEnter contact ID you want to delete here: ")
            delete_contact(contact_id)
            print("Contact deleted")
            
        elif menu_choice == '5':
            print("\nQuitting")
            break

menu()
