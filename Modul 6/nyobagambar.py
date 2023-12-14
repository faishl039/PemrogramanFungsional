# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# img = mpimg.imread('../Modul 6/tc105.jpeg')

# print('a')
# plt.imshow(img)
# plt.axis('off')
# plt.show()

from PIL import Image, ImageFilter

img = Image.open('../Modul 6/tc105.jpeg')
rotated_image = img.rotate(45)
blurred_image = img.filter(ImageFilter.BLUR)
sepia_image = img.convert('RGB', matrix=[(0.272, 0.534, 0.131),
(0.349, 0.686, 0.168),
(0.393, 0.769, 0.189)])
sepia_image.show()