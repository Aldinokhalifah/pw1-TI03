#luas persegi = L = s * s
#luas lingkaran = L = π * r * r 
#luas segitiga = L = 1/2 * a * t

print("""menghitung luas bangun datar
      
      pilih bangun datar yang akan dihitung:
      1.Menghitung luas persegi
      2.Menghitung luas lingkaran
      3.Menghitung luas segitiga
      """)
    
bangun_datar=int(input("masukkan angka"))

match bangun_datar:
    case 1 :
        s= int(input("masukkan angka"))
        rumus1= (s * s) 
        print("hasil dari penghitungan luas persegi adalah",rumus1)
    case 2 :
        π= int(3.14)
        r= int(input("masukkan angka"))
        rumus2= ( π * r * r )
        print("hasil dari penghitungan luas lingkaran adalah",rumus2)
    case 3 :
        a= int(input("masukkan angka"))
        t= int(input("masukkan angka"))
        rumus3= (1/2 * a * t)
        print("hasil dari penghitungan luas lingkaran adalah",rumus3)
    case _:
        print("Plihan yang anda masukkan tidak valid.")
    



