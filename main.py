from PIL import Image
from matplotlib import image
image_file = Image.open("images/test.jpg")
width, height = image_file.size
newsize = (int(width/2), int(height/2))
new_image = image_file.resize(newsize)
new_image = new_image.convert('1')
new_image.save('result.png')
im = Image.open("result.png", 'r')
pixel_vals = list(im.getdata())
ascii_vals = []
count = 1
for val in pixel_vals:
    if count % newsize[0] == 0:
        ascii_vals.append("\n")
        count += 1
    else:
        if val == 255:
            ascii_vals.append("~")
            count += 1
        else:
            ascii_vals.append(".")
            count += 1
f = open("vals.txt", "a")
f.write(''.join(ascii_vals))
f.close()
