# basic qr code
import qrcode

data = 'Don\'t forget to subscribe'
img = qrcode.make(data)
img.save('Projects/myqrcode1.png')

# adding formatting 
data = 'Don\'t forget to subscribe'

qr = qrcode.QRCode(version = 1, box_size=10, border = 5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = 'red', back_color = 'white')
img.save('Projects/myqrcode.png')

# decoding a qr code
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('Projects/myqrcode.png')
result = decode(img)
print(result)
