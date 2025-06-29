print("Welkom bij je eigen rekenmachine!")

getal1 = float(input("Voer het eerste getal in: "))
bewerking = input("Kies een bewerking (+, -, *, /): ")
getal2 = float(input("Voer het tweede getal in: "))

if bewerking == "+":
    resultaat = getal1 + getal2
elif bewerking == "-":
    resultaat = getal1 - getal2
elif bewerking == "*":
    resultaat = getal1 * getal2
elif bewerking == "/":
    if getal2 != 0:
        resultaat = getal1 / getal2
    else:
        resultaat = "Kan niet delen door nul."
else:
    resultaat = "Ongeldige bewerking."

print("Resultaat:", resultaat)
