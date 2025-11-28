import tkinter as tk
from tkinter import simpledialog, messagebox

bag = []

def show_bag():
    if bag:
        messagebox.showinfo("Påsen", "\n".join(bag))
    else:
        messagebox.showinfo("Påsen", "Påsen är tom.")

def add_item():
    item = simpledialog.askstring("Spara", "Vad vill du lägga i påsen?")
    if item:
        bag.append(item)

def remove_item():
    item = simpledialog.askstring("Ta bort", "Vad vill du ta bort?")
    if item:
        if item in bag:
            bag.remove(item)
            messagebox.showinfo("Borttagen", f"{item} togs bort.")
        else:
            messagebox.showinfo("Fel", f"{item} finns inte.")

def find_item():
    item = simpledialog.askstring("Leta i påsen", "Vad letar du efter?")
    if item:
        if item in bag:
            messagebox.showinfo("Hittad", f"{item} finns i påsen.")
        else:
            messagebox.showinfo("Inte hittad", f"{item} hittades inte.")

root = tk.Tk()
root.title("Påsen🎒")
root.geometry("250x260")

tk.Button(root, text="Visa innehåll👓", command=show_bag).pack(fill="x", pady=5)
tk.Button(root, text="Spara i påsen📁", command=add_item).pack(fill="x", pady=5)
tk.Button(root, text="Ta bort från påsen🗑️", command=remove_item).pack(fill="x", pady=5)
tk.Button(root, text="Leta i påsen🔎", command=find_item).pack(fill="x", pady=5)
tk.Button(root, text="Avsluta❌", command=root.quit).pack(fill="x", pady=5)

root.mainloop()
