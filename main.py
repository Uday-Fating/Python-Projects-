import qrcode as qr
from PIL import Image

qr=qr.QRCode(version=1,
                    error_correction=qr.ERROR_CORRECT_H,
                    box_size=10,border=2)
qr.add_data("https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/")
qr.make(fit=True)
img=qr.make_image(fill_color="yellow",back_color="black")
img.save("striverwebsiteqr.png") 
