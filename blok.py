from PIL import Image, ImageDraw

# Membuka foto
image = Image.open("image1.jpg")

# Membuat objek ImageDraw
draw = ImageDraw.Draw(image)

# Menggambar titik-titik hitam pada foto
point1 = (50, 50)
point2 = (200, 150)
point3 = (300, 250)

draw.point(point1, fill="black")
draw.point(point2, fill="black")
draw.point(point3, fill="black")

# Menyimpan gambar yang telah diubah
image.save("image1_titik.jpg")
