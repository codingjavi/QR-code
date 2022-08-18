import qrcode

#could put a link here
img = qrcode.make("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwix2Kmg8ND5AhXWBzQIHUH7D7wQPAgI")

#it imediatly saves it to the folder this code is in
img.save("google.jpg")


#to read what's in the QR code

#import cv2 to get the class QRCodeDetector() which has the method: detectAndDecode()
import cv2

#d is the class now
d = cv2.QRCodeDetector()

#detectAndDecode returns 3 outputs
#val is the literal string in the qr code
#imread reads the image in opencv
val, points, straight = d.detectAndDecode(cv2.imread("google.jpg"))
print (val)