from tkinter import*
from tkinter import messagebox

afisaj=Tk()
afisaj.title("Calculator")

def adunare():
    try:
        valoare1=float(entry1.get())
        valoare2=float(entry2.get())
        rezultat=valoare1 + valoare2
        entry3.delete(0, END)
        entry3.insert(0, str(rezultat))
    except ValueError:
        messagebox.showerror("eroare", "Introduceti valori valide")
        

def scadere():
    try:
        valoare1=float(entry1.get())
        valoare2=float(entry2.get())
        rezultat=valoare1 - valoare2
        entry3.delete(0, END)
        entry3.insert(0, str(rezultat))
    except ValueError:
        messagebox.showerror("eroare", "Introduceti valori valide")
        
def inmultire():
    try:
        valoare1=float(entry1.get())
        valoare2=float(entry2.get())
        rezultat=valoare1 * valoare2
        entry3.delete(0, END)
        entry3.insert(0, str(rezultat))
    except ValueError:
        messagebox.showerror("eroare", "Introduceti valori valide")
        
    
def impartire():
    try:
        valoare1=float(entry1.get())
        valoare2=float(entry2.get())
        if valoare2==0:
            messagebox.showerror("Eroare", "Nu se poate imparti la zero")
        else:
            rezultat=valoare1 / valoare2
            entry3.delete(0, END)
            entry3.insert(0, str(rezultat))
    except ValueError:
        messagebox.showerror("eroare", "Introduceti valori valide")

def stergere():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

#prima valoare
Label(afisaj, text="Valoare: 1").grid(row=0,column=0)
entry1=Entry(afisaj)
entry1.grid(row=0, column=1)

#a doua valoare
Label(afisaj, text="Valoare:2").grid(row=1,column=0)
entry2=Entry(afisaj)
entry2.grid(row=1, column=1)

#rezultat
Label(afisaj,text="Rezultat:").grid(row=2,column= 0)
entry3=Entry(afisaj)
entry3.grid(row=2, column=1)

#Butoane pt operatii

Button(afisaj, text="+", width=15, command=adunare).grid(row=3, column=0, padx=5)
Button(afisaj, text="-", width=15, command=scadere).grid(row=3, column=1, padx=5)
Button(afisaj, text="*", width=15, command=inmultire).grid(row=4, column=0, padx=5)
Button(afisaj, text="/", width=15, command=impartire).grid(row=4, column=1, padx=5)

#Buton stergere
Button(afisaj, text="c", width=10, command=stergere).grid(row=5, column=0, padx=5, pady=5)

mainloop()
