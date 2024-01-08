import qrcode
from PIL import Image

def attach_qr_code(certificate_path, qr_code_data, output_path):
    # Generate the QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(qr_code_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color='black', back_color='white')

    # Load the certificate image
    certificate_img = Image.open(certificate_path)

    # Resize the QR code to fit the desired position on the certificate
    qr_img = qr_img.resize((600, 600))  # Adjust the size as per your requirement

    # Position the QR code on the certificate
    position = (2600, 500)  # Specify the coordinates where you want to place the QR code
    certificate_img.paste(qr_img, position)

    # Save the modified certificate with the attached QR code
    certificate_img.save(output_path)

# List of QR code data and certificate paths
qr_code_data_list = [' Angad kumar / Certificate NO-21cskpr00001 ',
'Biki Kumar Sah / Certificate NO-21cskpr00002',
'Sri Ram S / Certificate NO-21cskpr00003',
'Nitish Kumar Yadav / Certificate NO-21cskpr00004',
'Manjunath S / Certificate NO-21cskpr00005',
'Bharath S / Certificate NO-21cskpr00006',
'Priti kumari / Certificate NO-21cskpr00006']
certificate_path_list = ['generated-certificates/Angad kumar.jpg',
'generated-certificates/Biki Kumar Sah.jpg',
'generated-certificates/Sri Ram S.jpg',
'generated-certificates/Nitish Kumar Yadav.jpg',
'generated-certificates/Manjunath S.jpg',
'generated-certificates/Bharath S.jpg',
'generated-certificates/Priti kumari.jpg']

# Attach QR code to each certificate
for i in range(len(qr_code_data_list)):
    qr_code_data = qr_code_data_list[i]
    certificate_path = certificate_path_list[i]
    output_path = f'output_certificate{i+1}.pdf'
    attach_qr_code(certificate_path, qr_code_data, output_path)
