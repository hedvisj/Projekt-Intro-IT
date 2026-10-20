ledtrådar = { #prövar att fixa
    "lampan" : ["Lampan är trasig", "Lampan har blod på sig"]
}

Splashkontext = {"Blackwood Manor": 
            "Välkommen till Blackwood Manor, en miljardärs villa."
            "\nFör två dagar sedan skedde det ett mord här, ditt jobb är att lösa mysteriet."
            "\nDu kan undersöka olika rum i huset och samla ledtrådar."
            "\n Varje rum har en person som kan ge dig information, men var försiktig, inte alla talar sanning."
            "\n Lycka till!",

            # "Woodrow hights" : 
            # "Välkommen till Woodrow hights, en gammal sjukhusbyggnad."
            # "\nIgår skedde det ett mord här, ditt jobb är att lösa mysteriet."
            # "\nDu kan undersöka olika rum i huset och samla ledtrådar."
            # "\n Varje rum har en person som kan ge dig information, men var försiktig, inte alla talar sanning."
            # "\n Lycka till!"
             }
huset = {
    "rum1": {
        "namn": "Trädgården", #MEN DET ÄR VINTER
        "person": "Trädgårdsmästaren",
        "alibi": "Jag vattnade rosorna",
        "attribut": "Har leriga skor",
        "ledtrådar": {
            "lampan": "Har blod på sig", 
            "golvet": "Blodfläck på golvet"
        }
    },

    "rum2": {
        "namn": "Garaget",
        "person": "Butlern",
        "alibi": "Jag tvättade bilen",
        "attribut": "Har en nyckelknippa",
        "ledtrådar": {
            "skorna": "Har lera på sig"
        }
    },

    "rum3": {
        "namn": "Köket",
        "person": "Kocken",
        "alibi": "Jag lagade middag",
        "attribut": "Har en nyckelknippa",
        "ledtrådar": {
            "skjortan": "Har en blodfläck"
        }
    }
}
#när man kommer till vardagsrummet Choices()
def Choices(huset):
    for x in huset:
        print(f"{x}) {huset[x]["namn"]}") # anropa view istället

    val = input("Vilket rum vill du gå till? ")
    if val.strip().lower() in huset:
        rum = huset[val]

        print(f"\nDu går in i {rum["namn"]}")
        print(f"Där finns {rum["person"]}")
        print(f"{rum["person"]} säger: {rum["alibi"]}")

    else:
        print("Det rummet finns inte.")
Choices(huset)
inventory = [] #kanske för att samla ledtrådar 

def splash(): 
    print(Splashkontext({"Blackwood Manor"}))
    
def view(description,string):
    print(description)
    for key in string:
        print(f"{key} {string[key]}")

#1 är alibi
#2 är attribut
def clear(): #Den här kanske är smidig om vi vill rensa terminalen mellan rummen eller när man startar om spelet
  print("\033c", end="")

def main(): 
    options = {"l":"Leta efter ledtrådar", "g":"Gissa"}
    splash()
    view()
    print()
    clear()


