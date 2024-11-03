import qrcode
import barcode
from barcode.writer import ImageWriter


# def qr_code(request):
    # qr = qrcode.make('https://datanexis-production.up.railway.app/')
    # qr.save("media/qrcodes/" + str(serviceId) + ".png")



# numbers = []
# for i in range(1, 1001, 10):
#     numbers.append(i)
# print(numbers)


# BARCODE
# bc = barcode.get_barcode_class('ean13')     # you can only enter 13 number digits
bc_ = barcode.get_barcode_class('code39')
BC = bc_('00021322', writer=ImageWriter())
bc = BC.save('bcofficial-jb')


# QRCODE
# qr = qrcode.make('https://datanexistech.com/home/')
# qr.save("qrofficial1.png")