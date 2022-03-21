

from PIL import Image


colorImage  = Image.open("croiseur_de_grasse_resized.png")

transposed  = colorImage.transpose(Image.ROTATE_90)


transposed.show()