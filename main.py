from contacts import add_contact, get_contacts

contacts = get_contacts()

for contact in contacts:
    print(contact)

name = input("Name: ")
email = input("Email: ")

add_contact(name, email)

print("Contact added")