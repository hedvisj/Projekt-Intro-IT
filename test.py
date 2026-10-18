def view(title,options):
    print(title)
    if type(options) == dict:        #if options is a dict, then print items preceeded by the keys
        for n in options:
                print(f"{n}) {options[n]}")
    else:                            #if options is something else (list), then print items preceeded by numbers
        index = 0
        for n in options:
            print(f"{index + 1}) {n}")
            index += 1

def add(prompt, string):
    string.append(input(prompt)) 
    return string

def menu(title, prompt, options):
    view(title, options)
    while True:
        choice = input(prompt)
        if choice in options:
            break
        else:
            print(f"\n{choice} is not an option")
            continue
    return choice

def user_actions(user, items):
    options = {"a":"Add Item", "l":"List Item", "q":"Quit"}
    print(f"\nWelcome {user}!\n")
    view("These are your items\n", items[user])
    while True:
        action = menu("\nselect an action\n", "\nOption: ", options)
        if action == "a":
            add("\nAdd Item: ", items[user])
        elif action == "l":
            view("These are your items\n", items[user])
        else:
            print(f"\nGoodbye {user}, your following items are stored: {", ".join(items[user])}")
            return items

def login(users):
    while True:
        user = input("\nUser: ")
        password = input("\nPassword: ")
        if user in users and password == users[user]:
            return user
        elif menu("\nInvalid username or password\n", "\nAction: ", {"r":"Try again", "q":"Quit"}) != "r":
            return None

def main():
    users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
    data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}
    options = {"l":"Leta efter ledtrådar", "g":"Gissa"}
    while True:
        if menu("\nWelcome to lagra!\n", "\nOption: ", options) != "l":
            print("\nQuitting...\n")
            break
        user = login(users)
        if user == None:
            print("\nYou are logged out")
            continue
        user_actions(user, data)
            

main()