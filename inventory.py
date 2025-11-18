from colorama import Fore
run = True
bag = []
print(Fore.BLACK + "Välkommen till påsen🎒")
while run:
    print("_________________________")
    print("Visa innehållet👓     [V]")
    print("Spara i påsen📁       [S]")
    print("Sök efter föremål🔍   [L]")
    print("Ta bort föremål🗑️      [R]")
    print("Avsluta❌             [Q]")

    choice = input("Ange ditt val: ")
    if choice.lower() == "v":
        for thing in bag:
            print(thing)
        if not bag:
            print("Påsen är tom just nu🕳️")
    elif choice.lower() == "s":
        bag.append(input("Ange vad du vill spara📁: "))
    elif choice.lower() == "r":
        query = input("Ange föremålet du vill ta bort🗑️ : ")
        if query.lower() in bag:
            bag.remove(query)
            print(f"Du tog bort {query}🗑️")
        else:
            print(f"Du kunde inte hitta {query} i påsen🚫")
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
