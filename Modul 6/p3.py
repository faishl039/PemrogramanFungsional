from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan Pillow
image = Image.open('../Modul 6/tein.jpg')

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(2.5)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
final_image.save("percobaan_tiga.jpg")

# TODO 4: Tampilkan
final_image.show()
