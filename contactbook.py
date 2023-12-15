import json

# Store contact data in a dictionary
contacts = {}

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def load_contacts():
    with open('contacts.json', 'r') as file:
        global contacts
        contacts = json.load(file)

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts()

def view_contact_list():
    for name, details in contacts.items():
        print(f"{name} - {details['phone']}")

def search_contact():
    search = input("Enter search term: ")
    for name, details in contacts.items():
        if search.lower() in name.lower() or search.lower() in details['phone'].lower():
            print(f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n")

def update_contact():
    name = input("Enter contact name: ")
    if name in contacts:
        print("Current details:")
        print(f"Phone: {contacts[name]['phone']}\nEmail: {contacts[name]['email']}\nAddress: {contacts[name]['address']}\n")
        action = input("Would you like to update phone, email, or address? ")
        if action.lower() == "phone":
            contacts[name]['phone'] = input("Enter new phone number: ")
        elif action.lower() == "email":
            contacts[name]['email'] = input("Enter new email address: ")
        elif action.lower() == "address":
            contacts[name]['address'] = input("Enter new address: ")
        save_contacts()
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name: ")
    if name in contacts:
        del contacts[name]
        save_contacts()
    else:
        print("Contact not found.")

while True:
    action = input("Would you like to add, view, search, update, delete, or exit? ")
    if action.lower() == "add":
        add_contact()
    elif action.lower() == "view":
        view_contact_list()
    elif action.lower() == "search":
        search_contact()
    elif action.lower() == "update":
        update_contact()
    elif action.lower() == "delete":
        delete_contact()
    elif action.lower() == "exit":
        break
    else:
        print("Invalid action. Please try again.")
