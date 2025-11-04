run = True
bag = []
print("Välkommen till påsen")
while run:
    print("Visa innehållet [V]")
    print("Spara i påsen [S]")
    print("Avsluta [Q]")

    choice = input("Välj: ")
    if choice.lower() == "v":
        for thing in bag:
            print(thing)
    elif choice.lower() == "s":
        bag.append(input("Ange vad du vill spara: "))
    elif choice.lower() == "q":
        run = False
    else:
        print("Felaktig inmatning, försök igen.")