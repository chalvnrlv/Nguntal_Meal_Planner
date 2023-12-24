from customtkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Define custom colors
dark_yellow = "#FFD700"  # Dark Yellow
dark_red = "#8B0000"     # Dark Red
white = "#FFFFFF"  # White

# Dictionary untuk menyimpan resep
resep = {
    "Nasi goreng": ["Beras", "Daging Ayam", "Bawang Merah", "Bawang Putih", "Kecap Manis", "Kecap Asin", "Cabe", "Ebi Kering", "Garam"],
    "Tahu Tempe Bacem": ["Tahu", "Tempe", "Kecap Manis", "Air Kelapa", "Gula Merah", "Asam Jawa", "Kemiri", "Bawang Merah", "Bawang Putih"],
    "Soto Ayam": ["Daging Ayam", "Bawang Merah", "Bawang Putih", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Garam"],
    "Rendang": ["Daging Sapi", "Santan", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Ayam Bakar": ["Daging Ayam", "Kecap Manis", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Ikan Bakar": ["Ikan", "Kecap Manis", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Sate Ayam": ["Daging Ayam", "Kecap Manis", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Sate Kambing": ["Daging Kambing", "Kecap Manis", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Gado-gado": ["Sayuran Campur", "Kacang Tanah", "Kecap Manis", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Pecel": ["Sayuran Campur", "Kacang Tanah", "Kecap Manis", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Ketoprak": ["Tahu", "Tempe", "Kecap Manis", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Lontong Sayur": ["Sayuran Campur", "Kacang Tanah", "Kecap Manis", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Opor Ayam": ["Daging Ayam", "Santan", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Ayam Goreng": ["Daging Ayam", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Tempe Goreng": ["Tempe", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Tahu Goreng": ["Tahu", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Perkedel": ["Kentang", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Sayur Asem": ["Sayuran Campur", "Asam Jawa", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Sayur Lodeh": ["Sayuran Campur", "Santan", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"],
    "Bakso": ["Daging Sapi", "Tepung Kanji", "Bawang Merah", "Bawang Putih", "Kemiri", "Kunyit", "Jahe", "Serai", "Daun Jeruk", "Cabe", "Garam"]

}

# List untuk menyimpan jenis protein dalam setiap masakan
protein = {
    "Nasi goreng": "Ayam",
    "Tahu Tempe Bacem": ["Tahu", "Tempe"],
    "Soto Ayam": "Ayam",
    "Rendang": "Sapi",
    "Ayam Bakar": "Ayam",
    "Ikan Bakar": "Ikan",
    "Sate Ayam": "Ayam",
    "Sate Kambing": "Kambing",
    "Gado-gado": ["Tahu", "Tempe"],
    "Pecel": ["Tahu", "Tempe"],
    "Ketoprak": ["Tahu", "Tempe"],
    "Lontong Sayur": ["Tahu", "Tempe"],
    "Opor Ayam": "Ayam",
    "Ayam Goreng": "Ayam",
    "Tempe Goreng": "Tempe",
    "Tahu Goreng": "Tahu",
    "Perkedel": "Kentang",
    "Sayur Asem": "Sayuran",
    "Sayur Lodeh": "Sayuran",
    "Bakso": "Sapi"
}

# List untuk menyimpan apakah masakan bersantan atau tidak
santan = ["Opor Ayam", "Rendang", "Sayur Lodeh"]

def cari_masakan(bahan):
    masakan_mungkin = {masakan: set(resep[masakan]) - set(bahan) for masakan in resep if len(set(resep[masakan]) - set(bahan)) <= 5}
    return dict(sorted(masakan_mungkin.items(), key=lambda item: len(item[1])))

def is_valid(masakan, jadwal, hari):
    if masakan in jadwal:
        return False

    if protein[masakan] in ["Ayam", "Daging Ayam", "Daging Sapi"] and list(protein.values()).count("Daging") < 3:
        return False

    if hari > 0 and protein[masakan] == protein[jadwal[hari-1]]:
        return False

    if masakan in santan and jadwal.count(masakan) >= 2:
        return False

    return True

def solve_csp(jadwal, hari, masakan_mungkin):
    if hari == 7:
        return True

    for masakan in masakan_mungkin:
        if is_valid(masakan, jadwal, hari):
            jadwal[hari] = masakan

            if solve_csp(jadwal, hari + 1, masakan_mungkin):
                return True

            jadwal[hari] = None

    return False

def create_schedule():
    # Input bahan dari antarmuka pengguna
    bahan_input = entry_bahan.get().split(", ")

    # Cari masakan yang mungkin
    masakan_mungkin = cari_masakan(bahan_input)

    # Inisialisasi jadwal
    jadwal = [None] * 7

    # Mulai dari hari Senin (index 0)
    if solve_csp(jadwal, 0, masakan_mungkin):
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Jadwal masakan:\n")
        for hari, masakan in zip(["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"], jadwal):
            result_text.insert(tk.END, f"{hari}: {masakan}\n")

            if masakan and masakan in masakan_mungkin:
                bahan_kurang = masakan_mungkin[masakan]
                if bahan_kurang:
                    result_text.insert(tk.END, f"   Bahan yang kurang: {', '.join(bahan_kurang)}\n")
        result_text.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Informasi", "Tidak ada solusi untuk jadwal masakan.")

# Membuat antarmuka pengguna Tkinter
app = tk.Tk()
app.title("Nguntal: Your Food Planner!")
app.geometry("800x600")  # Set the window size
app.configure(bg="#761111")
app.option_add("*Font", "Montserrat")

# Label dan Entry untuk input bahan
label_bahan = tk.Label(master=app, text="Masukkan Bahan (Pisahkan dengan Koma):", font=("Montserrat-Bold", 20), fg=white, bg="#761111")
label_bahan.pack(pady=10)
entry_bahan = tk.Entry(master=app, width=50, bg=white)
entry_bahan.pack(pady=10)

# Tombol untuk membuat jadwal
button_create_schedule = tk.Button(master=app, text="BUAT", font=("Montserrat-Bold"), command=create_schedule, bg=dark_yellow, fg="#000000")
button_create_schedule.pack(pady=10)

# Text untuk menampilkan hasil jadwal
result_text = tk.Text(app, height=15, width=60, background="#1D1010", foreground=white, state=tk.DISABLED, relief=tk.GROOVE, bd=5)
result_text.pack(pady=10)

app.mainloop()