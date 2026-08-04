from contacts import (
    add_contact,
    update_contact_name,
    update_contact_email,
    update_contact_name_email,
    delete_contact
)


from phone_numbers import (
    add_phone_number,
    update_phone_number,
    delete_phone_number
)


from ui import (
    show_menu,
    display_contacts,    
    display_phone_numbers,
    handle_result,
    get_id_input
)


from utils import parse_integer



def menu():

    while True:

        show_menu()
        menu_choice = input("\nEnter here: ")
        if menu_choice not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print("\nInvalid menu input")
            continue


        if menu_choice == '1':

            name = input("\nEnter name here: ")
            email = input("Enter email here: ")
            result = add_contact(name, email)
            handle_result(result)

        elif menu_choice == '2':

            display_contacts()


        elif menu_choice == '3':

            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID you want to update here: ")
            if contact_id is None:
                continue

            print(
                "\nEnter 1 to update contact name"
                "\nEnter 2 to update contact email"
                "\nEnter 3 to update contact name and email"
            )
            update_choice = input("\nEnter here: ")
            if update_choice not in ('1', '2', '3'):
                print("\nInvalid choice input")
                continue

            if update_choice == '1':
                new_name = input("\nEnter new name here: ")
                result = update_contact_name(contact_id, new_name)
                handle_result(result)
                
            elif update_choice == '2':
                new_email = input("\nEnter new email here: ")
                result = update_contact_email(contact_id, new_email)
                handle_result(result)

            elif update_choice == '3':
                new_name = input("\nEnter new name here: ")
                new_email = input("Enter new email here: ")
                result = update_contact_name_email(contact_id, new_name, new_email)
                handle_result(result)


        elif menu_choice == '4':

            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID you want to delete here: ")
            if contact_id is None:
                continue

            result = delete_contact(contact_id)
            handle_result(result)


        elif menu_choice == '5':

            if not display_contacts():
                continue
    
            contact_id = get_id_input("\nEnter contact ID you want to add a phone number to here: ")
            if contact_id is None:
                continue

            phone_number = input("\nEnter phone number here: ")
            phone_type = input("Enter phone type here: ")
            result = add_phone_number(contact_id, phone_number, phone_type)
            handle_result(result) 


        elif menu_choice == '6':

            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID to view phone numbers for here: ")
            if contact_id is None:
                continue

            if not display_phone_numbers(contact_id):
                continue


        elif menu_choice == '7':

            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID to update phone number for here: ")
            if contact_id is None:
                continue
            
            if not display_phone_numbers(contact_id):
                continue

            phone_id = get_id_input("\nEnter phone ID to update here: ")
            if phone_id is None:
                continue    

            new_number = input("\nEnter new phone number here: ")
            new_phone_type = input("Enter new phone type here: ")
            result = update_phone_number(phone_id, new_number, new_phone_type)
            handle_result(result)


        elif menu_choice == '8':

            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID to delete phone number for here: ")
            if contact_id is None:
                continue

            if not display_phone_numbers(contact_id):
                continue

            phone_id = get_id_input("\nEnter phone ID to delete here: ")
            if phone_id is None:
                continue

            result = delete_phone_number(phone_id)
            handle_result(result)


        elif menu_choice == '9':
            
            print("\nQuitting")
            break


if __name__ == "__main__":
    menu()