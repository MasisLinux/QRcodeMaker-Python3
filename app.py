import qrcode

value = input('Value: ')
img = qrcode.make(value)

img.save('myqrcode.png')