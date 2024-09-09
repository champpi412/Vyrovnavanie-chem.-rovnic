# Vyrovnávač chemických rovníc
Program na určovanie stechiometrických koeficientov v chemickej rovnici.
# Uživateľský manuál

### Spustenie

Pred spustením je potrebné nainštalovať Python a všetky balíčky potrebné na spustenie programu. Tie sa nainštalujú spustením 
```py -m pip install -r requirements.txt``` v adresári projektu. Program sa spúšťa príkazom ```py ui.py``` v adresári projektu zo zložky balancer.

### Používanie

Pre vyrovnanie rovnice stačí rovnicu zadať v správnom tvare, ktorý je uvedený nad kolónkou pre zadanie rovnice. Po stlačení tlačítka ```Vyrovnaj``` program zobrazí vyrovnanú rovnicu.
Ak bola rovnica zadaná v zlom tvare, program na to upozorní zvukom a taktiež aj error správou.

Uživateľ si môže zadanú rovnicu skopírovať pomocou tlačítka ```Skopíruj vyrovnanú rovnicu``` a ďalej ju použiť pre svoje potreby. Ak sa uživateľ potrebuje vrátiť ku starším vstupom, môže si ich vybrať z histórie vstupov.
Po kliknutí na jeden zo vstupov sa tento vstup automaticky nakopíruje.

Ak uživateľ preferuje buď tmavý alebo svetlý vzhľad, môže si jeden z nich nastaviť tlačítkom ```Zmeniť vzhľad```.

# Technický popis
Kód pozostáva z dvoch častí, jedna určená na vyrovnanie zadanej chemickej rovnice a druhá na vizuálne spracovanie. Použité externé knižnice sú CustomTkinter, PyGame a ChemPy.
## Popis funkcií
### vyrovnanie()
Táto funkcia je určená na vyrovnanie chemickej rovnice, prípadne aby zhodnotila že uživateľ zadal vstup v nesprávnom tvare. Po kliknutí tlačítka ```Vyrovnaj``` táto funkcia najprv skúsi vstup rozdeliť  podľa charakteru "=" a následne rozdeliť vstup na produkty a reaktanty podľa charakteru "+". V ďalšom kroku sa spúšta funkcia z knižnice ChemPy ```balance_stoichiometry``` a vyrovnaná rovnice sa konvertuje do stringovej podoby. Ak ```balance_stoichiometry``` neprebehne, funkcia vyrovnanie() vyhodí error.
### zmen()

Funkcia zmen() je určená na zmenu vzhľadu z tmavého na svetlý resp. zo svetlého na tmavý. Používa jednoduchý if a elif check na globálnej premennej ```vzhľad```.

### skopirujhistoria()

Funckia používa jednoduché CustomTkinter funkcie na skopírovanie jedného zo vstupov z histórie vstupov po kliknutí.

### copy_to_clipboard()

Funkcia kopíruje vyrovnanú rovnicu pomocou tlačítka.

### update_history_menu()

Táto funkcia aktualizuje históriu vstupov po každej správne zadanej rovnici.

## Zvyšný kód

Zvyšok kódu je určený na vizuálne spracovanie, používa sa najmä knižnica CustomTkinter plus je použitá taktiež knižnica PyGame na spustenie zvuku pri správne zadanom alebo nesprávne zadanom vstupe.

