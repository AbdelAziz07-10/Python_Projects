import qrcode

data = input('Enter URL: ').strip()
file_name = input('Enter file name to be saved: ').strip()

qr = qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)

image = qr.make_image(fill_color = 'black',back_color = 'white')

image.save(file_name)

print(f'The QR code saved as {file_name}')