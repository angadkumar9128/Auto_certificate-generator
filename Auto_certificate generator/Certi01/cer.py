from PIL import Image, ImageDraw, ImageFont

# Path to the template certificate image
certificate_template = "certificate_template.png"

# Path to the font files
font_file = "arial.ttf"
signature_font_file = "signature.ttf"

# Text to be added on the certificate
participant_name = "John Doe"
event_name = "Certificate of Attendance"
date = "June 1, 2023"
signature = "Angad Kumar"

# Load the certificate template image
image = Image.open(certificate_template)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define the font sizes and font color
font_size = 48
signature_font_size = 36
font_color = (0, 0, 0)  # Black color

# Load the fonts
font = ImageFont.truetype(font_file, font_size)
signature_font = ImageFont.truetype(signature_font_file, signature_font_size)

# Calculate the position to place the participant's name
text_width, text_height = draw.textsize(participant_name, font=font)
x = (image.width - text_width) / 2
y = 400

# Add the participant's name to the certificate
draw.text((x, y), participant_name, font=font, fill=font_color)

# Calculate the position for the event name
text_width, text_height = draw.textsize(event_name, font=font)
x = (image.width - text_width) / 2
y += text_height + 20

# Add the event name to the certificate
draw.text((x, y), event_name, font=font, fill=font_color)

# Calculate the position for the date
text_width, text_height = draw.textsize(date, font=font)
x = (image.width - text_width) / 2
y += text_height + 20

# Add the date to the certificate
draw.text((x, y), date, font=font, fill=font_color)

# Calculate the position for the signature
text_width, text_height = draw.textsize(signature, font=signature_font)
x = image.width - text_width - 100
y = image.height - text_height - 100

# Add the signature to the certificate
draw.text((x, y), signature, font=signature_font, fill=font_color)

# Save the generated certificate
output_file = "generated_certificate.png"
image.save(output_file)

print(f"Certificate generated and saved as {output_file}")
