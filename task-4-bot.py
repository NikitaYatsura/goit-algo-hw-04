import re

# func whic checking coorect input data such as correct name and phone number
def check_correct_data(data):
    if re.fullmatch(r"[a-z]+", data[0]) and \
        re.fullmatch(r"((\+38067)|(\+38068)|(\+38096)|(\+38097)|(\+38098)|(\+38077)| \
                     (\+38050)|(\+38066)|(\+38095)|(\+38099)|(\+38075)| \
                     (\+38063)|(\+38073)|(\+38093)| \
                     (\+38089)|(\+38094)|(\+38020))(\d{7})", data[1]):
        return True
    
    else:
        print("Incorrect phone or name")
        return False

# func for input
def paser_input():
    return input("How can I help you? ").lower().split() 

#func for add the contact to the dict
def add_contact(data, contacts_dict):
    name, phone = data

    # checking if the contact is allready exist in dict
    if name in contacts_dict.keys():
        print("User exist")

    else:
        contacts_dict[name] = phone
        print("User added")

# func for change the contacts in the dict
def change_contact(data, contacts_dict):

    #checking exist the contact
    if data[0] in contacts_dict.keys():
        contacts_dict[data[0]] = data[1]
        print("Contact update")
        return contacts_dict
    
    #checking if user input a phone number not only name
    elif not data[1]:
        print("Miss phone number")

    else:
        print("Contact doesn't exist")       

# func for display a specified contact's phone number
def show_phone(data, contacts_dict):
    print(f"phone: {contacts_dict[data[0]]}")

# func for display all strings in dict
def show_all(contacts_dict):
    for k, v in contacts_dict.items():
        print(f"{k}: {v}")


def main():
    contacts_dict = dict() # create dict for safe data 
    start_bot = input("Input a command ").lower() # input command (hellow) which activate the bot

    if start_bot == "hello": # check if input coomand is matches to command which activate bot

        while True:

            try:                          
                command, *args = paser_input() # devide input string on command and data which will be safe in the dict

                if command == "add" or command == "change" or command == "phone": # check correct command

                    # check that input data will be not more args (name and phone number) 
                    # and correct (only name and correct phone number)
                    if args and len(args) <= 2 and check_correct_data(args):

                        match command: # check when input data exist command and data for dict
                            case "add": # when command "add"
                                add_contact(args, contacts_dict)
                            case "change": # when command "change"
                                change_contact(args, contacts_dict)
                            case "phone": # when command "phone"
                                show_phone(args, contacts_dict)          
                         
                    else:
                        print("ERROR! Try again!")
                        continue

                elif command == "exit" or command == "close": #check for close the bot
                    print("Good bye")
                    break 
                
                elif command == "all": # check for display all data in the dict
                    show_all(contacts_dict)

                else:
                    print("ERROR! Incorrect command") 
                    
            except (IndexError, KeyError):
                print("The dict is empty")

            except ValueError:
                print("ERROR! Input a command")


    elif  start_bot == "bay": # check if input coomand is matches to command which close bot
        print("Good bay")


    else: # if command doesn't matches any value
        print("I don't understand you")    



if __name__ == "__main__":
    
    main()
    