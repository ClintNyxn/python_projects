import qrcode

msg = "I LOVE YOU <3"

qr = qrcode.QRCode(version=2, box_size=50, border=2)
qr.add_data(msg)
qr.make(fit=True)
img = qr.make_image()
img.save('/home/nyxn/qrcode1.png')
print('done!')
