rum2 = {"Köket": ["Kocken","Lagade middag","Blod på skjortan"]}
#här navigerar ju vi med index 
print(f"I {list(rum2.keys())[0]} finns {rum2['Köket'][0]}, han säger att han {rum2['Köket'][1]}")

rum1 = {"Person": "Trädgårdsmästaren", 
       "Alias": "Vattnade rosorna",
       "Attribut": "Leriga skor"}
print(f"{rum1["Person"]} säger att han {rum1["Alias"]} och har {rum1["Attribut"]}")

rum1 = {"Köket": ["Kocken", "lagade middag", "Blod på skjortan"]}
rum2 = {"Biblioteket": ["Bibliotekarien", "läste en bok", "Leriga skor"]}

rum = {
    "Vardagsrummet": rum1,
    "Biblioteket": rum2}

for x in rum:
    print(x)
val = input("Vilket rum? Vardagsrummet eller Biblioteket? ")

if val in rum:
    x = rum[val]
    namn = list(x.keys())[0]

    print(f"I {namn} finns {x[namn][0]}, han säger att han {x[namn][1]}")
else:
    print("Det rummet finns inte.")

