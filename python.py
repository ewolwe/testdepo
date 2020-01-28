import os
import time
import datetime

def doktorisimleri():

    print("1- Doç. Dr. Ahmet Erdal TAŞÇI")
    print("2- Doç. Dr. Ali FEDAKAR")
    print("3- Doç. Dr. Ayşe İnci YILDIRIM")
    print("4- Prof. Dr Ali Can HATEMİ")
    print("5- Uzm. Dr Adile Ece ALTINAY")
    print("6- Uzm. Dr. Abdullah Arif YILMAZ")
    print("7- Uzm. Dr. Abdülkadir USLU")

def databasebilgialma():

    doktorisimleri()

    f = input("Kayıt hangi doktor için yapılacak? : ")
    if f == "1":
        f = "Doç. Dr. Ahmet Erdal TAŞÇI\\"
        return f
    else:
        pass

    if f == "2":
        f = "Doç. Dr. Ali FEDAKAR\\"
        return f
    else:
        pass

    if f == "3":
        f = "Doç. Dr. Ayşe İnci YILDIRIM\\"
        return f
    else:
        pass

    if f == "4":
        f = "Prof. Dr Ali Can HATEMİ\\"
        return f
    else:
        pass

    if f == "5":
        f = "Uzm. Dr Adile Ece ALTINAY\\"
        return f
    else:
        pass

    if f == "6":
        f = "Uzm. Dr. Abdullah Arif YILMAZ\\"
        return f
    else:
        pass

    if f == "7":
        f = "Uzm. Dr. Abdülkadir USLU\\"
        return f
    else:
        pass

def tarihklasör():

    b = "C:\\Users\\abatox\\Desktop\\Hastane\\"

    tarih = time.strftime('%d-%m-%Y/')
    
    yol = b + f + tarih + "database.log"
    
    kontrolyol = os.path.dirname(yol)
    if not os.path.exists(kontrolyol):
        os.makedirs(kontrolyol)

    return yol

def hastabilgilerivelog():

    an = datetime.datetime.now()
    ansaat = an.hour
    andakika = an.minute
    
    
    isim = input("Hasta İsmi: ")
    soyisim = input("Hasta Soyismi: ")

    doğumtrh = input("Hasta Doğum Tarihi: ")

    if len(doğumtrh) != 10:
        os.system("cls")
        print("Doğum Tarihi Hatalı")
        doğumtrh = input("Hasta Doğum Tarihi: ")
    
    else:
        pass
    
    TC = input("Hasta TC Kimlik Numarası: ")

    if len(TC) != 11:
        os.system("cls")
        print("TC Kimlik Numarası Hatalı")
        TC = input("Hasta TC Kimlik Numarası: ")
        
    else:
        pass

    dosya =open(yol,"a",encoding="utf8")
    dosya.write("\n----------------------------\n")
    dosya.write("Hasta Kayıt Saati : ")
    dosya.write(str(ansaat))
    dosya.write(":")
    dosya.write(str(andakika))
                
    dosya.write("\n")
    dosya.write("Hasta İsmi : ")
    dosya.write(isim + '\n')
    dosya.write("Hasta Soyismi : ")
    dosya.write(soyisim + '\n')
    dosya.write("Hasta Doğum Tarihi : ")
    dosya.write(doğumtrh + '\n')
    dosya.write("Hasta TC Numarası : ")
    dosya.write(TC + '\n')
    dosya.write("----------------------------")
    dosya.close()
    
    

while True:
    os.system("cls")
    f = databasebilgialma()
    yol = tarihklasör()
    hastabilgilerivelog()