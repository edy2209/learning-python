
#program sederhana boking hotel
harga_total = []
tipe_hotel = []
lama_inap = []

print('         HOTEL PANGERAN BEACH\n==========================================\n\
|| kode || jenis kamar || harga permalam ||\n==========================================\n\
S           Single       Rp100.000\nD           double       Rp350.000\nF           Family       Rp.550.000')


def menu():
    sewa=int(input('mau sewa berapa kamar : '))
    for i in range (sewa):
        kode=str(input('kode jenis kamar :'))
        if (kode=='S'):
            print('kamar anda adalah : Singel')
            lama=int(input('lama inap anda: '))
            harga=100000
            jharga=harga*lama
            harga_total.append(jharga)
            tipe_hotel.append("Singel")
            lama_inap.append(lama)
        
        elif (kode=='D'):
            print('kamar anda adalah : Double')
            lama=int(input('lama inap anda: '))
            harga=350000
            jharga=harga*lama
            harga_total.append(jharga)
            tipe_hotel.append("Double")
            lama_inap.append(lama)
            
        elif (kode=='F'):
            print('kamar anda adalah : Family')
            lama=int(input('lama inap anda: '))
            harga=550000
            jharga=harga*lama
            harga_total.append(jharga)
            tipe_hotel.append("Family")
            lama_inap.append(lama)
            
        #bonus jika lebih dari 2 jt
        else:
            print('menu tidak tersedia')
    print('**************HOTEL PANGERAN BEACH*****************')
    print('====================================================')
    print("No.\tJenis Kamar\tHarga per malam\t\tlama inap\tJumlah harga")
    totalharga = 0
    count = 0
    for data in harga_total:
        print(str(count + 1)+".\t"+str(tipe_hotel[count])+"\t\t"+str(data / lama_inap[count])+"\t\t"+str(lama_inap[count])+"\t\t"+str(data))
        totalharga += data
        count += 1
    print('====================================================')
    print('\t\t\ttotal bayar anda :',totalharga)
    if (totalharga>2000000):
        print('\t\t\tbonus:  handuk')
    else:
        print('\t\t\tbonus:  totebag')
        
menu()


    