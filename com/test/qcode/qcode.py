#coding:utf-8
from PIL import Image
import qrcode


'''

qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
qr.add_data("http://www.cnblogs.com/")
qr.make(fit=True)

img = qr.make_image()
img = img.convert("RGBA")

# logo="D:/favicon.jpg"
icon = Image.open("D:/self/图片/time.jpg")

img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)

icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
icon = icon.convert("RGBA")
img.paste(icon, (w, h), icon)

# img.show()
img.save('createlogo.png', quality=100)
'''
def create_qrcode(url, filename):
    qr = qrcode.QRCode(
        version=1,
        #设置容错率为最高
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
  
    img = qr.make_image()
    #设置二维码为彩色
    img = img.convert("RGBA")
    icon = Image.open("D:\\self\\图片\\time.jpg")
    w, h = img.size
    factor = 4
    size_w = int(w / factor)
    size_h = int(h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((w - icon_w) / 2)
    h = int((h - icon_h) / 2)
    icon = icon.convert("RGBA")
    newimg = Image.new("RGBA", (icon_w + 8, icon_h + 8), (255, 255, 255))
    img.paste(newimg, (w-4, h-4), newimg)
  
    img.paste(icon, (w, h), icon)
    img.save(filename + '.png', quality=100)
if __name__ == '__main__':
    m=input("请输入二维码文字 or url：")
    create_qrcode(m,"image_code")
