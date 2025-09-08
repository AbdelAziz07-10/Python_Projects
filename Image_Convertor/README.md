# PNG to JPG Converter
A simple desktop application built with Python that converts PNG images to JPG format with a user-friendly graphical interface.
Features

---

- Easy file selection through browse dialog
- Automatic PNG to JPG conversion
- Success/error message feedback
- Clean and intuitive GUI
- Custom save location selection
- Handles PNG images with transparency (RGBA)

Screenshots
Show Image
Main application window

## Requirements
- Python 3.x
- Pillow (PIL)

## Installation

### Clone this repository:

git clone https://github.com/AbdelAziz07-10/Python_Projects.git

cd Python_Projects/Image_Converter

### Install required packages:

pip install Pillow

### Run the application:

python image_converter.py

---

## How to Use:
- Select PNG File: Click "Select PNG file" to browse and choose your PNG image
- Convert: Click "Convert PNG to JPG" to choose where to save the converted file
Done: The app will show a success message when conversion is complete

---

## Technical Details:
- Built with tkinter for the GUI
- Uses PIL (Pillow) for image processing
- Automatically converts RGBA images to RGB format for JPEG compatibility
- Error handling for missing file selection and save cancellation
