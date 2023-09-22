# Sebuah motor kecil digunakan untuk memberi daya pada sebuah lift yang menaikkan beban beton dengan berat 750 N sampai ketinggian 15 m dalam 20 s.
# Berapakah kecepatan motor tersebut ?
# Berapakah dkerja yang dilakukan motor tersebut ?
# Berapakah daya minimum yang harus disediakan motor tersebut ?

# Menentukan variabel
F = 750  # Gaya dalam newton
h = 15   # Ketinggian dalam meter
t = 20   # Waktu dalam detik

# Menghitung Kecepatan Motor
v = h / t

print ("Kecepatan motor adalah:", v, "m/s")

# Menghitung kerja yang dilakukan
W = F * h

print ("Kerja yang dilakukan oleh motor adalah:", W, "Joule")

# Menghitung daya
P = W / t

print("Daya minimum yang harus disediakan oleh motor:", P, "Watt")
