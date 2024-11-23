import sqlite3
import random

def adaugare_scuze():
    conn =sqlite3.connect('scuze.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS scuze(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,                  
                    scuze_text TEXT NOT NULL
    )''')
    scuza_noua = input("introdu o scuza noua: ")
    cursor.execute('INSERT INTO scuze (scuze_text) VALUES (?) ', (scuza_noua,))
    conn.commit()
    print("Scuza  ta a fost adaugata cu succes!")
    conn.close()

def afisare_scuze():
    conn=sqlite3.connect('scuze.db')
    cursor=conn.cursor()
    cursor.execute('Select * From scuze ')
    scuze=cursor.fetchall()
    print("Toate scuzele existente sunt: ")
    for i in scuze:
        print(f"{i[0]}:{i[1]}")
    conn.close()

def stergere_scuze():
    conn=sqlite3.connect('scuze.db')
    cursor=conn.cursor()
    afisare_scuze()
    id_scuza_de_sters=input("Introdu id-ul scuzei pe care vrei sa o stergi:")
    cursor.execute('DELETE FROM scuze WHERE id=?', (id_scuza_de_sters))
    conn.commit()
    print("scuza ta a fost stearsa cu succes!")
    conn.close()

def generare_scuze():
    conn=sqlite3.connect('scuze.db')
    cursor=conn.cursor()
    cursor.execute('SELECT scuze_text FROM scuze')
    scuze=cursor.fetchall()
    if scuze:
        scuza_aleasa=random.choice(scuze)
        print('Scuza ta este: "', scuza_aleasa[0], '"')
    else:
        print("Nu exista scuze in baza de date! :( ")
    conn.close()

adaugare_scuze()
afisare_scuze()
stergere_scuze()
generare_scuze()
