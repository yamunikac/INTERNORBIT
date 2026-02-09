# Task 2: Phone Book / Contact Management System
# InternOrbit Python Programming Internship


contacts = {}  

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}")

def search_contact():
    search = input("Enter name or phone number to search: ")
    found = False

    for name, details in contacts.items():
        if search == name or search == details["Phone"]:
            print("\nContact Found:")
            print("Name:", name)
            print("Phone:", details["Phone"])
            print("Email:", details["Email"])
            print("Address:", details["Address"])
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")

    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")

        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email
        contacts[name]["Address"] = address

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

while True:
    print("\n==============================")
    print("        CONTACT BOOK          ")
    print("==============================")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using the Contact Book!")
        break
    else:
        print("Invalid choice. Please try again.")
