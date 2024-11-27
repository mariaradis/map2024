import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("To-Do List")
root.configure(bg='#F5F5DC')

def genereaza_ore():
    return [f"{h:02}:{m:02}" for h in range(24) for m in (0, 30)]

def adauga_task():
    task = entry_task.get()
    ora_selectata = combo_ora.get()
    importanta = combo_importanta.get()

    if not (task and ora_selectata and task != "INTRODUC TASK" and ora_selectata != "Selecteaza ora"):
        messagebox.showwarning("Atentie", "Introduceti un task si selectati ora!")
        return
    
    lista_tasks.insert(tk.END, f"{task} - Ora: {ora_selectata} - Importanta: {importanta}")
    entry_task.delete(0, tk.END)
    entry_task.insert(0, "INTRODUC TASK")
    combo_ora.set("Selecteaza ora")

def sterge_task():
    try:
        task_selectat = lista_tasks.curselection()[0]
        lista_tasks.delete(task_selectat)
    except IndexError:
        messagebox.showwarning("Atentie", "Selectati un task pentru a-l sterge!")

def sterge_toate():
    if messagebox.askyesno("Confirmare", "Sunteti sigur ca doriti sa stergeti toate task-urile?"):
        lista_tasks.delete(0, tk.END)

def clear_entry_task(event):
    if entry_task.get() == "INTRODUC TASK":
        entry_task.delete(0, tk.END)

def restore_entry_task(event):
    if not entry_task.get():
        entry_task.insert(0, "INTRODUC TASK")

def update_background(event=None):
    bg_image = Image.open("photo.png")
    bg_image = bg_image.resize((root.winfo_width(), root.winfo_height()))
    bg_photo = ImageTk.PhotoImage(bg_image)
    label_bg.configure(image=bg_photo)
    label_bg.image = bg_photo

bg_image = Image.open("photo.png")
bg_image = bg_image.resize((root.winfo_width(), root.winfo_height()))
bg_photo = ImageTk.PhotoImage(bg_image)

label_bg = tk.Label(root, image=bg_photo)
label_bg.image = bg_photo
label_bg.place(relwidth=1, relheight=1)

root.bind("<Configure>", update_background)

def creare_grafica():
    label_titlu = tk.Label(root, text="Lista To-Do", font=("Arial", 18))
    label_titlu.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

    frame_input = tk.Frame(root, bg='#F5F5DC')
    frame_input.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    global entry_task
    entry_task = tk.Entry(frame_input, width=30, font=("Arial", 14))
    entry_task.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    entry_task.insert(0, "INTRODUC TASK")
    entry_task.bind("<FocusIn>", clear_entry_task)
    entry_task.bind("<FocusOut>", restore_entry_task)

    global combo_ora
    combo_ora = ttk.Combobox(frame_input, values=genereaza_ore(), font=("Arial", 14))
    combo_ora.set("Selecteaza ora")
    combo_ora.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    global combo_importanta
    combo_importanta = ttk.Combobox(frame_input, values=["Scazut", "Mediu", "Ridicat"], font=("Arial", 14))
    combo_importanta.current(1)
    combo_importanta.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    btn_adauga = tk.Button(frame_input, text="Adauga", command=adauga_task, bg='#FFE4C4')
    btn_adauga.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

    btn_sterge = tk.Button(frame_input, text="Sterge Task", command=sterge_task, bg='#FFE4C4')
    btn_sterge.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

    btn_sterge_toate = tk.Button(frame_input, text="Sterge Tot", command=sterge_toate, bg='#FFE4C4')
    btn_sterge_toate.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

    frame_lista = tk.Frame(root, bg='#F5F5DC')
    frame_lista.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    global lista_tasks
    lista_tasks = tk.Listbox(frame_lista, width=65, height=15, font=("Arial", 12), selectmode=tk.SINGLE, bg='#FAF0E6')
    lista_tasks.pack(side="left", padx=5, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=lista_tasks.yview)
    scrollbar.pack(side="right", fill=tk.Y)

    lista_tasks.config(yscrollcommand=scrollbar.set)

    root.grid_columnconfigure(0, weight=1, uniform="equal")
    root.grid_columnconfigure(1, weight=2, uniform="equal")
    root.grid_rowconfigure(0, weight=0)
    root.grid_rowconfigure(1, weight=1, uniform="equal")
    root.grid_rowconfigure(2, weight=0)

creare_grafica()

root.mainloop()
