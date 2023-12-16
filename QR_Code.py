# import qrcode
# qr = qrcode.QRCode(
#     version= 15,
#     box_size = 10,
#     border = 5
# )#We made an object of QRCode class.  object_name = module_name.class_name, 
# # bcz this class is present in the qrcode module, thats why we need to reference it's module whenever we create it's object.
# #or if we import like this, 'from qrcode import all' then we did not need to write reference.
# #Here ( version= it specifies what will be the size of qr code,
# # box_size= choto choto je box gullo thake qr code e seglor size,
# # border= specifies the width of the border )
# data = "https://www.linkedin.com/in/akash-sarkar59/"
# #to add this url or data variable with qr code, we will:
# qr.add_data(data) #add_data is a method to add the data with the qr code, object.add_data(data)
# #now we will generate qr code:
# qr.make(fit = True) #make also a method generate qr code with (fit =True)
# # Now we will create an image or save the qr code as an image:
# img = qr.make_image(fill = 'black', back_color= 'white')
# # make_image is a method to make an image, qr.method means, it will make the image froom the qr object.
# img.save('linkedin_QR.jpg')
# #This is to save the image file as an jpg format in the same location as this code is present!
# # now RUN

#Same program but without any explaination!
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

# Replace 'YOUR_LINKEDIN_PROFILE_URL' with the actual URL of your LinkedIn profile
linkedin_profile_url = 'https://www.linkedin.com/in/akash-sarkar59/'

# Load LinkedIn logo or photo
linkedin_logo_path = r'D:\1. APPS\Works\Akash1\Projects\python_Basic_projects\linkedIn_image2.png'
linkedin_logo = Image.open(linkedin_logo_path)

# Convert the image to RGBA mode if it's a palette image without transparency
linkedin_logo = linkedin_logo.convert("RGBA")

# Create a QR code with the LinkedIn profile URL
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

# Create a new image with RGBA mode and paste the QR code onto it
final_img = Image.new('RGBA', qr_img.size, (255, 255, 255, 255))
final_img.paste(qr_img, (0, 0))

# Set alpha (transparency) channel for the logo
linkedin_logo_with_alpha = Image.new('RGBA', linkedin_logo.size)
linkedin_logo_with_alpha.paste(linkedin_logo, (0, 0), mask=linkedin_logo)
final_img.paste(linkedin_logo_with_alpha, logo_position, linkedin_logo_with_alpha)

# Save or display the final image
final_img.save('linkedin_qr_code.png')
final_img.show()

