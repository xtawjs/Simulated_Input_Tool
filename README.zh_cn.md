# README

[English](./README.md) | [中文](./README.zh_cn.md)

## Simulated_Input_Tool

这个 Python 脚本提供了一个模拟输入工具，允许用户将剪贴板内容逐字符“敲”入任何应用程序。它在直接粘贴功能受限的场景中特别有用，例如在安全环境或禁止标准粘贴功能的应用程序中。

该工具以后台系统托盘图标的形式运行，并监听鼠标中键点击以触发模拟粘贴操作。它支持 ASCII 和非 ASCII 字符（例如中文字符），并且可以随时通过再次点击鼠标中键来中断操作。

### 功能

- **模拟粘贴**：逐字符模拟输入剪贴板内容。

- **系统托盘集成**：以后台进程运行，带有系统托盘图标，方便访问。

- **鼠标中键触发**：监听鼠标中键点击以启动或停止粘贴操作。

- **编码支持**：支持 ASCII 和非 ASCII 字符（例如中文）。

- **重启和退出选项**：包括从系统托盘菜单重启或退出应用程序的选项。

### 使用方法

1. **前提条件**：
   
   - Python 3.x
   
   - 所需库：`pynput`、`pyperclip`、`Pillow`、`pystray`
   
   - 使用以下命令安装依赖项：
     
     ```bas
     pip install pynput pyperclip Pillow pystray
     ```

2. **运行脚本**：
   
   - 从命令行运行脚本：
     
     ```bash
     python input_tool.py
     ```
   
   - 脚本将启动并显示为系统托盘图标。

3. **使用工具**：
   
   - 将文本复制到剪贴板。
   
   - 点击鼠标中键以启动模拟粘贴操作。
   
   - 再次点击鼠标中键以停止操作。

4. **系统托盘菜单**：
   
   - 右键单击系统托盘图标以访问菜单。
   
   - 选项包括：
     
     - **重启**：重启应用程序。
     
     - **退出**：停止应用程序。

### 注意事项

- 该工具设计用于 Windows、macOS 和 Linux。

- 在触发粘贴操作之前，请确保剪贴板中包含文本。

- 在出于安全原因阻止模拟输入的应用程序中，该工具可能无法正常工作。

- 对 ASCII 字符，使用 pynput.keyboard.Controller 的 press() release() 方法模拟键盘输入。

- 对非 ASCII 字符（如中文），使用 pynput.keyboard.Controller 中 type() 方法方法直接输入。

- 仅可用于美式 QWERTY 键盘布局下。


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
