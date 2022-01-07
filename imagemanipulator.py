from PIL import Image, ImageEnhance, ImageFile
import random, shutil, os
ImageFile.LOAD_TRUNCATED_IMAGES = True
def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)


randint = random.randint(1, 6) #TODO: Make max limit the amount of files inside the "images" folder
rand = str(randint)
randSaturation = random.randint(0, 55)
randBrightness = random.uniform(0, 2)
randContrast = random.randint(0, 255)
file = './images/' + rand + '.png'
im = Image.open(file)
os.remove('processedImages/done.png')
os.remove('processedImages/done2.png')
os.remove('processedImages/done3.png')

converterSaturation = ImageEnhance.Color(im)
new_image = converterSaturation.enhance(randSaturation)
new_image.save("processedImages/done.png")
converterBrightness = ImageEnhance.Brightness(Image.open('processedImages/done.png'))
new_image = converterBrightness.enhance(randBrightness)
new_image.save("processedImages/done2.png")
converterContrast = change_contrast(Image.open('processedImages/done2.png'), randContrast)
new_image = converterContrast
new_image.save("processedImages/done3.png")
#please don't ask what this mess of code is