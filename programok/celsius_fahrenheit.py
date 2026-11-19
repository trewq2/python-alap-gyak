# Celsius-fok átváltása Fahrenheit-fokra
print("Celsius-fok átváltása Fahrenheit-fokra")

try:
    # Negatív szám és tizedestört is megadható.
    celsius = float(
        input("Add meg a hőmérsékletet Celsius-fokban: ").replace(",", ".")
    )

    # Előbb szorzunk, utána hozzáadunk 32-t.
    fahrenheit = celsius * 1.8 + 32

    # Mindkét érték egy tizedesjeggyel jelenik meg.
    print(f"{celsius:.1f} °C = {fahrenheit:.1f} °F")

    # Az eredeti Celsius-érték alapján választunk üzenetet.
    if celsius < 0:
        print("Fagyveszély!")
    elif celsius <= 30:
        # Ide csak akkor jutunk, ha a Celsius már legalább nulla.
        print("Nincs szélsőséges hőmérséklet.")
    else:
        print("Hőség!")

except ValueError:
    print("Hibás bevitel! Számot adj meg, például: 25,5 vagy -5.")
