def view():
  
  v="""
  =========Nama Peminjam Buku===============
        Universitas Metamedia
  
  """
  print(v)
view()

list_buku=[]
list_nama=[]
perulangan=int(input('masukan jumlah buku : '))
for data in range (perulangan):
    nama=str(input('masukan nama : '))
    buku=input("judul buku : ")
    list_buku.append(buku)
    list_nama.append(nama)
m="""
  =======================================
  || NO.        NAMA.        JUDUL BUKU.||
  =======================================
  """
print(m)
for num,data in enumerate(list_buku):
    print("||",num+1,"        ",list_nama[num],"         ",list_buku[num],"||")



  
  
  
  
