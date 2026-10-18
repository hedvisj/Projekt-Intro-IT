def splash():
    print()
    print("~~~~~~~~~~~~~~~~~~~~")
    print("      Biathlon      ")
    print(" A hit or miss game ")
    print("~~~~~~~~~~~~~~~~~~~~")
    print()
    print("You got 5 shots")

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

def gissa(mördare_dict):
# if input() in mördare_dict[] så har man gissat rätt


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


def main():
    spelplan1 = {
        "Story" : {"Det har skett ett mord....."},

        "Mördare" : {"Mördare":"Trädgårdsmästaren", "mordvapen":"Kniv från köket"},

        "Trädgården" : {"Trädgårdsmästaren":["Jag plockade ogräs", "Nervös"], "Ledtrådar":["Det är ogräs i alla rabatter", "En kratta ligger på backen"]},

        "Garaget" : {"Stefan":["Hej", "Ser ut som han inte sovit"], "Ledtrådar":["x", "y"]}, 

        "Köket": {"Kocken":["Lagade mat, råka skära mig whoops", "Hon har blod på ärmen"], "Ledtrådar":["a", "b"]}
    }
    options = {"l":"Leta efter ledtrådar", "g":"Gissa"}
    while True:
        splash()
        if menu("\nNyckel till värde i dict med story!\n", "\nOption: ", options) != "l":
            print("\nQuitting...\n")
            break
        #user = login(users)
        #if user == None:
            #print("\nYou are logged out")
            #continue
        #user_actions(user, data)
            

main()