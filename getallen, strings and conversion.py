cijferICOR = float(input("Welk cijfer ga je halen voor ICOR? "))
cijferPROG = float(input("Welk cijfer ga je halen voor PROG? "))
cijferCSN = float(input("Welk cijfer ga je halen voor CSN? "))

lijst1 = ([cijferPROG, cijferCSN, cijferICOR])
lijst2 = str(lijst1)
CijferOpgeteld = sum(lijst1)
aantalwrd = len(lijst2.split())

GemiddeldeCijfer = CijferOpgeteld / aantalwrd
Verdiensten = CijferOpgeteld * 30

print("\nMijn cijfers hebben een gemiddelde van " + str(GemiddeldeCijfer) +
      ",\ndaarom geeft de HU een beloning van " + str(Verdiensten) + " euro!")
