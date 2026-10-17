class DataManager:
    def __init__(self, nama_koleksi):
        self.nama_koleksi = nama_koleksi
        self.items = []

    def tambah_item(self, item):
        if item:
            self.items.append(item)

    def ambil_semua(self):
        return self.items