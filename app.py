import qrcode

print('Enter your name:')
name = input()

img = qrcode.make(name)
type(img)
img.save("qr.png")
