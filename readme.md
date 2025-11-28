"Vad har du använt för layouten i ditt GUI? Dvs. har du använt pack eller grid för att placera innehållet. Vilka skillnader har dessa?"

    - Jag använde pack för att placera knapparna, pack placerar widgets i riktningar (top, left, etc) medan grid använder rader och kolummer.

"Hur sparar vi innehållet i väskan? Hur fungerar datatypen och varför väljer vi att jobba med den i det här programmet?"

    - Innehållet ligger i en Python-lista som heter bag. Man sparar innehåll i listan genom att använda append och tar bort innehåll genom att använda remove. Datatypen lista fungerar bra eftersom vi gör en påse.

"Hur fungerar kontroller i tkinter? Förklara till exempel hur du lägger till en knapp och får den att fungera, vad krävs?"

    - För att skapa en knapp och få den att fungera så måsta man binda den till en funktion, till exempel:
            def add_item():
                #gör något

            btn = tk.Button(root, text="Spara", command=add_item)
            btn.pack()

"Finns det skillnader mellan ditt program som använder tkinter och terminalen? Vilka är det i så fall och varför skiljer det sig?"

    - Terminalen använder en while-loop och inputs medan tkinter använder visuella knappar och mainloop. Fördelen med tkinter är att det gör programmet mer användarvänligt.

"Jämför strukturen på programmen? Vad är det som driver programmet i terminal versionen och vad ersätts det med i tkinter?"

    - I terminalen så styr en huvudloop allt och inmatning bestämmer nästa steg medan tkinter registrerar funktioner till knappar medan mainloop sköter händelser. 

Förslag på förbättringar:
    1. Att använda en Listbox så användaren ser och väljer saker direkt.
    2. Att lägga till ett Entry-fält för snabbare inmatning (istället för dialogrutor).
    3. Att spara väskan i en JSON-fil så innehållet finns kvar nästa gång.

Listbox: skapa listbox = tk.Listbox(root) och uppdatera med listbox.insert(tk.END, item) eller rensa+fylla om listan ändras.

Entry + knapp: läs entry.get(), validera, bag.append(value) och uppdatera Listbox.

Spara/ läs fil: använd import json; json.dump(bag, file) och json.load(file).