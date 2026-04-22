import qrcode

url = input(f"ENTER YOUR URL: ")
file_path = (f"C:\\python-projects\\qrcode.png")

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print(f"YOUR QR HAS BEEN GENERATED !!")