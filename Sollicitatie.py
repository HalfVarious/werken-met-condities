def main():
    print("===============================================================================================================================================================")
    if float(input("Hoeveel jaar praktijk ervaring heeft u met dieren-dresuur : ")) <=4:
        if float(input("Hoeveel jaar heeft u met jongleren? : ")) <=5:
            if float(input("Hoeveel jaar praktijk ervaring heeft u met acrobatiek? : ")) <=3:
                return False
    

    if input("Heeft u een MBO-4 Diploma? (Ja of Nee) : ") == "Nee":
        return False
    
    if input("Bent u in het bezit van een geldig rijbewijs? (Ja of Nee) : ") == "Nee":
        return False
    
    if input("Bent u in het bezit van een hoge hoed? (Ja of Nee) : ") == "Nee":
        return False

    if input("Bent u een Man of Vrouw? : ") == "Man" or "man" :
        if input("Heeft u een snor? (Ja of Nee) :") == "Nee":
            return False
        if float(input("Hoeveel cm is uw snor? : ")) <= 9:
            return False
    else:
        if input("Is uw haarkleur rood? (Ja of Nee) : ") == "Nee":
            return False
        if float(input("Hoelang is uw haar in cm")) <= 19:
            return False
    if float(input("Hoelang bent u inclusief hoogte kapsel? (In Cm) : ")) <= 149:
        return False
    if float(input("Hoeveel weegt u ongeveer in KG? : ")) <= 89:
        return False
    if input("Bent u in het bezit van een certificaat 'Werken met gevaarlijk personeel' (Ja of Nee) : ") == "Nee":
        return False
        
    return True

if __name__ == "__main__":
        if main():
                print("===============================================================================================================================================================")
                print("==== Gefeliciteerd u komt in aanmerking voor de functie directeur voo Circus HotelDeBotel! Stuur snel uw cv op en wij zullen u zo snelmogelijk contacteren ====")
        else:
            print("===============================================================================================================================================================")
            print("======================== Helaas u voldoet niet aan de vereiste criteria om in aanmerking te komen voor de baan circus directeur. ==============================")
print("===============================================================================================================================================================")