# QR Code Generator
# Developed for Biox Systems

import qrcode

def generate_qr():
    print("=== QR Code Generator ===")

    # Take URL input from user
    url = input("Enter the URL: ")

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    # Add URL data
    qr.add_data(url)
    qr.make(fit=True)

    # Generate image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code image
    file_name = "generated_qr.png"
    img.save(file_name)

    print(f"QR code generated successfully!")
    print(f"Saved as: {file_name}")

if __name__ == "__main__":
    generate_qr()