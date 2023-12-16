# import qrcode
# qr = qrcode.QRCode(
#     version= 15,
#     box_size = 10,
#     border = 5
# )
# data = "https://www.linkedin.com/in/akash-sarkar59/"
# qr.add_data(data)
# qr.make(fit = True)
# img = qr.make_image(fill = 'black', back_color= 'white')
# img.save('linkedin_QR.jpg')


#########  New style:
import qrcode
from PIL import Image

linkedin_profile_url = 'https://www.linkedin.com/in/akash-sarkar59/'

linkedin_logo_path = r'D:\1. APPS\Works\Akash1\Projects\python_Basic_projects\linkedIn_image2.png'
linkedin_logo = Image.open(linkedin_logo_path)

linkedin_logo = linkedin_logo.convert("RGBA")

qr = qrcode.QRCode(
    version=8,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
qr.add_data(linkedin_profile_url)
qr.make(fit=True)

# Generate the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white")

# Resize the logo to fit within the QR code
linkedin_logo = linkedin_logo.resize((qr_img.size[0] // 4, qr_img.size[1] // 4), resample=Image.BICUBIC)
# Calculate the position for pasting the logo at the center of the QR code
logo_position = ((qr_img.size[0] - linkedin_logo.size[0]) // 2, (qr_img.size[1] - linkedin_logo.size[1]) // 2)

final_img = Image.new('RGBA', qr_img.size, (255, 255, 255, 255))
final_img.paste(qr_img, (0, 0))

linkedin_logo_with_alpha = Image.new('RGBA', linkedin_logo.size)
linkedin_logo_with_alpha.paste(linkedin_logo, (0, 0), mask=linkedin_logo)
final_img.paste(linkedin_logo_with_alpha, logo_position, linkedin_logo_with_alpha)

# Save or display the final image
final_img.save('linkedin_qr_code.png')
final_img.show()

