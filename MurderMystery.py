house = {
    "murderer":"The Gardener",
    "start":'''Welcome to blackwood manor, the manor of the wealthy lord John of Blackwood. 
    \nAn hour ago John was brutally murdured in his own garage. \nYour job is to find out who the murderer is. \nYou will go room to room gathering clues, questioning the suspects, \nand taking notes in your journal. \nBut be careful, not all of them are telling the truth! \nYou only have one guess, so be sure. \nGood luck!\n''',
    "ending":
  '''The Gardener was the murderer. He murdered John in the garage with a pitchfork while the caretaker was repairing the sprinklers. He then deeply cleaned the pitchfork and put it back outside the shed.\n''',
    "1": {
        "name": "The garden",
        "description": 
      '''In the garden the sprinklers are on and the lawn is shining. The flowers in the flowerbed are all well taken care of. There is a bunch of gardening tools lined up against the wall of the shed, a dirty shovel, a pitchfork and a broken rake. The garderner is picking weeds from the flowerbed.\n''',
      	"person": {
          "name":"The Gardener",
          "alibi": "Gardener: I was picking weeds from the flowerbed when John was murdered. And now I'm picking weeds because it makes me feel calm\n",
          "temper":"The gardener seems calm and collected, yet when he answers your questions he is still looking at the weeds.\n",
          "overall":"The Gardener's overall is covered in dirt\n",
          "button":"The Gardener is missing one of the red buttons on his overall\n",
          "occupation":"The Gardener is picking weeds and putting them into a basket.\n",
          "stain": "The Gardener has a red stain on his overall, but he says its from the beetrots\n",
        },
        "clues": {
            "name": "The garden",
            "footprints":"Muddy footprints can be seen exiting the shed.\n",
            "pitchfork": "The pitchfork is looking newly polished, compared to the other tools.\n",
            "flower":"The flowers are very pretty\n",
          	"shed": "The shed has a broken window, but no glass shards around it can be found\n",
          	"shovel": "The shovel has a large dent in it\n",
            "sprinklers":"The sprinklers are on\n"
        }
    },

    "2": {
        "name": "The kitchen",
      	"description": "The Chef is sitting on a chair with her head in her palms, the kitchen is a bit messy from the cooking. Through the window you can see the beautiful garden.\n",
      
        "person": {
          	"name": "The Chef",
          	"alibi": "Chef: I was cutting onions for John's onion soup when he died. It was his favourite. I accidentaly cut myself but I am fine.\n",
            "temper":"The Chef's gaze wanders while she is answering your questions.\n",
            "sleeve":"You notice that the Chef twists her sleeve while talking. Maybe it's because she's nervous.\n",
            "blood": "The white sleeves of her chefs-jacket are stained red, looking like blood.\n",
            "temper":"The Chef is very sad\n"
        },
        "clues": {
            "name":"The kitchen",
            "Window":"On the window sill there is a photograph of John\n",
            "Stove": "There are onion skin in front of the stove on the floor\n",
          	"knives":"All the knives are cleaned and in the knife rack\n"

    
        }
    },

    "3": {
        "name": "The Garage",
      	"description": "The garage is very messy with a big jeep in the middle of the garage, the Caretaker leans against the jeep looking at you.\n",
        "person": {
          	"name": "The Caretaker",
          	"alibi": "Caretaker: I was repairing the sprinkler system when John died. I didn't notice anyone else in the garden, but I was also very focused on the repair.\n",
            "keys": "The Caretaker has a keychain full of keys.\n",
            "temper": "The Caretaker seems to be very nervous\n",
            "wet":"The Caretaker has wet stains on his clothes, but the dark fabric hides the color of the stains.\n",
        },
        "clues": {
            "name": "The Garage",
            "John": "John is laying on the floor. You check the damage to his body. The only noticeable thing is 4 equally sized holes in a straight line across his chest. That must have been the cause of death.\n",
            "tools": "A lot of different tools are hanging on a wall.\n",
            "button":"A red button is laying next to John's body\n",
            "door":"The garage door is open\n", 
            "toolbox":"A toolbox is sitting on top of the workbench\n"
        }
    }
}

journal = []

def splash(context):
    print("\033c", end="") 
    print("             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n      				MurderTime     		 		 \n 				A Murder Mystery game 			 \n             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(context)

def view(title,options):
    print(title)
    if type(options) == dict:   
        for n in options:
                print(f"{n}) {options[n]}")
    else:                            
        for n in options:
            print(f"{n}")

def menu(title, prompt, options):
    view(title, options)
    while True:
        choice = input(prompt)
        if choice in options:
            break
        else:
            print(f"\n{choice} is not an option\n")
            continue
    print(f"You chose {options[choice]}")
    print("\033c", end="") 
    return choice

def guess(dicts, murderer):
    options = {"1":dicts["1"]["person"]["name"], "2":dicts["2"]["person"]["name"], "3":dicts["3"]["person"]["name"]}
    print("\nHere are your journal entries:\n")
    print("\n".join(journal) + "\n")
    if options[menu("\nYou want to guess the murder!\nThese are your options:\n ", "\nGuess: ", options)] == murderer:
        print(f"\n \nYou guessed right! {dicts["murderer"]} is the murder.\n")
        print(dicts["ending"])
    else:
        print("\n \n You guessed wrong! GAME OVER!!!\n \n")

def display(nr, value, dicts):
    for n in dicts[nr][value]:
        if n == "name":
            continue
        print(dicts[nr][value][n])
        choice = input("Do you want to write this in your journal? y/n ")
        if choice == "y":
            journal.append(dicts[nr][value][n])
            print("\nYou made a note in your journal\n")

def search():
    val = menu("Which room do you want to enter?: \n", "Choose: ", {"1": house["1"]["name"], "2": house["2"]["name"], "3": house["3"]["name"]})
    rum = house[val]
    print(f"\nYou walk into {rum["name"]}, there you see: {rum["description"]}\n")
    
    steg1 = {"1": "Question the person in the room","2": "Search the room for clues", "3": "Leave the room"}
    while True:
        x = menu(f"Do you want to question the person in the room, search the room for clues or exit {rum["name"]}? \n", "Choose 1-3: ", steg1)
        if x == "1": 
            display(val, "person", house)
            continue
        elif x == "2":
            display(val,"clues",house)
            continue
        elif x == "3":
            break
        else:
            print("Not an option, try again\n")

def main(dicts):
    options = {"1":"Search for clues", "2":"Guess the murderer"}
    splash(dicts["start"])
    while True:
        if menu("\nYou now have the options to either \n", "What do you want to do? ", options) == "2":
            guess(dicts, dicts["murderer"])
            break
        else:
            search()
    

       
main(house)
