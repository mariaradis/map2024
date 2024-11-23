
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import smtplib
from money_parser import price_str

with open(r"C:\Users\Maria\Documents\Desktop\map\parola_google.txt") as fisier:
    parola_google=fisier.read().strip()

email="maria.madalina.radis@gmail.com"
email_destinatar="maria.madalina.radis@gmail.com"
def send_email():
    msg=MIMEText(f"Pretul produsului a scazut\n{pret_produs_v2()}\{titlu_produs()}\n{get_rating()}")
    msg["Subject"]="Modificare text!"
    msg['From']=email
    msg['To']=email_destinatar
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server_smtp:
        server_smtp.login(email,parola_google)
        server_smtp.sendmail(email,email_destinatar,msg.as_string())
    print("Email trimis cu succes!")


url="https://www.emag.ro/telefon-mobil-samsung-galaxy-s24-ultra-dual-sim-12gb-ram-512gb-5g-titanium-black-sm-s928bzkheue/pd/DF6L7KYBM/"
raspuns= requests.get(url)
raspuns2= BeautifulSoup(raspuns.text, 'html.parser')
def afisare_continut_pagina():
    print(raspuns)
    print(raspuns2.prettify())

def pret_produs():
    pret= raspuns2.find('p', attrs={'class':'product-new-price'}).text
    pret=price_str(pret)
    return pret

def pret_produs_v2():
    pret= raspuns2.find('p', attrs={'class':'product-new-price'}).text
    pret=price_str(pret)
    pret=float(pret)
    return pret

def titlu_produs():
    titlu=raspuns2.find('h1', attrs={'class':'page-title'}).text
    return titlu.strip()

def get_rating():
    rating=raspuns2.find('a', attrs={'class':'rating-text'}).text.strip()
    return rating.split(" ")[0]

def verificare():
    pret_referinta=5300
    pret=pret_produs_v2()
    nume=titlu_produs()
    rating=get_rating()
    if pret<pret_referinta:
        print("pretul a scazut")
        send_email()
    else:
        print("Pretul nu a scazut")


#v1
#print( parola_google())
#print(pret_produs())
#print(pret_produs_v2())
#print(titlu_produs())
#afisare_continut_pagina()
verificare()

#print(rating()) 
