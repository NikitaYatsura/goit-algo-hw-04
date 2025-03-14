# func for input
def parse_input(input_str):
    return input_str.lower().split() 

#func for add the contact to the dict
def add_contact(data, contacts_dict):
    name, phone = data

    # checking if the contact is allready exist in dict
    if name in contacts_dict.keys():
        return "User exist"

    else:
        contacts_dict[name] = phone
        return "User added"

# func for change the contacts in the dict
def change_contact(data, contacts_dict):

    #checking exist the contact
    if data[0] in contacts_dict.keys():
        contacts_dict[data[0]] = data[1]
        return "Contact change"
    
    else:
        return "Contact doesn't found"      

# func for display a specified contact's phone number
def show_phone(data, contacts_dict):
    if data[0] in contacts_dict.keys():
        return (f"phone: {contacts_dict[data[0]]}")

# func for display all strings in dict
def show_all(contacts_dir, str = ""):
    for k, v in contacts_dir.items():
        str += f"{k}:{v} \n"
    return str


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    try:    
        while True:
            
            input_str = input("How can I help you? ")
            command, *args = parse_input(input_str)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                continue
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.")

    except (IndexError, KeyError):
                print("The dict is empty")

    except ValueError:
                print("ERROR! Input a command")

if __name__ == "__main__":
    main()
                    
           
