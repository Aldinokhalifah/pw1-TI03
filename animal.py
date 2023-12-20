class Animmal:

    def __init__(self,name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

class Badak(Animmal):

    def __init__(self, name, makanan, hidup, berkembang_biak,jenis,berat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.berat = berat

    def info(self):
        print(f"""
                Nama \t \t: {self.name}
                Makanan \t: {self.makanan}
                Hidup \t \t: {self.hidup}
                Berkembang Biak : {self.berkembang_biak}
                Jenis \t \t: {self.jenis}
                Berat \t \t: {self.berat}
                    """)


class Ikan(Animmal):
    def __init__(self, name, makanan, hidup, berkembang_biak,jenis,berat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.berat = berat

    def info(self):
        print(f"""
                Nama \t \t: {self.name}
                Makanan \t: {self.makanan}
                Hidup \t \t: {self.hidup}
                Berkembang Biak : {self.berkembang_biak}
                Jenis \t \t: {self.jenis}
                Berat \t \t: {self.berat}
                    """)

class Ular(Animmal):
     def __init__(self, name, makanan, hidup, berkembang_biak,jenis,berat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.berat = berat

     def info(self):
        print(f"""
                Nama \t \t: {self.name}
                Makanan \t: {self.makanan}
                Hidup \t \t: {self.hidup}
                Berkembang Biak : {self.berkembang_biak}
                Jenis \t \t: {self.jenis}
                Berat \t \t: {self.berat}
                    """)

x = Badak("Azzam","Rumput","Daratan","Melahirkan","Badak Bercula Satu",500)
x.info()

y= Ikan('Gihal',"Cacing","Air","Bertelur","Ikan Mas",20)
y.info()

n= Ular("Raja","Tikus","Daratan","Bertelur","Python",100)
n.info()