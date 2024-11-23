from tkinter import *
from tkinter import messagebox

def raspuns():
    if gen_var.get() == "masculin":
        gen = "un barbat"
        fumator_status = "fumator" if fumator_var.get() == "fumator" else "nefumator"
    else:
        gen = "o femeie"
        fumator_status = "fumatoare" if fumator_var.get() == "fumator" else "nefumatoare"
    mesaj = f"Esti {gen} {fumator_status}"
    rezultat.set(mesaj)
    messagebox.showinfo("Raspuns", mesaj)

afisaj = Tk()
afisaj.title("Tipuri de persoane")
#afisaj.geometry("300x200")
gen_var = StringVar(value="masculin")
fumator_var = StringVar(value="fumator")

frame_gen = LabelFrame(afisaj, text="Gen", padx=10, pady=10)
frame_gen.pack(side="left")

Radiobutton(frame_gen, text="masculin",variable=gen_var, value="masculin").pack(anchor="w")
Radiobutton(frame_gen, text="feminin",variable=gen_var, value="feminin").pack(anchor="w")

frame_fumator = LabelFrame(afisaj, text="Fumator?", padx=10, pady=10)
frame_fumator.pack(side="right")

Radiobutton(frame_fumator, text= "fumator", variable=fumator_var,value="fumator").pack(anchor="w")
Radiobutton(frame_fumator, text= "nefumator", variable=fumator_var,value="nefumator").pack(anchor="w")

rezultat = StringVar()
label_rezultat = Label(afisaj, textvariable=rezultat, fg="red")
label_rezultat.pack(anchor="w")

buton_afiseaza_informatii = Button(afisaj, text="Afla raspunsul", command=raspuns)
buton_afiseaza_informatii.pack(pady=100)

mainloop()