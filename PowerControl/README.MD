# PowerControl

A simple Python GUI application for managing system power operations on Windows.

## Description

This application provides a graphical interface with three buttons to perform system operations: shutdown, restart, and logout. It uses Python's tkinter library for the interface and executes Windows system commands.

## Features

- Shutdown: Powers off the computer after 1 second
- Restart: Reboots the computer after 1 second
- Log Out: Logs out the current user session

## Requirements

- Python 3.x
- tkinter (included with Python)
- Windows operating system

## Installation

No installation required. Simply ensure Python is installed on your system.

## Usage

Run the script using Python:

```
python powercontrol.py
```

Click the desired button to perform the operation. The system will execute the command immediately.

## Warning

This application executes real system commands. Clicking any button will perform the actual operation on your computer. Save your work before using this application.

## Technical Details

The application uses Windows shutdown commands:
- `shutdown /s /t 1` - Shutdown with 1 second delay
- `shutdown /r /t 1` - Restart with 1 second delay
- `shutdown -l` - Logout immediately