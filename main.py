import qrcode

print("QR Code Generator \n")

web_link = input("Please type or paste your web link here: ")
web_link = web_link.replace(" ", "%20")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(web_link)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
print("\nQR Code Generated Successfully!")