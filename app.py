from utils import tambah, kurang
from models import DataManager

def main():
    print("=== Aplikasi DevSecOps Sederhana ===")
    dm = DataManager("Data Siswa")
    dm.tambah_item("Yulia")

    hasil_tambah = tambah(10, 5)
    hasil_kurang = kurang(10, 5)

    print(f"Hasil Tambah: {hasil_tambah}")
    print(f"Hasil Kurang: {hasil_kurang}")
    print(f"Data tersimpan: {dm.ambil_semua()}")

if __name__ == "__main__":
    main()