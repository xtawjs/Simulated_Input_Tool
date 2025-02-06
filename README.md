# README

[English](./README.md) | [中文](./README.zh_cn.md)

## Simulated_Input_Tool

This Python script provides a simulated input tool that allows users to paste clipboard content character by character into any application. It is particularly useful for scenarios where direct pasting is restricted, such as in secure environments or applications that block standard paste functionality.

The tool runs in the background as a system tray icon and listens for middle mouse button clicks to trigger the simulated paste operation. It supports both ASCII and non-ASCII characters (e.g., Chinese characters) and can be interrupted at any time by clicking the middle mouse button again.

### Features

- **Simulated Paste**: Simulates typing out clipboard content character by character.

- **System Tray Integration**: Runs as a background process with a system tray icon for easy access.

- **Middle Mouse Button Trigger**: Listens for middle mouse button clicks to start or stop the paste operation.

- **Encoding Support**: Handles both ASCII and non-ASCII characters (e.g., Chinese).

- **Restart and Exit Options**: Includes options to restart or exit the application from the system tray menu.

### Usage

1. **Prerequisites**:
   
   - Python 3.x
   
   - Required libraries: `pynput`, `pyperclip`, `Pillow`, `pystray`
   
   - Install dependencies using:
     
     ```bash
     pip install pynput pyperclip Pillow pystray
     ```

2. **Running the Script**:
   
   - Run the script from the command line:
     
     ```bash
     python script.py
     ```
   
   - The script will start and appear as a system tray icon.

3. **Using the Tool**:
   
   - Copy text to your clipboard.
   
   - Click the middle mouse button to start the simulated paste operation.
   
   - Click the middle mouse button again to stop the operation.

4. **System Tray Menu**:
   
   - Right-click the system tray icon to access the menu.
   
   - Options include:
     
     - **Restart**: Restarts the application.
     
     - **Exit**: Stops the application.

### Notes

- The tool is designed to work on Windows, macOS, and Linux.

- Ensure that the clipboard contains text before triggering the paste operation.

- The tool may not work in applications that block simulated input for security reasons.

- For ASCII characters, use `pynput.keyboard.Controller`'s `press()` and `release()` methods to simulate keyboard input.

- For non-ASCII characters (such as Chinese), use the `type()` method in `pynput.keyboard.Controller` to input them directly.

- This tool is only compatible with the US QWERTY keyboard layout.When using, please switch to the English input method.


## Dependencies

This project relies on the following Python libraries:

- `pynput` - For listening to and controlling keyboard and mouse input (MIT License)  
- `pystray` - For system tray icon support (MIT License)  
- `pyperclip` - For clipboard management (BSD License)  
- `Pillow` - For image processing (HPND License)  

Additionally, the project uses the following Python standard libraries:  

- `sys`  
- `os`  
- `time`  
- `base64`  
- `threading`  
- `io`  
