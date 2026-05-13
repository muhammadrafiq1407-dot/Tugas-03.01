class Pegawai:
    def __init__(self, id_pegawai:str, nama:str, departemen:str, gaji_pokok:float):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.departemen = departemen
        self.gaji_pokok = gaji_pokok

    def get_info(self):
        return(
            f"ID Pegawai: {self.id_pegawai}\n"
            f"Nama: {self.nama}\n"
            f"Departemen: {self.departemen}\n"
            f"Gaji Pokok: {self.gaji_pokok}"
        )
    
    def hitung_gaji(self) -> float:
        return self.gaji_pokok
    

    def tampilkan_gaji(self):
        total = self.hitung_gaji()
        print(f" >> [{self.__class__.__name__}]{self.nama} Total Gaji: {total:,.0f}")

        def __str__(self):
            return self.get_info()

        