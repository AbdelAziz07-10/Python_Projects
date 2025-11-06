# QR Code Generator

A simple Python script that generates QR codes from any URL and saves them in your desired image format.

## Features

- Generate QR codes from any URL
- Customize the output filename and format
- High-quality QR code generation with customizable box size and border
- Black and white color scheme for optimal scanning

## Prerequisites

Before running the script, make sure you have Python installed along with the required library:

```bash
pip install qrcode
```

## Installation

1. Clone this repository or download the script
2. Install the required dependencies:
   ```bash
   pip install qrcode
   ```

## Usage

1. Run the script:
   ```bash
   python qr_code_generator.py
   ```

2. Enter the URL you want to convert to a QR code
3. Enter the desired filename (including the file extension like `.png`, `.jpg`, etc.)
4. The QR code will be generated and saved in the current directory

## Example

```
Enter URL: https://www.linkedin.com/in/abdelaziztantawi/
Enter file name to be saved: Linkedin_Profile_QR.jpg
```

## Output

Here's an example of a generated QR code:

![Generated QR Code](Linkedin_Profile_QR.jpg)

*QR code linking to LinkedIn profile*

### Terminal Output

```
Enter URL: https://www.linkedin.com/in/abdelaziztantawi/
Enter file name to be saved: Linkedin_Profile_QR.jpg
The QR code saved as Linkedin_Profile_QR.jpg
```

## Configuration

You can customize the QR code appearance by modifying these parameters in the script:

- `box_size`: Size of each box in the QR code grid (default: 10)
- `border`: Width of the border in boxes (default: 4)
- `fill_color`: Color of the QR code (default: 'black')
- `back_color`: Background color (default: 'white')

## Supported File Formats

The script supports various image formats including:
- PNG (`.png`)
- JPEG (`.jpg`, `.jpeg`)
- BMP (`.bmp`)
- GIF (`.gif`)

## Contributing

Feel free to fork this project and submit pull requests with improvements!