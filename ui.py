from contacts import (
    get_contacts,
    get_contacts_descriptive
)
from phone_numbers import (
    get_phone_numbers,
    get_phone_numbers_for_contact
)
from tags import (
    get_tags,
    get_tags_for_contact
)
from utils import parse_integer


def show_main_menu():

    print(
        "\n1. Contact options"
        "\n2. Phone number options"
        "\n3. Tag options"
        "\n4. Exit"
    )


def show_contact_menu():

    print(
        "\n1. Add contact"
        "\n2. Update contact"
        "\n3. Delete contact"
        "\n4. Show contacts"
        "\n5. Show descriptive contacts"
        "\n6. Go back"
    )


def show_phone_number_menu():

    print(
        "\n1. Add phone number"
        "\n2. Update phone number"
        "\n3. Delete phone number"
        "\n4. Show phone numbers"
        "\n5. Show phone numbers by contact"
        "\n6. Go back"
    )


def show_tag_menu():

    print(
        "\n1. Add tag"
        "\n2. Assign tag"
        "\n3. Delete tag"
        "\n4. Delete tag from contact"
        "\n5. Show tags"
        "\n6. Show tags by contact"
        "\n7. Go back"
    )


def display_contacts():

    contacts = get_contacts()
    if not contacts:
        print("\nNo contacts")
        return False
    for contact in contacts:
        print(
            f"\nContact ID: {contact[0]}"
            f"\nContact name: {contact[1]}"
            f"\nContact email: {contact[2]}"
        )
    return True


def display_contacts_descriptive():

    descriptive_contacts = get_contacts_descriptive()
    if not descriptive_contacts:
        print("\nNo contacts")
        return False
    for descriptive_contact in descriptive_contacts:
        print(
            f"\nContact ID: {descriptive_contact[0]}"
            f"\nContact name: {descriptive_contact[1]}"
            f"\nContact email: {descriptive_contact[2]}"
            f"\nPhone number ID: {descriptive_contact[3]}"
            f"\nPhone number: {descriptive_contact[4]}"
            f"\nPhone type: {descriptive_contact[5]}"
            f"\nTag ID: {descriptive_contact[6]}"
            f"\nTag name: {descriptive_contact[7]}"
        )


def display_phone_numbers():

    phone_numbers = get_phone_numbers()
    if not phone_numbers:
        print("\nNo phone numbers")
        return False
    for phone in phone_numbers:
        print(
            f"\nPhone number ID: {phone[0]}"
            f"\nContact ID: {phone[1]}"
            f"\nNumber: {phone[2]}"
            f"\nType: {phone[3]}"
        )
    return True


def display_phone_numbers_by_contact(contact_id):

    phone_numbers = get_phone_numbers_for_contact(contact_id)
    if not phone_numbers:
        print("\nNo phone numbers")
        return False
    for phone in phone_numbers:
        print(
            f"\nPhone number ID: {phone[0]}"
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
            f"\nTag ID: {tag[0]}"
            f"\nName: {tag[1]}"
        )
    return True


def display_tags_by_contact(contact_id):

    tags = get_tags_for_contact(contact_id)
    if not tags:
        print("\nNo tags")
        return False
    for tag in tags:
        print(
            f"\nTag ID: {tag[0]}"
            f"\nName: {tag[1]}"
        )
    return True


def handle_result(result):

    messages = {
        "success": "Success",
        "invalid_input": "Input cannot be empty",

        "duplicate_email": "Email already exists",
        "duplicate_phone_number": "Phone number already exists",
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

    if parse_integer(value) is None:
        print("\nInvalid ID")
        return None

    return int(value)