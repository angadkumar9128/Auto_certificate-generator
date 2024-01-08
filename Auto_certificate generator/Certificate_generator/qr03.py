import qrcode
import base64

# Example image and text data
image_paths = ["certificate-template.jpg", "certificate-template.jpg", "certificate-template.jpg"]
text_data_list = ["Text Data 1", "Text Data 2", "Text Data 3"]

qr_code_data_list = []

# Encode image data as base64 strings and add to the list
for i in range(len(image_paths)):
    with open(image_paths[i], "rb") as image_file:
        image_data = image_file.read()
        encoded_image = base64.b64encode(image_data).decode("utf-8")
        qr_code_data_list.append((encoded_image, text_data_list[i]))

# Example usage
for qr_code_data in qr_code_data_list:
    encoded_image, text_data = qr_code_data

    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(encoded_image)
    qr.make(fit=True)

    # Convert the QR code to an image
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image with the corresponding text data as the filename
    filename = f"qr_code_{text_data}.png"
    qr_image.save(filename)
