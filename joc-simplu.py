import tkinter as tk
from tkinter import messagebox
import random

root =tk.Tk()
root.title("GhicesteNumarulApp")

class GhicesteNumarulApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Ghicește Numărul")
        self.numar_secret = random.randint(1, 100)
        self.incercari = 0
        
        # Eticheta de instrucțiuni
        self.instructiuni = tk.Label(root, text="Am ales un număr între 1 și 100. Ghicirea ta?")
        self.instructiuni.pack(pady=10)
        
        # Caseta pentru input
        self.input_numar = tk.Entry(root, width=10)
        self.input_numar.pack(pady=5)
        
        # Butonul pentru ghicire
        self.ghiceste_buton = tk.Button(root, text="Ghicește", command=self.verifica_numar)
        self.ghiceste_buton.pack(pady=10)
        
        # Eticheta pentru afișarea mesajelor
        self.mesaj = tk.Label(root, text="", fg="blue")
        self.mesaj.pack(pady=5)
    
    def verifica_numar(self):
        try:
            ghicire = int(self.input_numar.get())
        except ValueError:
            self.mesaj.config(text="Te rog să introduci un număr valid!", fg="red")
            return
        
        self.incercari += 1
        
        if ghicire < self.numar_secret:
            self.mesaj.config(text="Prea mic! Mai încearcă.", fg="orange")
        elif ghicire > self.numar_secret:
            self.mesaj.config(text="Prea mare! Mai încearcă.", fg="orange")
        else:
            messagebox.showinfo("Felicitări!", f"Ai ghicit numărul {self.numar_secret} în {self.incercari} încercări!")
            self.reset_joc()
    
    def reset_joc(self):
        self.numar_secret = random.randint(1, 100)
        self.incercari = 0
        self.mesaj.config(text="")
        self.input_numar.delete(0, tk.END)

root.mainloop()