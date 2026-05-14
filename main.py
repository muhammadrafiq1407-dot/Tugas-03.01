import sys
import os


from models.pegawai  import Pegawai
from models.staf     import Staf
from models.menejer  import  Menejer
from models.direktur import Direktur

from utils.display import (
    cetak_heder,
    tampilkan_semua_pegawai,
    tampilkan_fitur_khusus,
    tampilkan_subtyping_check,
    tampil_ringkasan_gaji,
)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

def buat_data_pegawai():
    staf1     = Staf("S001", "Budi Santoso",   "IT",        5_000_000, 10, 50_000)
    staf2     = Staf("S002", "Rina Amalia",    "Keuangan",  4_500_000,  5, 50_000)
    staf3     = Staf("S003", "Doni Pratama",   "Marketing", 4_800_000,  8, 50_000)
    manajer1  = Menejer("M001", "Ahmad Fauzi", "IT",       10_000_000, 3_000_000, 5)
    manajer2  = Menejer("M002", "Siti Rahma",  "Keuangan",  9_500_000, 2_500_000, 4)
    direktur1 = Direktur(
        "D001", "Hendra Wijaya", "Direksi",
        20_000_000, 8_000_000, 15,
        60_000_000, 5.
    )
    return [staf1, staf2, staf3, manajer1, manajer2, direktur1]


def main():
    cetak_heder("Sistem Manajemen SDM (HRD)")
    print("  Aplikasi pengelolaan data pegawai dan penggajian.")
    print("  Konsep: Inheritance | super() | Subtyping")

    semua_pegawai = buat_data_pegawai()


    daftar_staf    = [p for p in semua_pegawai if isinstance(p, Staf)]
    daftar_manajer = [p for p in semua_pegawai
    if isinstance(p, Menejer) and not isinstance(p, Direktur)]
    direktur       = next(p for p in semua_pegawai if isinstance(p, Direktur))


    tampilkan_semua_pegawai(semua_pegawai)


    tampilkan_fitur_khusus(daftar_staf, daftar_manajer, direktur)


    tampilkan_subtyping_check(semua_pegawai)


    tampil_ringkasan_gaji(semua_pegawai)


if __name__ == "__main__":
    main()