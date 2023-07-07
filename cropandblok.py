from PIL import Image, ImageDraw

# Membuka gambar
image = Image.open("image2.jpg")

# Mendapatkan ukuran gambar
width, height = image.size

# Menghitung ukuran setiap bagian
piece_width = width // 3
piece_height = height // 3

# Membuat gambar kosong dengan latar belakang putih
white_image = Image.new("RGB", (piece_width, piece_height), "white")

# Membuat objek ImageDraw
draw = ImageDraw.Draw(white_image)

# Memotong dan menambahkan tanda blok hitam pada setiap bagian gambar
for i in range(3):
    for j in range(3):
        left = j * piece_width
        top = i * piece_height
        right = (j + 1) * piece_width
        bottom = (i + 1) * piece_height

        piece = image.crop((left, top, right, bottom))

        # Menggambar tanda blok hitam pada setiap bagian
        draw.rectangle([(0, 0), (piece_width, piece_height)], fill="black")

        # Menggabungkan bagian gambar dengan tanda blok hitam
        combined_image = Image.alpha_composite(white_image.convert("RGBA"), piece)

        # Menampilkan setiap bagian gambar yang telah dimodifikasi
        combined_image.show()
