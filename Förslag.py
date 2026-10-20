huset = {
    "Källaren": {
    "person": {
    "namn": "Trädgårdsmästaren",
    "alibi": "Jag vattnade rosorna",
    "attribut": "Har en nyckelknippa"},
    "ledtråd": {
    "namn": "Lampan",
    "egenskaper": [
        "Lampan är trasig",
        "Lampan har blod på sig"]}},

    "Garaget": {
        "person": {
        "namn": "Butlern",
        "alibi": "Jag tvättade bilen",
        "attribut": "Har lera på sina skor"},
        "ledtråd": {
        "namn": "Däckspår",
        "egenskaper": [
            "Det finns färska däckspår",
            "Spåren innehåller lera"]}},

    "Köket": {
        "person": {
        "namn": "Kocken",
        "alibi": "Jag lagade middag",
        "attribut": "Har en blodfläck på sin skjorta"},
        "ledtråd": {
        "namn": "Kniven",
        "egenskaper": [
            "Kniven är nydiskad",
            "Det finns blod på handtaget"]}}}


# Skriv ut information om ett rum
rum = huset["Källaren"]
rum = huset["Garaget"]
print(rum, "Källaren")
print("Person:", rum["person"]["namn"])
print("Alibi:", rum["person"]["alibi"])
print(f"Attribut: {rum['person']['attribut']}")
print("Ledtråd:", rum["ledtråd"]["namn"])

for egenskap in rum["ledtråd"]["egenskaper"]:
    print("-", egenskap)
