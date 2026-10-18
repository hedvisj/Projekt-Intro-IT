import random

attribut = {"Personliga ": ["Blod på skjortan", "leriga skor", "Har en nyckel", "Borde gå hem"],
            "Plats": ["Finns en blodfläck här", "Ligger en knapp på golvet", "En låst dörr"]}

Personer = {
    "Namn": ["Pelle", "Niklas", "Frank", ]}
# vardagsrummet = {
#     "Personer": ["Erik", "Anton"],
#     "attribut": ["Snäll", "arg" ]} 
# köket = {
#     "Personer": ["Pelle", "Niklas"],
#     "attribut": ["Snäll", "arg" ]} 

# def call(rum):
#     print(f"({rum["Personer"][randint(0,1)]} är {rum["attribut"][randint(0,1)]}")

# huset = {"Hallen": hallen,
#          "vardagsrummet": vardagsrummet,
#           "Köket" : köket}
# print(call(rum = input("Vilket rum: ")))


person = random.choice(Personer["Namn"])
egenskap = random.choice(attribut["Personliga "])

print(f"{person}: {egenskap}")

