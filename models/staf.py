from .pegawai import Pegawai

class Staf(Pegawai):
    def __init__(self, id_pegawai:str, nama:str, departemen:str, gaji_pokok:float, jam_lembur:int, tarif_lembur:float):
        super().__init__(id_pegawai, nama, departemen, gaji_pokok)
        self.jam_lembur = jam_lembur
        self.tarif_lembur = tarif_lembur

    def hitung_gaji(self) -> float:
        return super().hitung_gaji() + (self.jam_lembur * self.tarif_lembur)
    
    def get_info(self):
        return(
            super().get_info() + "\n"
            f"Jam Lembur: {self.jam_lembur}\n"
            f"Tarif Lembur: {self.tarif_lembur}"
        )
    
    def input_laporan(self):
        print(f' [Staf] {self.nama} menginput laporan harian ke depertemen {self.departemen}')

    def __str__(self):
        return self.get_info()