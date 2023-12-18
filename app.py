import qrcode

# Taking UPI ID As a input 

upi_id = input("Enter your UPI ID = ")

# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Defining the payment URL based on the UPI ID and the payment app

# You can modify these URLs based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

## Create QR Codes for each payment app

phonepe_QR = qrcode.make(phonepe_url)
paytm_QR = qrcode.make(paytm_url)
google_pay_QR = qrcode.make(google_pay_url)


## Save the QR code to image file (optional)

phonepe_QR.save('phonepe_QR.png')
paytm_QR.save('paytm_QR.png')
google_pay_QR.save('google_pay_QR.png')


## Display the qr codes (you may need to install PIL/Pillow library)

paytm_QR.show()
phonepe_QR.show()
google_pay_QR.show()