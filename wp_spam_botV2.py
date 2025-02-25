# Basit Whatsapp Spam Botu coded by Kejii
import pyautogui
from time import sleep

print("""
██╗ ██╗ ███████╗     ██╗██╗██╗
██║ ██║ ██╔════╝     ██║██║██║
█████╔╝ █████╗       ██║██║██║
██╔═██╗ ██╔══╝  ██   ██║██║██║
██║ ██║ ███████╗╚█████╔╝██║██║
╚═╝ ╚═╝ ╚══════╝ ╚════╝ ╚═╝╚═╝""")
print(" ")

x = input("Başlamak için 'enter' tuşuna basın.")
sleep(1)

if x == "":
    y = input("Göndermek istediğiniz mesajı girin: ")
    sayı = int(input("Kaç tane gönderilsin? "))
    adet = 0
    print("Saldırı başlatılıyor...")
    sleep(3)
    baha = ("Whatsapp'a gidin ve 'enter' tuşuna basın.")
   
    def mesaj():
        pyautogui.write(y)
        pyautogui.press('enter')
    while True:
        mesaj()
        sleep(0)
        adet = adet +1
        if adet == sayı:
            break
        
           
    
