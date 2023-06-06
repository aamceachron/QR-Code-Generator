import qrcode

print("QR Code Generator \n")

web_link = qrcode.make(input("Please either type or paste your url here: "))
web_link.save("qrcode.png")

print("\n")  # Just for spacing

print("Your QR Code has been generated successfully! \n")
print(
  "Your QR Code is located in the folder 'qrcode.png', click on 'Show code' to your right to access the folder."
)
