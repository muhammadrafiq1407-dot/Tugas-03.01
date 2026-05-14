from models.pegawai import Pegawai
from models.menejer import Menejer
from models.direktur import Direktur    
from models.staf import Staf

def cetak_heder(judul: str):
    lebar = 57
    print("\n" + "=" * lebar)
    print(f" {judul.upper()}")
    print("=" * lebar)

def cetak_pemisah():
    print("-" * 57)

def tampilkan_detail_pegawai(pegawai: Pegawai):
    print(pegawai)
    pegawai.tampilkan_gaji()
    cetak_pemisah()

def tampilkan_semua_pegawai(daftar : list):
    cetak_heder("Data &  Gaji Seluruh Pegawai")
    for pegawai in daftar:
        tampilkan_detail_pegawai(pegawai)

def tampilkan_fitur_khusus(daftar_staf: list, daftar_menejer: list, direktur: Direktur):
    cetak_heder("Fitur Khusus Per Peran")
    for s in daftar_staf:
        s.input_laporan()
    for m in daftar_menejer:
        m.pimpin_rapat()

    direktur.tetapkan_kebijakan("Kita setiap jumat akan work from home ")
    direktur.tetapkan_kebijakan("Evaluasi kinerja tahunan akan dilakukan setiap bulan desember")

def tampilkan_subtyping_check(daftar: list):
    cetak_heder("Verifikasi subtyping dengan isinstance()")
    print(f" {'Nama':<22} {'Pegawai':<10} {'Staf':<8} {'Menejer':<10} {'Direktur'}")
    cetak_pemisah()
    for p in daftar:
        print(
            f"  {p.nama:<22}"
            f"{'Ya':<10}" if isinstance(p, Pegawai)  else f"  {p.nama:<22}{'Tidak':<10}",
            end=""
        )
        print(f"{'Ya':<8}"  if isinstance(p, Staf)      else f"{'Tidak':<8}",  end="")
        print(f"{'Ya':<10}" if isinstance(p, Menejer)   else f"{'Tidak':<10}", end="")
        print(f"{'Ya'}"     if isinstance(p, Direktur)  else f"{'Tidak'}")


def tampil_ringkasan_gaji(daftar: list):
    cetak_heder("Ringkasan Pengeluaran Gaji")
    total_gaji     = sum(p.hitung_gaji() for p in daftar)
    gaji_per_peran = {}

    for p in daftar:
        peran = p.__class__.__name__
        if peran not in gaji_per_peran:
            gaji_per_peran[peran] = []
        gaji_per_peran[peran].append(p.hitung_gaji())

    for peran, gaji_list in gaji_per_peran.items():
        rata2  = sum(gaji_list) / len(gaji_list)
        jumlah = len(gaji_list)
        print(f"  {peran:<12} | {jumlah} orang | Rata-rata: Rp{rata2:,.0f}")

    cetak_pemisah()
    print(f"  Total Pengeluaran Gaji Perusahaan: Rp{total_gaji:,.0f}")
