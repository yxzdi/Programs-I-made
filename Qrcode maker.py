#importing library
import qrcode

#getting user's data
user_data = str(input("enter link of the picture or website you want to make a QRcode of: "))

#assigning the qrcode that will be made to a variable
img = qrcode.make(user_data)

#assigning the file type of the qrcode made
type(img) #qrcode.image.pil.PilImage

#asking the user what the name of the file should be
file_name = str(input("Enter the name you want to save the qrcode file as: "))

#assigning the name of the qrcode file
img.save(file_name + ".png")

