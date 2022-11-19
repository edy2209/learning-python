#program atm sederhana
def pin():
    mpin=int(input('masukan pin anda : '))
    if (mpin==220901):
        print('selamat anda berhasil login')
        
    else:
        print('pasword yang anda masukan salah,silahkan input kembali\
        pin anda!!')
        pin()

pin()
def yatidak():
    print('          apakah anda ingin melanjutakan transaksi\n\
        ==============================================\
            \n1.YA\n2.TIDAK')
    inp=int(input('pilihan : '))
    if (inp==1):
        print('silahkan masukan pilihan')
        menu()
    elif (inp==2):
        print('silahkan ambil kartu anda !!!!\n============================\n\
            terima kasih sudah betransaksi')
    else:
        print('data tidak ditemukan')

def menu():
    
    
    print('selamat datang di bank suka suka\n=================================\n1.cek saldo\n2.transfer dana\n3.tarik dana\
    \n4.keluar atm\n5.logout')
    pil=int(input('masukan pilihan anda :'))
    saldo=2000000
    if (pil==1):
        print('saldo anda sebesar',saldo)
        yatidak()
        
    elif (pil==2):
        tambah=int(input('masukan nominal : '))
        nama=str(input('masukan nama : '))
        norek=int(input('masukan nomor rekening :'))
        if (tambah < 50000):
            print('saldo harus di atas Rp.50000')
        else:
            total=saldo-tambah
            print('saldo berhasil ditransfer ke :',nama ,'no rekening :',norek,'sebesar',tambah)
            print('total saldo anda sekarang',total)
            yatidak()
        
    elif (pil==3):
        tarik=int(input('masukan nominal : '))
        if (tarik > saldo):
            print('saldo anda tidak cukup')
        else:
            total=saldo-tarik
            print('saldo anda berkurang sebesar Rp.',tarik)
            print('total saldo anda sekaranag',total)
            yatidak()
    elif (pil==4):
        print('terima kesih')
        pin()
        menu()
    elif (pil==5):
        print('             terima kasih sudah bertransaksi\n\
        ===========================================\n\
                    di bank suka suka')

        
    
menu()



