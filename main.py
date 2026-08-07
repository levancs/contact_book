from contacts import (
    add_contact,
    update_contact_name,
    update_contact_email,
    update_contact_name_email,
    delete_contact,
)
from phone_numbers import (
    add_phone_number,
    update_phone_number,
    delete_phone_number
)
from tags import (
    add_tag,
    assign_tag,
    delete_tag,
    delete_tag_from_contact
)
from ui import (
    show_main_menu,
    show_contact_menu,
    show_phone_number_menu,
    show_tag_menu,
    show_search_menu,
    display_contacts,
    display_contacts_by_name,
    display_contacts_by_email,
    display_contacts_by_phone_number,
    display_contacts_by_tag,
    display_phone_numbers,    
    display_phone_numbers_by_contact,
    display_tags,
    display_tags_by_contact,
    handle_result,
    get_id_input
)




def contact_menu():

    while True:

        show_contact_menu()
        contact_menu_choice = input("\nEnter here: ")
        if contact_menu_choice not in ('1', '2', '3', '4', '5'):
            print("Invalid contact menu input")
            continue


        if contact_menu_choice == '1':

            name = input("\nEnter name here: ")
            email = input("Enter email here: ")
            result = add_contact(name, email)
            handle_result(result)


        elif contact_menu_choice == '2':
        
            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID you want to update here: ")
            if contact_id is None:
                continue

            print(
                "\n1. Update contact name"
                "\n2. Update contact email"
                "\n3. Update contact name and email"
            )
            contact_update_choice = input("\nEnter here: ")
            if contact_update_choice not in ('1', '2', '3'):
                print("\nInvalid contact update choice input")
                continue

            if contact_update_choice == '1':
                new_name = input("\nEnter new name here: ")
                result = update_contact_name(contact_id, new_name)
                handle_result(result)
                
            elif contact_update_choice == '2':
                new_email = input("\nEnter new email here: ")
                result = update_contact_email(contact_id, new_email)
                handle_result(result)

            elif contact_update_choice == '3':
                new_name = input("\nEnter new name here: ")
                new_email = input("Enter new email here: ")
                result = update_contact_name_email(contact_id, new_name, new_email)
                handle_result(result)
        

        elif contact_menu_choice == '3':

            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID you want to delete here: ")
            if contact_id is None:
                continue

            result = delete_contact(contact_id)
            handle_result(result)


        elif contact_menu_choice == '4':

            display_contacts()


        elif contact_menu_choice == '5':

            break

            

            
def phone_number_menu():

    while True:
        show_phone_number_menu()
        phone_number_menu_choice = input("\nEnter here: ")
        if phone_number_menu_choice not in ('1', '2', '3', '4', '5', '6'):
            print("\nInvalid phone number menu input")
            continue


        if phone_number_menu_choice == '1':

            if not display_contacts():
                continue
    
            contact_id = get_id_input("\nEnter contact ID you want to add a phone number to here: ")
            if contact_id is None:
                continue

            phone_number = input("\nEnter phone number here: ")
            phone_type = input("Enter phone type here: ")
            result = add_phone_number(contact_id, phone_number, phone_type)
            handle_result(result)


        elif phone_number_menu_choice == '2': 

            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID to update phone number for here: ")
            if contact_id is None:
                continue
            
            if not display_phone_numbers_by_contact(contact_id):
                continue

            phone_id = get_id_input("\nEnter phone ID to update here: ")
            if phone_id is None:
                continue  

            new_number = input("\nEnter new phone number here: ")
            new_phone_type = input("Enter new phone type here: ")
            result = update_phone_number(phone_id, new_number, new_phone_type)
            handle_result(result)


        elif phone_number_menu_choice == '3':

            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID to delete phone number for here: ")
            if contact_id is None:
                continue

            if not display_phone_numbers_by_contact(contact_id):
                continue

            phone_id = get_id_input("\nEnter phone ID to delete here: ")
            if phone_id is None:
                continue

            result = delete_phone_number(phone_id)
            handle_result(result)


        elif phone_number_menu_choice == '4':

            display_phone_numbers()


        elif phone_number_menu_choice == '5':

            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID to view phone numbers for here: ")
            if contact_id is None:
                continue

            display_phone_numbers_by_contact(contact_id)


        elif phone_number_menu_choice == '6':

            break




def tag_menu():

    while True:
        show_tag_menu()
        tag_menu_choice = input("\nEnter here: ")
        if tag_menu_choice not in ('1', '2', '3', '4', '5', '6', '7'):
            print("\nInvalid tag menu choice")
            continue


        if tag_menu_choice == '1':

            tag_name = input("\nEnter a name for a new tag: ")
            result = add_tag(tag_name)
            handle_result(result)


        elif tag_menu_choice == '2':

            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID to assign a tag to here: ")
            if contact_id is None:
                continue

            if not display_tags():
                continue

            tag_id = get_id_input("\nEnter tag ID to assign here: ")
            if tag_id is None:
                continue

            result = assign_tag(contact_id, tag_id)
            handle_result(result)


        elif tag_menu_choice == '3':

            if not display_tags():
                continue

            tag_id = get_id_input("\nEnter tag ID to delete here: ")
            if tag_id is None:
                continue

            result = delete_tag(tag_id)
            handle_result(result)


        elif tag_menu_choice == '4':

            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID to delete a tag from here: ")
            if contact_id is None:
                continue

            if not display_tags():
                continue

            tag_id = get_id_input("\nEnter tag ID to delete from this contact here: ")
            if tag_id is None:
                continue

            result = delete_tag_from_contact(contact_id, tag_id)
            handle_result(result)


        elif tag_menu_choice == '5':

            display_tags()


        elif tag_menu_choice == '6':

            if not display_contacts():
                continue

            contact_id = get_id_input("\nEnter contact ID to view tags for here: ")
            if contact_id is None:
                continue

            display_tags_by_contact(contact_id)


        elif tag_menu_choice == '7':

            break




def search_menu():

    while True:
        show_search_menu()
        search_menu_choice = input("\nEnter here: ")
        if search_menu_choice not in ('1', '2', '3', '4', '5'):
            print("\nInvalid search menu choice")
            continue


        if search_menu_choice == '1':

            name = input("\nEnter name to search for here: ")
            display_contacts_by_name(name)


        elif search_menu_choice == '2':

            email = input("\nEnter email to search for here: ")
            display_contacts_by_email(email)


        elif search_menu_choice == '3':

            phone_number = input("\nEnter phone number to search for here: ")
            display_contacts_by_phone_number(phone_number)


        elif search_menu_choice == '4':

            tag_name = input("\nEnter tag name to search for here: ")
            display_contacts_by_tag(tag_name)


        elif search_menu_choice == '5':

            break




def menu():

    while True:

        show_main_menu()
        main_menu_choice = input("\nEnter here: ")
        if main_menu_choice not in ('1', '2', '3', '4', '5'):
            print("\nInvalid main menu input")
            continue


        if main_menu_choice == '1':

            contact_menu()


        elif main_menu_choice == '2':

            phone_number_menu()


        elif main_menu_choice == '3':

            tag_menu()

        elif main_menu_choice == '4':

            search_menu()

        elif main_menu_choice == '5':

            print("\nQuitting")
            break




if __name__ == "__main__":
    menu()