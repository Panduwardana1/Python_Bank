import os
import datetime

# Program Banking menggunakan python
system = os.name
    
def cek_saldo():
    print("-"*50)
    print(f"{"MENGECEK SALDO 🪙":^50}")
    print("-"*50)
    print(f"Sldo anda \t:DR{balance:.2f}")
    waktu = datetime.datetime.today() #Mengecek waktu hari ini
    print(f"Time \t\t:{waktu}")
    
def Deposit():
    print("-"*50)
    print(f"{"Deposit 💵":^50}")
    print("-"*50)
    
    dana = float(input("Deposit \t:IDR "))
    
    if dana < 0:
        print(f"Harap masukkan dana yang valid")
        return 0
    else:
        waktu = datetime.datetime.today() #Mengecek waktu hari ini
        print(f"Time \t\t:{waktu}")
        return dana
    
def Penarikan():
    print("-"*50)
    print(f"{"Penarikan/Widhraw 💱":^50}")
    print("-"*50)
    dana = float(input("Masukkan nominal penarikakn :IDR "))
    
    if dana >= balance:
        print("Penarikan melebihi Deposit")
        return 0
    elif dana < 0:
        print("dana harus lebih besar dari Rp0 ")
        return 0
    else:
        return dana

balance = 0
isrunning = True

while isrunning:

    match system:
        case "posix" : os.system("clear")
        case "nt" : os.system("cls")
        
    print("-"*50)
    print(f"{"Selamat datang di e-BANK":^50}")
    print("-"*50)
    print("1. Cek Saldo")
    print("2. Deposit")
    print("3. Penarikan")
    print("4. Exit")

    user = int(input("Pilih Opsi : "))
    if user == 1:
        cek_saldo()
    elif user == 2:
        balance += Deposit()
    elif user == 3:
        balance -= Penarikan()
    elif user == 4:
        isrunning = False
    else:
        print("Data anda tidal Valid")
    isdone = input("Apakah selesai Y/N -> ")
    if isdone == "y" or isdone == "Y":
        break
    
print("Semoga harimu menyenagkan")