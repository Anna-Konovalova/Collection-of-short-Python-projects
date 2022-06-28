#pip install pyqrcode
#pip install pypng

import pyqrcode 
from pyqrcode import QRCode 
import png

#User link for the QR code as a string
user_link = "https://www.youtube.com/watch?v=HlMqr92wNp4"
  
#Generate QR code 
qr_code = pyqrcode.create(user_link) 

# Create and save the png file naming "myqr.png"
qr_code.png("myqr.png", scale=6)
