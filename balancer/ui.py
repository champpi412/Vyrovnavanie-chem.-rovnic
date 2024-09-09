import tkinter
import customtkinter
from chempy import balance_stoichiometry
from chempy import Reaction
from pygame import mixer


mixer.init()

vzhlad = "dark"
historia = []

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
def update_history_menu():
    historia_zvol.configure(values=historia)
    
def copy_to_clipboard():
    okno.clipboard_clear()
    okno.clipboard_append(dokoncene.cget("text"))


def vyrovnavanie():
    try:
        rovnica = vstup_produkty.get().split("=")
        produkty = set(rovnica[0].split("+"))
        reaktanty = set(rovnica[1].split("+"))
        reakcia = balance_stoichiometry(produkty, reaktanty)
        
        if vzhlad == "dark":
            dokoncene.configure(text=Reaction(*reakcia), text_color="white")
        elif vzhlad == "light":
            dokoncene.configure(text=Reaction(*reakcia), text_color="black")
        
        historia.append(vstup_produkty.get())
        update_history_menu()
        
        mixer.music.load("zvuk.mp3")
        mixer.music.play(loops=0)
    except:
        dokoncene.configure(text="Rovnica bola zadaná v zlom tvare", text_color="red")
        mixer.music.load("error.mp3")
        mixer.music.play(loops=0)

        
def zmen():
    global vzhlad
    if vzhlad == "dark":
        customtkinter.set_appearance_mode("light")
        vzhlad = "light"
        mod.configure(text = "🌙 Zmeniť vzhľad")
    elif vzhlad == "light":
        customtkinter.set_appearance_mode("dark")
        vzhlad = "dark"
        mod.configure(text = "☀ Zmeniť vzhľad")

def skopirujhistoria(choice):
    okno.clipboard_clear()
    okno.clipboard_append(choice)


okno = customtkinter.CTk()
okno.geometry("960x640")
okno.title("Vyrovnávač chemických rovníc")
okno.iconbitmap("ikonka.ico")


mod = customtkinter.CTkButton(okno, text = "☀ Zmeniť vzhľad", command=zmen, font=("Helvetica", 15))
mod.place(relx = 0.1, rely = 0.05, anchor = tkinter.CENTER)

priklad = customtkinter.CTkLabel(okno, text = "Zadajte chemickú rovnicu", font=("Helvetica", 50, "bold"))
priklad2 = customtkinter.CTkLabel(okno, text = "Príklad: Ca3(PO4)2 + SiO2 + C = CaSiO3 + CO + P", font=("Helvetica", 25))
priklad.pack(pady = 20)
priklad2.pack(pady = 10)

reakcia = tkinter.StringVar()
vstup_produkty = customtkinter.CTkEntry(okno, width = 500, height = 40, textvariable = reakcia, font=("Helvetica", 25))
vstup_produkty.pack(pady = 10)

vyrovnaj = customtkinter.CTkButton(okno, text = "Vyrovnaj", command=vyrovnavanie, font=("Helvetica", 15))
vyrovnaj.pack(pady=5)


copy_btn = customtkinter.CTkButton(okno, text="Skopírovať vyrovnanú rovnicu", command=copy_to_clipboard, font=("Helvetica", 15))
copy_btn.pack(pady=10)

dokoncene = customtkinter.CTkLabel(okno, text="", font = ("Comic Sans MS", 20))
dokoncene.pack(pady=100)

historia_var = tkinter.StringVar(value="Vstupy")
historia_napis = customtkinter.CTkLabel(okno, text = "História vstupov", font = ("Helvetica", 25))
historia_napis.pack(pady = 5)
historia_zvol = customtkinter.CTkOptionMenu(okno, width=300, values=historia, variable=historia_var, command=skopirujhistoria)
historia_zvol.pack()

okno.mainloop()



