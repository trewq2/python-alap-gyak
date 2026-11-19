# Autóút üzemanyagköltségének kiszámítása
print("Autóút üzemanyagköltségének kiszámítása")

try:
    # Az input() szöveget ad vissza.
    # A replace() a tizedesvesszőt tizedespontra cseréli.
    # A float() tört szám kezelésére alkalmas számmá alakít.
    tavolsag = float(
        input("Az út hossza kilométerben: ").replace(",", ".")
    )
    fogyasztas = float(
        input("Átlagfogyasztás (liter/100 km): ").replace(",", ".")
    )
    literar = float(
        input("Az üzemanyag ára (Ft/liter): ").replace(",", ".")
    )

    # Hibás adatokkal nem végzünk számítást.
    if tavolsag < 0:
        print("Hiba: az út hossza nem lehet negatív!")
    elif fogyasztas <= 0:
        print("Hiba: a fogyasztásnak pozitívnak kell lennie!")
    elif literar <= 0:
        print("Hiba: az üzemanyag árának pozitívnak kell lennie!")
    else:
        # A fogyasztást 100 kilométerre adtuk meg.
        uzemanyag = tavolsag * fogyasztas / 100
        koltseg = uzemanyag * literar

        # .2f: két tizedesjegy; .0f: egészre kerekített kiírás.
        print(f"Szükséges üzemanyag: {uzemanyag:.2f} liter")
        print(f"Az út üzemanyagköltsége: {koltseg:.0f} Ft")

        # Az összehasonlítás a kerekítés előtti értékkel történik.
        if koltseg > 10000:
            print("Figyelem! Az út üzemanyagköltsége meghaladja a 10 000 Ft-ot.")
        else:
            print("Az út üzemanyagköltsége legfeljebb 10 000 Ft.")

except ValueError:
    # Ha a szöveg nem alakítható számmá, érthető üzenetet adunk.
    print("Hibás bevitel! Számot adj meg, például: 200 vagy 6,5.")
