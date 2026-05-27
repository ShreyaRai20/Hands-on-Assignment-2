# Hands-on-Assignment-2

# QR Code Generator – Biox Systems

## Project Description

This is a simple Python-based QR Code Generator that takes a URL as input and generates a scannable QR code image. The QR code is saved as a PNG file in the project directory.

---

## Requirements

Before running the project, make sure you have:

- Python 3 installed
- pip (Python package manager)
- VS Code or any code editor (optional)

---

## Install Dependencies

This project uses the `qrcode` library and `Pillow`.

### Option 1: Using requirements.txt (Recommended)

Run the following command:

```bash
pip install -r requirements.txt
```

---

### Option 2: Manual installation

If requirements.txt does not work, run:

```bash
pip install qrcode[pil]
```

---

## How to Run the Project

1. Open terminal in the project folder:

```bash
cd "Hands on Assignment 2"
```

2. Run the Python file:

```bash
python3 qr_generator.py
```

---

## How It Works

1. The program asks for a URL input
2. It generates a QR code using the `qrcode` library
3. The QR code is saved as:

```bash
generated_qr.png
```

---

## Example Usage

```bash
Enter the URL: https://www.google.com
QR code generated successfully!
Saved as: generated_qr.png
```

---

## Output File

After running the program, you will find:

- `generated_qr.png` → The generated QR code image

---

## Troubleshooting

### ModuleNotFoundError: No module named 'qrcode'

Fix it by running:

```bash
python3 -m pip install qrcode[pil]
```

---

## Author

Shreya Rai  
University of the Cumberlands  
Master of Science in Information Technology and Management

---

## Note

Make sure all files are in the same folder before running the program.
