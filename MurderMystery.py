# ledtrådar = {
#     "lampan" : ["Lampan är trasig", "Lampan har blod på sig"]
# }

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
    "1": {
        "namn": "Trädgården", #MEN DET ÄR VINTER
        "person": "Trädgårdsmästaren",
        "alibi": "Jag vattnade rosorna",
        "attribut": "Har leriga skor",
        "ledtrådar": {
            "lampan": "Har blod på sig", 
            "golvet": "Blodfläck på golvet"
        }
    },

    "2": {
        "namn": "Garaget",
        "person": "Butlern",
        "alibi": "Jag tvättade bilen",
        "attribut": "Har en nyckelknippa",
        "ledtrådar": {
            "skorna": "Har lera på sig"
        }
    },

    "3": {
        "namn": "Köket",
        "person": "Kocken",
        "alibi": "Jag lagade middag",
        "attribut": "Har en nyckelknippa",
        "ledtrådar": {
            "skjortan": "Har en blodfläck"
        }
    }
}

def view(description,string):
    print(description)
    for key in string:
       print(f"{key}) {huset[key]["namn"]}")

#när man kommer till vardagsrummet Choices()
def Choices(huset):
    view("Välj ett alternativ", huset)
    
    #for x in huset:
    #    print(f"{x}) {huset[x]["namn"]}") # anropa view istället

    val = input("Vilket rum vill du gå till? 1-3 ")
    if val in huset:
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


