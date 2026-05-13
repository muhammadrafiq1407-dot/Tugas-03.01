from .pegawai import Pegawai


class Menejer(Pegawai):
    def __init__(self, id_pegawai:str, nama:str, departemen:str, gaji_pokok:float, tunjangan:float, jumlah_tim:int):
        super().__init__(id_pegawai, nama, departemen, gaji_pokok)
        self.tunjangan = tunjangan
        self.jumlah_tim = jumlah_tim

    def hitung_gaji(self) -> float:
        return super().hitung_gaji() + self.tunjangan
    
    def get_info(self):
        return(
            super().get_info() + "\n"
            f"Tunjangan: {self.tunjangan}\n"
            f"Jumlah Tim: {self.jumlah_tim}"
        )
    
    def pimpin_rapat(self):
        print(f' [Menejer] {self.nama} memimpin rapat dengan tim sebanyak {self.jumlah_tim} anggota di depertemen {self.departemen}')

    def __str__(self):
        return self.get_info()