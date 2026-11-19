# Kilométer és mérföld átváltása
print("Távolság átváltása")
print("1 - Kilométerből mérföld")
print("2 - Mérföldből kilométer")

# A menüválasztás szöveg marad. A strip() levágja a szélső szóközöket.
valasztas = input("Válassz egy lehetőséget (1 vagy 2): ").strip()

# Az or jelentése: vagy. Bármelyik feltétel teljesülése elég.
if valasztas == "1" or valasztas == "2":
    try:
        tavolsag = float(
            input("Add meg az átváltandó távolságot: ").replace(",", ".")
        )

        if tavolsag < 0:
            print("Hiba: a távolság nem lehet negatív!")
        elif valasztas == "1":
            # Kilométerből mérföldre osztással váltunk.
            merfold = tavolsag / 1.609344
            print(f"{tavolsag:.2f} km = {merfold:.2f} mérföld")
        else:
            # Itt már biztosan a 2-es lehetőséget választották.
            kilometer = tavolsag * 1.609344
            print(f"{tavolsag:.2f} mérföld = {kilometer:.2f} km")

    except ValueError:
        print("Hibás bevitel! A távolságot számmal add meg!")
else:
    print("Hibás választás! Csak 1 vagy 2 adható meg.")
