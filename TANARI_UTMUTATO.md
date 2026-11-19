# Tanári útmutató

A négy feladat önállóan is kiadható. Ugyanazokat az alapokat gyakoroltatják: input, float, szövegkezelés, műveletek, if/elif/else, logikai kapcsolat, f-string és egyszerű ValueError-kezelés.

## Javasolt munkamenet

1. A tanuló olvassa el a feladatot. Saját szavaival nevezze meg a bemeneteket és a várt kimeneteket.
2. Egy mintát számoljatok ki kézzel. Tisztázzátok, miért szorzás vagy osztás szerepel benne.
3. A magyarázó részletek alapján írja meg a kódot Thonnyban. A rövid részletek önmagukban nem teljes programok.
4. Próbálja ki a mintabemeneteket és a határértékeket. A böngészős számítás segít a számolás ellenőrzésében.
5. Nyissa ki a teljes megoldást, és a konkrét eltérést keresse meg. A teljes kódot új szerkesztőlapra másolja.
6. Oldja meg az önálló próbát, és magyarázza el a megfelelő feltételes ágat.

## Mire kérdezz rá?

- Miért kell float, ha az input után még szövegünk van?
- Mi a különbség az = és a == között?
- Miért "1" és "2" szöveggel hasonlítjuk össze a menüválasztást?
- Miért kell a fogyasztásnál 100-zal osztani?
- Mi történik pontosan 10 000 Ft, 0 °C és 30 °C esetén?
- A negatív érték minden feladatnál hibás? Miért nem?
- Mi a különbség a nem számmá alakítható és a számmá alakítható, de tiltott érték között?
- A .2f átírja a változót, vagy csak a megjelenítést formázza?

## Ellenőrzés

A MINTAFUTTATASOK.txt a négy ténylegesen lefuttatott mintát tartalmazza. A források a programok mappában vannak; ugyanazok tölthetők le a weboldalról.

Az összes megoldás szokásos, véges tizedes számokra készült. A float különleges értékei (például nan és inf), illetve szélsőségesen nagy értékek ellenőrzése nem része ennek a kezdő feladatsornak. A böngészős szemléltetés ezeket elutasítja. A Python-formázás lebegőpontos számokon dolgozik; ne várjátok, hogy minden félérték a hétköznapi kerekítési szokással egyezzen.

A Celsius-besorolás a feladat egyszerű szabálya; nincs abszolút nulla szerinti érvényességvizsgálat. Az osztályozás az eredeti, kerekítés előtti Celsius-értéket használja.

## Beadás

Kérd a tanulók saját négy .py fájlját, és szükség esetén egy-egy helyes futtatást bemutató képernyőképet. A weboldal gyakorló munkafüzet, nem automatikus kódértékelő és nem felügyelt vizsga.
