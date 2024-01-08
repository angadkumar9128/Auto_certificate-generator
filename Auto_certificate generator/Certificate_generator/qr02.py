import qrcode
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_qr_code_with_image_and_text(image_path, text_data, output_path):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add text data to the QR code
    qr.add_data(text_data)
    qr.make(fit=True)

    # Convert the QR code to an image
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Open the image to be embedded
    image = Image.open(image_path)

    # Resize the image to fit within the QR code
    qr_size = qr_image.size[0]
    image = image.resize((qr_size, qr_size))

    # Calculate the position to paste the image within the QR code
    offset = (int((qr_image.size[0] - image.size[0]) / 2), int((qr_image.size[1] - image.size[1]) / 2))

    # Paste the image onto the QR code
    qr_image.paste(image, offset)

    # Save the final QR code image
    qr_image.save(output_path)


def generate_certificate_with_qr_code(qr_code_path, certificate_path, text_data):
    # Create a new PDF document
    c = canvas.Canvas(certificate_path, pagesize=letter)

    # Load the QR code image
    qr_code_image = Image.open(qr_code_path)

    # Set the position to place the QR code on the certificate
    qr_code_pos_x = 100
    qr_code_pos_y = 300

    # Draw the QR code on the certificate
    c.drawImage(qr_code_image, qr_code_pos_x, qr_code_pos_y)

    # Set the position to place the text on the certificate
    text_pos_x = 100
    text_pos_y = 100

    # Draw the text on the certificate
    c.setFont("Helvetica", 12)
    c.drawString(text_pos_x, text_pos_y, text_data)

    # Save the certificate
    c.save()


# Example usage
image_path =   ['generated-certificates/Angad kumar.jpg',
'generated-certificates/Biki Kumar Sah.jpg',
'generated-certificates/Sri Ram S.jpg',
'generated-certificates/Nitish Kumar Yadav.jpg',
'generated-certificates/Manjunath S.jpg',
'generated-certificates/Bharath S.jpg',
'generated-certificates/Priti kumari.jpg'] # Path to the image file
qr_code_paths = ["qr_code1.png", "qr_code2.png", "qr_code3.png"]  # List of output paths for the generated QR codes
text_data_list = ["QR Code 1", "QR Code 2", "QR Code 3"]  # List of text data for each QR code
certificate_paths = ["certificate1.pdf", "certificate2.pdf", "certificate3.pdf"]  # List of output paths for the generated certificates

image = Image.open(image_path)

for i in range(len(qr_code_paths)):
    image_path =  image_path [i]
    qr_code_path = qr_code_paths[i]
    text_data = text_data_list[i]
    certificate_path = certificate_paths[i]

    generate_qr_code_with_image_and_text(image, text_data, qr_code_path)
    generate_certificate_with_qr_code(qr_code_path, certificate_path, text_data)
