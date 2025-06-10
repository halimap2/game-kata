import tkinter as tk
import random

# Daftar kata berdasarkan kategori
word_categories = {
    'Buah': [
        'apel', 'pisang', 'jeruk', 'mangga', 'semangka', 'anggur',
        'nanas', 'pepaya', 'kelapa', 'strawberi', 'kiwi', 'alpukat'
    ],
    'Benda': [
        'meja', 'kursi', 'pintu', 'komputer', 'buku', 'televisi',
        'lampu', 'kulkas', 'lemari', 'telepon', 'jam', 'sepatu'
    ],
    'Hewan': [
        'kucing', 'anjing', 'gajah', 'ular', 'elang', 'singa',
        'harimau', 'zebra', 'kambing', 'sapi', 'kuda', 'koala'
    ],
    'Profesi': [
        'dokter', 'guru', 'pilot', 'polisi', 'petani', 'arsitek',
        'perawat', 'montir', 'chef', 'aktor', 'penulis', 'pemadam'
    ],
    'Transportasi': [
        'mobil', 'motor', 'kereta', 'pesawat', 'kapal', 'sepeda',
        'bus', 'truk', 'becak', 'ojek', 'perahu', 'skuter'
    ]
}


word_hints = {
    # Buah
    'apel': 'Buah berwarna merah atau hijau',
    'pisang': 'Buah berwarna kuning dan panjang',
    'jeruk': 'Buah jeruk berwarna oranye',
    'mangga': 'Buah tropis, sering dibuat jus',
    'semangka': 'Buah besar dan berair',
    'anggur': 'Buah kecil bisa dibuat wine',
    'nanas': 'Buah tropis berduri di luar, manis di dalam',
    'pepaya': 'Buah oranye, baik untuk pencernaan',
    'kelapa': 'Buah yang airnya segar',
    'strawberi': 'Buah merah kecil dengan bintik di kulitnya',
    'kiwi': 'Buah kecil berbulu dari Selandia Baru',
    'alpukat': 'Buah hijau, bisa dibuat jus atau guacamole',

    # Benda
    'meja': 'Benda untuk menaruh barang',
    'kursi': 'Benda untuk duduk',
    'pintu': 'Digunakan untuk keluar masuk ruangan',
    'komputer': 'Alat elektronik untuk bekerja',
    'buku': 'Berisi halaman-halaman untuk dibaca',
    'televisi': 'Alat untuk menonton siaran',
    'lampu': 'Memberikan penerangan saat gelap',
    'kulkas': 'Menyimpan makanan agar tetap dingin',
    'lemari': 'Tempat menyimpan pakaian atau barang',
    'telepon': 'Alat untuk berkomunikasi suara',
    'jam': 'Menunjukkan waktu',
    'sepatu': 'Dipakai di kaki saat berjalan',

    # Hewan
    'kucing': 'Hewan peliharaan yang suka mengeong',
    'anjing': 'Sahabat manusia, sering menggonggong',
    'gajah': 'Hewan besar dengan belalai',
    'ular': 'Melata tanpa kaki, bisa berbisa',
    'elang': 'Burung pemangsa yang terbang tinggi',
    'singa': 'Raja hutan dari Afrika',
    'harimau': 'Hewan besar dengan belang',
    'zebra': 'Seperti kuda, tetapi belang hitam-putih',
    'kambing': 'Hewan ternak, suka makan rumput',
    'sapi': 'Penghasil susu dan daging',
    'kuda': 'Bisa dikendarai, cepat larinya',
    'koala': 'Hewan dari Australia, tidur di pohon',

    # Profesi
    'dokter': 'Menyembuhkan orang sakit',
    'guru': 'Mengajar di sekolah',
    'pilot': 'Mengemudikan pesawat terbang',
    'polisi': 'Menjaga ketertiban dan keamanan',
    'petani': 'Bekerja di sawah atau ladang',
    'arsitek': 'Merancang bangunan',
    'perawat': 'Membantu dokter merawat pasien',
    'montir': 'Memperbaiki kendaraan',
    'chef': 'Memasak di dapur profesional',
    'aktor': 'Berperan dalam film atau sinetron',
    'penulis': 'Menulis buku atau artikel',
    'pemadam': 'Memadamkan api dan menyelamatkan orang',

    # Transportasi
    'mobil': 'Berkendara di jalan raya, punya roda 4',
    'motor': 'Kendaraan roda dua',
    'kereta': 'Berjalan di rel, membawa banyak penumpang',
    'pesawat': 'Terbang di udara, sangat cepat',
    'kapal': 'Berlayar di laut',
    'sepeda': 'Dikayuh, ramah lingkungan',
    'bus': 'Kendaraan umum berkapasitas besar',
    'truk': 'Digunakan untuk mengangkut barang berat',
    'becak': 'Transportasi tradisional beroda tiga',
    'ojek': 'Motor untuk jasa antar penumpang',
    'perahu': 'Kecil dan digunakan di sungai atau danau',
    'skuter': 'Kecil dan gesit di jalanan kota'
}


# Variabel global
time_left = 60
timer_id = None

secret_word = ''
guessed_letters = []
max_attempts = 10
attempts_left = max_attempts
hint_used = False

# Jendela utama
root = tk.Tk()
root.title("🎮 Game Tebak Kata")
root.geometry("800x700")
root.configure(bg="#d0f0f8")

# Variabel Tkinter
category_selected = tk.StringVar()
display_word = tk.StringVar()
status_text = tk.StringVar()
animation_text = tk.StringVar(value="Selamat datang di Game Tebak Kata Bahasa Daerah!")
guessed_text = tk.StringVar(value="Huruf ditebak: -")
attempts_text = tk.StringVar(value=f"Sisa Tebakan: {max_attempts}")

# Fungsi memperbarui tampilan kata
def update_display():
    display = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    display_word.set(display)
    guessed_text.set(f"Huruf ditebak: {', '.join(sorted(guessed_letters)) if guessed_letters else '-'}")
    attempts_text.set(f"Sisa Tebakan: {attempts_left}")

def guess_letter():
    global attempts_left
    if not secret_word:
        status_text.set("Pilih kategori terlebih dahulu.")
        return

    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if len(letter) == 1 and letter.isalpha():
        if letter in guessed_letters:
            status_text.set(f"Huruf '{letter}' sudah ditebak.")
        else:
            guessed_letters.append(letter)
            if letter in secret_word:
                status_text.set(f"✅ Benar! Huruf '{letter}' ada.")
            else:
                attempts_left -= 1
                status_text.set(f"❌ Salah! Huruf '{letter}' tidak ada.")
    else:
        status_text.set("Masukkan satu huruf saja.")

    update_display()

    if all(char in guessed_letters for char in secret_word):
        status_text.set("🎉 Selamat! Kamu berhasil menebak katanya!")
        disable_inputs()
    elif attempts_left <= 0:
        status_text.set(f"😢 Kamu kalah! Kata yang benar adalah '{secret_word}'.")
        disable_inputs()

def use_hint():
    global hint_used
    if hint_used:
        status_text.set("🔁 Hint sudah digunakan!")
        return
    if not secret_word:
        status_text.set("Mulai permainan dulu untuk menggunakan hint.")
        return

    remaining_letters = [l for l in secret_word if l not in guessed_letters]
    if not remaining_letters:
        status_text.set("✅ Semua huruf sudah terbuka.")
        return

    hint_letter = random.choice(remaining_letters)
    guessed_letters.append(hint_letter)
    hint_used = True
    update_display()
    status_text.set(f"💡 Hint: Huruf '{hint_letter}' telah dibuka!")

    if all(char in guessed_letters for char in secret_word):
        status_text.set("🎉 Selamat! Kamu berhasil menebak katanya!")
        disable_inputs()

def start_game():
    global secret_word, guessed_letters, attempts_left, hint_used
    guessed_letters.clear()
    attempts_left = max_attempts
    hint_used = False
    entry.config(state="normal")
    btn_guess.config(state="normal")

    category = category_selected.get()
    if category in word_categories:
        secret_word = random.choice(word_categories[category])
        update_display()
        status_text.set(f"Tebak kata dari kategori '{category}'")
    else:
        status_text.set("Pilih kategori yang valid!")

        global time_left, timer_id
    time_left = 60  # Atur sesuai durasi timer yang diinginkan
    timer_text.set(f"Waktu Tersisa: {time_left} detik")
    if timer_id:
        root.after_cancel(timer_id)
    countdown()


def reset_game():
    display_word.set("")
    guessed_text.set("Huruf ditebak: -")
    attempts_text.set(f"Sisa Tebakan: {max_attempts}")
    status_text.set("Pilih kategori dan mulai permainan.")
    category_selected.set("")
    entry.config(state="normal")
    btn_guess.config(state="normal")

def disable_inputs():
    entry.config(state="disabled")
    btn_guess.config(state="disabled")

def countdown():
    global time_left, timer_id
    if time_left > 0:
        time_left -= 1
        timer_text.set(f"Waktu Tersisa: {time_left} detik")
        timer_id = root.after(1000, countdown)
    else:
        status_text.set(f"⏰ Waktu habis! Kata yang benar adalah '{secret_word}'.")
        disable_inputs()


def animate_text():
    current = animation_text.get()
    new_text = current[1:] + current[0]
    animation_text.set(new_text)
    root.after(200, animate_text)

    global time_left, timer_id
    time_left = 60
    timer_text.set(f"Waktu Tersisa: {time_left} detik")
    if timer_id:
        root.after_cancel(timer_id)


# UI Layout
label_title = tk.Label(root, textvariable=animation_text, font=("Helvetica", 20, "bold"),
                       bg="#d0f0f8", fg="blue")
label_title.pack(pady=20)

frame_kategori = tk.Frame(root, bg="#d0f0f8")
frame_kategori.pack(pady=10)
tk.Label(frame_kategori, text="Kategori:", bg="#d0f0f8", font=("Helvetica", 16)).pack(side='left', padx=10)
option_menu = tk.OptionMenu(frame_kategori, category_selected, *word_categories.keys())
option_menu.config(font=("Helvetica", 16))
option_menu.pack(side='left', padx=10)
btn_start = tk.Button(frame_kategori, text="Mulai", command=start_game, font=("Helvetica", 16), bg="#ffffff")
btn_start.pack(side='left', padx=10)
btn_reset = tk.Button(frame_kategori, text="Reset", command=reset_game, font=("Helvetica", 16), bg="#ffe0e0")
btn_reset.pack(side='left', padx=10)

label_word = tk.Label(root, textvariable=display_word, font=("Courier", 40, "bold"), bg="#d0f0f8")
label_word.pack(pady=30)

entry = tk.Entry(root, font=("Helvetica", 24), width=5, justify='center')
entry.pack()
btn_guess = tk.Button(root, text="Tebak", command=guess_letter, font=("Helvetica", 18), bg="#e0ffe0")
btn_guess.pack(pady=15)

btn_hint = tk.Button(root, text="💡 Hint", command=use_hint, font=("Helvetica", 16), bg="#FFC107", fg="black")
btn_hint.pack(pady=10)

label_guessed = tk.Label(root, textvariable=guessed_text, font=("Helvetica", 14), bg="#d0f0f8")
label_guessed.pack(pady=5)
label_attempts = tk.Label(root, textvariable=attempts_text, font=("Helvetica", 14), bg="#d0f0f8")
label_attempts.pack(pady=5)
timer_text = tk.StringVar(value="Waktu Tersisa: 60 detik")
label_timer = tk.Label(root, textvariable=timer_text, font=("Helvetica", 14), bg="#d0f0f8", fg="red")
label_timer.pack(pady=5)
label_status = tk.Label(root, textvariable=status_text, font=("Helvetica", 14), bg="#d0f0f8", fg="darkgreen", wraplength=700)
label_status.pack(pady=15)

difficulty_selected = tk.StringVar(value="Sedang")

frame_difficulty = tk.Frame(root, bg="#E0F7FA")
frame_difficulty.pack()

tk.Label(frame_difficulty, text="Tingkat Kesulitan:", font=("Helvetica", 12), bg="#E0F7FA").pack(side='left')
tk.OptionMenu(frame_difficulty, difficulty_selected, "Mudah", "Sedang", "Sulit").pack(side='left', padx=5)

btn_hint = tk.Button(root, text="Lihat Petunjuk", font=("Helvetica", 10), bg="#FFEB3B", command=lambda: status_text.set("Petunjuk: " + word_hints.get(secret_word, "Tidak tersedia")))
btn_hint.pack(pady=5)


# Inisialisasi
animate_text()
update_display()
root.mainloop()
