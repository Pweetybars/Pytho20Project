# install the library needed 
# create a function that collect the text and convert it to qr code
# save QR Code as image 
# run the function 

import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction= qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("thisisQRimg.png")

url = input("Enter your URL : ")
generate_qrcode(url)