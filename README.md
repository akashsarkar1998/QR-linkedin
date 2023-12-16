# QR Code  
Made a QR code which contain my Linkedin profile's link and I made this qr code using linkedin's logo.
---  

Hope you like!
*Cheers* 🥂
###```Here's the code```
```python
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

qr_img = qr.make_image(fill_color="black", back_color="white")

linkedin_logo = linkedin_logo.resize((qr_img.size[0] // 4, qr_img.size[1] // 4), resample=Image.BICUBIC)
logo_position = ((qr_img.size[0] - linkedin_logo.size[0]) // 2, (qr_img.size[1] - linkedin_logo.size[1]) // 2)


final_img = Image.new('RGBA', qr_img.size, (255, 255, 255, 255))
final_img.paste(qr_img, (0, 0))

linkedin_logo_with_alpha = Image.new('RGBA', linkedin_logo.size)
linkedin_logo_with_alpha.paste(linkedin_logo, (0, 0), mask=linkedin_logo)
final_img.paste(linkedin_logo_with_alpha, logo_position, linkedin_logo_with_alpha)


final_img.save('linkedin_qr_code.png')
final_img.show()
```
