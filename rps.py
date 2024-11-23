from tkinter import*
from tkinter import messagebox
import random
from PIL import Image, ImageTk

afisaj=Tk()
afisaj.title("Piatra Hartie Foarfeca")
reguli=("Regulile jocului Piatra Hartie Foarfeca sunt: \n"
        "Piatra vs Hartie-> invinge Hartie \n"
        "Piatra vs Foarfeca -> invinge Piatra \n"
        "Hartie vs Foarfeca -> invinge Foarfeca"
        )
#Regulile jocului
label_reguli= Label(afisaj, text=reguli, font=('Arial',12,"bold"), fg="#993366")
label_reguli.pack(side="top",pady=20)
#Buton piatra
#buton_piatra=Button(afisaj, text="Piatra", width=10)
#buton_piatra.pack(side="left",padx=10,pady=20)

#Buto hartie

def joc(alegere):
    optiuni=["Piatra", "Hartie", "Foarfeca"]
    alegere_pc=random.choice(optiuni)
    mesaj=f"Pc-ul a ales {alegere_pc}\n"
    if (alegere==alegere_pc):
        mesaj+="Egalitate"
    elif(alegere=="Piatra" and alegere_pc=="Foarfeca") or\
    (alegere=="Hartie" and alegere_pc=="Piatra") or\
    (alegere=="Foarfeca" and alegere_pc=="Hartie"):
        mesaj+="Ai gastigat"
        messagebox.showinfo("Winner", "Ai gastigat")
    else:
        mesaj+="Ai pierdut!!"
        messagebox.showinfo("Loser","Ai pierdut")


imagine_hartie=PhotoImage(file=r"C:\Users\Maria\Documents\Desktop\map\hartie.png")
imagine_hartie=imagine_hartie.subsample(5,5)
buton_hartie=Button(afisaj, image=imagine_hartie, width=100, height=100, command=lambda:joc("Hartie"))
buton_hartie.pack(side="left",padx=10)

#Buton foarfeca
imagine_foarfeca=PhotoImage(file=r"C:\Users\Maria\Documents\Desktop\map\foarfeca.png")
imagine_foarfeca=imagine_foarfeca.subsample(20,20
buton_foarfeca=Button(afisaj, image=imagine_foarfeca, width=50, height=50, command=lambda:joc("Foarfeca"))
buton_foarfeca.pack(side="left",padx=10)

imagine_piatra=PhotoImage(file=r"C:\Users\Maria\Documents\Desktop\map\piatra.jpeg")
imagine_piatra=imagine_piatra.subsample(7,7)
buton_piatra=Button(afisaj, image=imagine_piatra, width=50, height=50, command=lambda:joc("Piatra"))
buton_piatra.pack(side="left",padx=10)

mainloop()