class pesawat():
    def __init__(self, nama, kapasitas):
        self.nama = nama
        self.kapasitas = kapasitas
        
plane1 = pesawat("Boeing 747", 416)
plane2 = pesawat("Airbus A380", 853)

print(plane1.nama, plane1.kapasitas)
print(plane2.nama, plane2.kapasitas)
