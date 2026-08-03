from contacts import (
    add_contact,
    get_contacts,
    update_contact_name,
    update_contact_email,
    update_contact_name_email,
    delete_contact
)


from phone_numbers import (
    add_phone_number,
    get_phone_numbers,
    update_phone_number,
    delete_phone_number
)


from utils import (
    validate_integer
)

def show_menu():

    print(
        "\nEnter 1 to add contact"
        "\nEnter 2 to show contacts"
        "\nEnter 3 to update contact"
        "\nEnter 4 to delete contact"
        "\nEnter 5 to add phone number"
        "\nEnter 6 to show phone numbers"
        "\nEnter 7 to update phone number"
        "\nEnter 8 to delete phone number"
        "\nEnter 9 to exit program"
    )


def display_contacts():

    contacts = get_contacts()
    if not contacts:
        print("\nNo contacts")
        return False
    for contact in contacts:
        print(
            f"\nID: {contact[0]}"
            f"\nContact name: {contact[1]}"
            f"\nContact email: {contact[2]}"
        )
    return True

def display_phone_numbers(contact_id):

    phone_numbers = get_phone_numbers(contact_id)
    if not phone_numbers:
        print("\nNo phone numbers")
        return False
    for phone in phone_numbers:
        print(
            f"\nID: {phone[0]}"
            f"\nNumber: {phone[1]}"
            f"\nType: {phone[2]}"
        )
    return True


def handle_result(result):

    if result == "success":
        print("\nSuccess")
    elif result == "invalid_input":
        print("\nInput cannot be empty")
    elif result == "duplicate_email":
        print("\nEmail already exists")
    elif result == "contact_not_found":
        print("\nContact wasn't found")
    elif result == "phone_number_not_found":
        print("\nPhone number wasn't found")


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

            contact_id = input("\nEnter contact ID you want to update here: ")
            if not validate_integer(contact_id):
                print("\nInvalid input")
                continue
            contact_id = int(contact_id)
            
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

            contact_id = input("\nEnter contact ID you want to delete here: ")
            if not validate_integer(contact_id):
                print("Invalid input")
                continue
            contact_id = int(contact_id)

            result = delete_contact(contact_id)
            handle_result(result)


        elif menu_choice == '5':

            if not display_contacts():
                continue
    
            contact_id = input("\nEnter contact ID you want to add a phone number to here: ")
            if not validate_integer(contact_id):
                print("Invalid input")
                continue
            contact_id = int(contact_id)

            phone_number = input("\nEnter phone number here: ")
            phone_type = input("Enter phone type here: ")
            result = add_phone_number(contact_id, phone_number, phone_type)
            handle_result(result) 


        elif menu_choice == '6':

            if not display_contacts():
                continue

            contact_id = input("\nEnter contact ID to view phone numbers for here: ")
            if not validate_integer(contact_id):
                print("Invalid input")
                continue
            contact_id = int(contact_id)

            if not display_phone_numbers(contact_id):
                continue


        elif menu_choice == '7':

            if not display_contacts():
                continue

            contact_id = input("\nEnter contact ID to update phone number for here: ")
            if not validate_integer(contact_id):
                print("Invalid input")
                continue
            contact_id = int(contact_id)

            if not display_phone_numbers(contact_id):
                continue

            phone_id = input("\nEnter phone ID to update here: ")
            if not validate_integer(phone_id):
                print("Invalid input")
                continue
            phone_id = int(phone_id)    

            new_number = input("\nEnter new phone number here: ")
            new_phone_type = input("Enter new phone type here: ")
            result = update_phone_number(phone_id, new_number, new_phone_type)
            handle_result(result)


        elif menu_choice == '8':

            if not display_contacts():
                continue

            contact_id = input("\nEnter contact ID to delete phone number for here: ")
            if not validate_integer(contact_id):
                print("Invalid input")
                continue
            contact_id = int(contact_id)

            if not display_phone_numbers(contact_id):
                continue

            phone_id = input("\nEnter phone ID to delete here: ")
            if not validate_integer(phone_id):
                print("Invalid input")
                continue
            phone_id = int(phone_id)

            result = delete_phone_number(phone_id)
            handle_result(result)

            
        elif menu_choice == '9':
            
            print("\nQuitting")
            break


if __name__ == "__main__":
    menu()