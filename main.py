contact = {}

def showFunction():
    print(contact.items())
    print("Name \t contact")
    for key in contact:
        print("{} \t {}".format(key,contact.get(key)))
while True:

    choice = int(input("1. Add new Contact \n"
                       "2. Search the Contact \n" 
                       "3. Display the Contact \n" 
                       "4. Edit the Contact \n" 
                       "5. Delete the Contact \n" 
                       "6. Exit \n"
                       "Please Write Number Between 1-6: "))
    if choice == 1:
        name = input("Add Your Contact Name: ")
        phone = int(input("Add your Phone Number: "))
        contact[name] = phone
    
    elif choice == 2:
        contactName = input("Search the Contact: ")
        if contactName in contact:
            print(contactName, "Contact number is  ", contact[contactName])
        else:
            print("Not Found the contact")

    elif choice == 3: 
        if not contact:
            print("Contact book is empty")
        else:
            showFunction()

    elif choice == 4:
        EditContact = input("Edit your contact: ")
        if EditContact in contact:
            phone = input("change your number: ")
            contact[EditContact] = phone
            print("contact Updated Successfully ")
            showFunction()
        else:
            print("Name is Not Found")

    elif choice == 5:
        Delete_contact = input("Whice contact Do you want to Delete?: ")
        if Delete_contact in contact:
            deleteConfirm = input("Do you want to delete this contact [y/n]")
            if deleteConfirm == "y" or deleteConfirm == "Y":
                contact.pop(Delete_contact)

            showFunction()
        else:
            print("The name is not found in the contact")

    else:
        break