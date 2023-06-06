import qrcode

print("General Purpose QR Code Generator \n")

web_link = qrcode.make(input("Please type or paste your web link here: "))
web_link.save("qrcode.png")

print("\n")  #general spacing for visual consisancy

print("QR code generated successfully!")
