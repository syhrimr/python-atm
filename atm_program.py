import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan PIN Anda: "))
    trial = 0

    # Verifikasi
    while (id != int(atm.checkPin()) and trial < 3 ):
        id = int(input("PIN Anda salah. Silakan masukkan lagi: "))
        trial += 1

        if trial == 3:
            print("Error! Silakan ambil kartu dan coba lagi...")
            exit()

    # Menu
    while True:
        print("Selamat datang di ATM Progate...")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti PIN \t 5 - Keluar")
        selectmenu = int(input("\nSilakan pilih menu: "))

        if selectmenu == 1:
            print("\nSaldo Anda sekarang: Rp " + str(atm.checkSaldo()) + "\n")
        elif selectmenu == 2:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut? Y/N " + str(nominal) + " ")

            if verify_withdraw == "y":
                print("Saldo awal Anda adalah: Rp " + str(atm.checkSaldo()) + "")
            else:
                break
            
            if nominal < atm.checkSaldo():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil!")
                print("Sisa saldo sekarang: Rp " + str(atm.checkSaldo()) + "")
            else:
                print("Maaf! Saldo Anda tidak cukup")
                print("Silakan lakukan penambahan saldo")
        elif selectmenu == 3:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut? Y/N " + str(nominal) + " ")
 
            if verify_withdraw == "y":
                atm.depositBalance(nominal)
                print("Saldo Anda sekarang adalah: Rp " + str(atm.checkSaldo()) + "")
            else:
                break
        elif selectmenu == 4:
            verify_pin = int(input("Masukkan pin anda: "))
            
            while verify_pin != int(atm.checkPin()):
                print("PIN Anda salah. Silakan masukkan PIN: ")
            
            updated_pin = int(input("Silakan masukkan PIN baru: "))
            print("PIN Anda berhasil diganti!")

            verify_newpin = int(input("Coba masukkan PIN baru: "))
 
            if verify_newpin == updated_pin:
                print("PIN berhasil diganti!")
            else:
                print("Maaf, PIN tidak sesuai!")
        elif selectmenu == 5:
            print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi Anda.")
            print("No. Resi: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo Akhir: ", atm.checkSaldo())
            print("Terima kasih telah menggunakan ATM Progate!")
            exit()
        else:
            print("Maaf, menu tidak tersedia!")
