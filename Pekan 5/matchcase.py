#untuk laki-laki
#beratL = (tinggi-100) - (tinggi-100) * 0.1

#untuk perempuan
#beratP = (tinggi-100) - (tinggi-100) * 0.15

print("sistem penghitung berat badan ideal")
print("""
sistem penghitung berat badan ideal
      
pilih jenis kelamin:
1 = Laki-laki
2 = Perempuan
""")

jk = int(input("Masukkan pilihan jenis kelamin: "))
tinggi = int(input("Masukkan tinggi badan: "))

match jk:
    case 1:
        ideal = (tinggi-100) - (tinggi-100) * 0.1
        print("berat badan ideal laki-laki unntuk tinggi", tinggi,"adalah", ideal)
    case 2:
         ideal = (tinggi-100) - (tinggi-100) * 0.15
         print("berat badan ideal perempuan untuk  tinggi", tinggi,"adalah", ideal)
    case _:
        print("Plihan yang anda masukkan tidak valid.")


