import requests
from email.mime.text import MIMEText
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler

with open(r"C:\Users\Maria\Documents\Desktop\map\cheie_api.txt") as fisier:
    API_KEY=fisier.read().strip()

#https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={API key}

URL_API="https://api.openweathermap.org/data/2.5/weather"
oras=input("Introdu numele orasului:")
units="metric"
requests_url=f"{URL_API}?q={oras}&appid={API_KEY}&units={units}"
email="maria.madalina.radis@gmail.com"
email_destinatar="maria.madalina.radis@gmail.com"

def verificare_vreme():
    raspuns=requests.get(requests_url)
    data=raspuns.json()
    if raspuns.status_code==200:
        vreme=data['main']['temp']
        starea_vremii=data['weather'][0]['description']
        umiditate=data['main']['humidity']
        return vreme,starea_vremii,umiditate
    else:
        print("Eroare")
        return None

def afisare_vreme():
    vreme,starea_vremii,umiditate=verificare_vreme()
    print(f"Temp: {vreme}\nUmid: {umiditate}\nStare vreme: {starea_vremii}")
    
vreme,starea_vremii,umiditate=verificare_vreme()   
continut_fisier=f"Temp: {vreme}\nUmid: {umiditate}\nStare vreme: {starea_vremii}"

def send_email():

    with open(r"C:\Users\Maria\Documents\Desktop\map\parola_google.txt") as fisier:

        parola_google=fisier.read().strip()

    msg=MIMEText(f"Starea vremii:{continut_fisier}")

    msg["Subject"]="vreme!"

    msg['From']=email

    msg['To']=email_destinatar

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server_smtp:

        server_smtp.login(email,parola_google)

        server_smtp.sendmail(email,email_destinatar,msg.as_string())

    print("Email trimis cu succes!")

#print(API_KEY)

print(continut_fisier)
print(send_email())
with open("raport_vreme.txt", "w+") as fisier_scriere:
    fisier_scriere.write(continut_fisier)

#apelare_interval_de_timp=BlockingScheduler()
#apelare_interval_de_timp.add_job(afisare_vreme,'interval',seconds=4)
#apelare_interval_de_timp.start()