class Queue:
    def __init__(self, capacity=None):
        self.items = []
        self.capacity = capacity  # None berarti tidak terbatas

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        if self.capacity is None:
            return False
        return len(self.items) >= self.capacity

    def enqueue(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            print("Antrian penuh. Tidak bisa menambahkan:", item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.items)

    def display(self):
        if not self.is_empty():
            print("Isi antrian:", self.items)
        else:
            print("Antrian kosong.")
# Membuat antrian dengan kapasitas maksimal 3
antrian = Queue(capacity=3)

# Menambahkan elemen
antrian.enqueue("Pelanggan 1")
antrian.enqueue("Pelanggan 2")
antrian.enqueue("Pelanggan 3")

# Mencoba menambahkan saat antrian penuh
antrian.enqueue("Pelanggan 4")

# Menampilkan semua isi antrian
antrian.display()

# Melihat elemen pertama tanpa menghapusnya
print("Yang akan dipanggil selanjutnya:", antrian.peek())

# Menghapus satu elemen
print("Panggilan ke kasir:", antrian.dequeue())

# Menampilkan isi antrian setelah dequeue
antrian.display()
