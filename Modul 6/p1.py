from PIL import Image, ImageDraw, ImageFont

gambar = Image.open('../Modul 6/tein.jpg')
gambarBW = gambar.convert("L")
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype("arial.ttf", 12)
text = "saSJFDNBNJDFGNl"
text_bbox = draw.textbbox((0, 0), text, font=font)  # Use draw.textbbox to get the bounding box
text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
text_x = (gambarBW.width - text_width) // 2
text_y = 20
draw.text((text_x, text_y), text, font=font, fill="red")
gambarBW.save('../Modul 6/hasil.jpg')
gambarBW.show()
