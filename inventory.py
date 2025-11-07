run = True
bag = []
print("Välkommen till påsen🎒")
while run:
    print(" ")
    print("Visa innehållet👓     [V]")
    print("Spara i påsen📁       [S]")
    print("Sök efter innehåll🔍  [L]")
    print("Töm påsen🗑️            [C]")
    print("Avsluta❌             [Q]")

    choice = input("Ange ditt val: ")
    if choice.lower() == "v":
        for thing in bag:
            print(thing)
    elif choice.lower() == "s":
        bag.append(input("Ange vad du vill spara📁: "))
    elif choice.lower() == "c":
        bag.clear()
        print("Påsen har tömts🗑️")
    elif choice.lower() == "q":
        run = False
        print("Programmet har avslutats❌")
    elif choice.lower() == "l":
        query = input("Ange vad du vill söka efter🔍: ")
        if query.lower() in bag:
            print(f"Du hittade {query} i påsen✅")
        else:
            print(f"Du kunde inte hitta {query} i påsen🚫")
    else:
        print("Felaktig inmatning, försök igen👾")