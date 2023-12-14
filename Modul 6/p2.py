from PIL import Image

bg_image = Image.open('../Modul 6/pemandangan.jpg')
overlay = Image.open('../Modul 6/tein.jpg')
# overlay = overlay.convert('RGB')
ov_image = Image.new("RGB", overlay.size, (255, 255, 255))
ov_image.paste(overlay, mask=overlay.split()[1])
# ov_image.save('../Modul 6/ov.jpg')
# ov_image.show()
# bg_image.show()
# x_center = 50
# y_center = 50
# ov_image = ov_image.resize((200, 200))
# bg_image.paste(ov_image, (x_center, y_center), ov_image)
bg_image.paste(ov_image)
bg_image.save("percobaan_dua.jpg")
bg_image.show()