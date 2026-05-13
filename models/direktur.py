from.menejer import Menejer

class Direktur(Menejer):
    def __init__(self, nama: str, gaji_pokok: float, id_pegawai: str, departemen: str, tunjangan: float, jumlah_tim: int, bonus_tahunan : float, saham_perusahaan : int):
        super().__init__(nama, gaji_pokok, id_pegawai, departemen, tunjangan, jumlah_tim)
        self.bonus_tahunan = bonus_tahunan
        self.saham_perusahaan = saham_perusahaan

    def hitung_gaji(self) -> float:
        return super().hitung_gaji() + (self.bonus_tahunan /12)
    
    def get_info(self) -> str:
        return(
            super().get_info()+
            f"\nBonus Tahunan:RP {self.bonus_tahunan:,.0f}"
            f"\nSaham Perusahaan: {self.saham_perusahaan}%"
        )
    
    def tetapkan_kebijakan(self, kebijakan: str) -> str:
        print(f" [Direktur] {self.nama} menetapkan kebijakan:\"{kebijakan}\"")

    def __str__(self) -> str:
        return self.get_info()
