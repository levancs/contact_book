from contacts import get_contacts
from phone_numbers import get_phone_numbers
from tags import get_tags
from utils import parse_integer


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
        "\nEnter 9 to add tag"
        "\nEnter 10 to show tags"
        "\nEnter 11 to assign tag"
        "\nEnter 12 to delete tag"
        "\nEnter 13 to exit program"
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


def display_tags():

    tags = get_tags()
    if not tags:
        print("\nNo tags")
        return False
    for tag in tags:
        print(
            f"\nID: {tag[0]}"
            f"\nName: {tag[1]}"
        )
    return True


def handle_result(result):

    messages = {
        "success": "Success",
        "invalid_input": "Input cannot be empty",
        "duplicate_email": "Email already exists",
        "duplicate_tag": "Tag already exists",
        "tag_already_assigned": "Tag already assigned",
        "contact_not_found": "Contact wasn't found",
        "tag_not_found": "Tag wasn't found",
        "contact_or_tag_not_found": "Contact/Tag wasn't found",
        "phone_number_not_found": "Phone number wasn't found"
    }

    print(f"\n{messages.get(result, 'Unknown error')}")


def get_id_input(prompt):
    value = input(prompt)

    if not parse_integer(value):
        print("\nInvalid ID")
        return None

    return int(value)