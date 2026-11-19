# Milliméter és hüvelyk átváltása
# Ebben a feladatban a col, inch és hüvelyk ugyanazt jelenti.
print("Milliméter és hüvelyk átváltása")
print("1 - Milliméterből hüvelyk")
print("2 - Hüvelykből milliméter")

valasztas = input("Válassz egy lehetőséget (1 vagy 2): ").strip()

# Csak a két megadott menüpontot fogadjuk el.
if valasztas == "1" or valasztas == "2":
    try:
        meret = float(
            input("Add meg az átváltandó méretet: ").replace(",", ".")
        )

        if meret < 0:
            print("Hiba: a méret nem lehet negatív!")
        elif valasztas == "1":
            # Milliméterből hüvelykre osztással váltunk.
            huvelyk = meret / 25.4
            print(f"{meret:.2f} mm = {huvelyk:.2f} hüvelyk")
        else:
            # Hüvelykből milliméterre szorzással váltunk.
            millimeter = meret * 25.4
            print(f"{meret:.2f} hüvelyk = {millimeter:.2f} mm")

    except ValueError:
        print("Hibás bevitel! A méretet számmal add meg!")
else:
    print("Hibás választás! Csak 1 vagy 2 adható meg.")
