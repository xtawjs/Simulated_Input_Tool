import sys
import os
import time
import base64
import threading
import pyperclip
from PIL import Image
from io import BytesIO
from pystray import Icon, MenuItem

from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller

# 需要使用 Shift 键来输入的符号
SHIFT_CHARS = {
    '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '_', '+', '{', '}', '|', ':', '"', '<', '>', '?'
}
SHIFT_CHAR_MAPPING = {
    '~': '`', '!': '1', '@': '2', '#': '3', '$': '4', '%': '5',
    '^': '6', '&': '7', '*': '8', '(': '9', ')': '0', '_': '-',
    '+': '=', '{': '[', '}': ']', '|': '\\', ':': ';', '"': "'",
    '<': ',', '>': '.', '?': '/'
}

# 全局的键盘控制器
keyboard_controller = Controller()
# 全局的鼠标监听器（方便在 on_quit() 里停止）
mouse_listener = None

# 用于控制 simulate_paste 的停止
stop_paste_event = threading.Event()
# 用于同步对 paste_thread 的访问
paste_thread_lock = threading.Lock()
paste_thread = None

def simulate_paste():
    """
    模拟粘贴功能，将剪贴板内容逐字符“敲”到当前光标处。
    对 ASCII 字符进行大写/特殊符号判断，中文等非 ASCII 字符则直接使用 type()。
    可以通过 stop_paste_event 来中断执行。
    """
    try:
        clipboard_content = pyperclip.paste().replace('\r\n', '\n')
        for char in clipboard_content:
            if stop_paste_event.is_set():
                print("simulate_paste() 被中断")
                break

            # 判断是否为 ASCII 字符
            if char.isascii():
                # 大写字符
                if char.isupper():
                    with keyboard_controller.pressed(Key.shift):
                        keyboard_controller.press(char.lower())
                        keyboard_controller.release(char.lower())
                # 特殊字符
                elif char in SHIFT_CHARS:
                    # 使用映射的非 Shift 键字符
                    mapped_char = SHIFT_CHAR_MAPPING.get(char, char)
                    with keyboard_controller.pressed(Key.shift):
                        keyboard_controller.press(mapped_char)
                        keyboard_controller.release(mapped_char)
                elif char == '\n':
                    keyboard_controller.press(Key.enter)
                    keyboard_controller.release(Key.enter)

                else:
                    # 普通字符
                    keyboard_controller.press(char)
                    keyboard_controller.release(char)

                # 可以根据需要调整输入间隔
                time.sleep(0.05)
            else:
                # 对非 ASCII 字符（如中文），使用 type() 方法直接输入
                keyboard_controller.type(char)
                time.sleep(0.05)
    except Exception as e:
        print(f"Error handling clipboard content: {e}")
    finally:
        # 清除停止事件
        stop_paste_event.clear()
        # 释放线程锁
        with paste_thread_lock:
            global paste_thread
            paste_thread = None

def on_click(x, y, button, pressed):
    """
    鼠标点击时的回调函数。监听鼠标中键（Button.middle）的一次按下事件。
    如果 simulate_paste() 正在运行，则中断它；否则，启动它。
    """
    if pressed and button == mouse.Button.middle:
        with paste_thread_lock:
            global paste_thread
            if paste_thread is None:
                # 启动 simulate_paste() 线程
                stop_paste_event.clear()
                paste_thread = threading.Thread(target=simulate_paste, daemon=True)
                paste_thread.start()
                print("simulate_paste() 启动")
            else:
                # 中断 simulate_paste()
                stop_paste_event.set()
                print("simulate_paste() 请求中断")

def on_quit(icon: Icon, item):
    """
    停止托盘图标、停止鼠标监听，并结束主线程。
    """
    global mouse_listener, paste_thread
    # 停止鼠标监听
    if mouse_listener is not None:
        mouse_listener.stop()

    # 中断 simulate_paste() 如果正在运行
    with paste_thread_lock:
        if paste_thread is not None:
            stop_paste_event.set()

    # 停止托盘图标
    icon.stop()

    # 等待 paste_thread 结束
    with paste_thread_lock:
        if paste_thread is not None:
            paste_thread.join()

    # 主动结束程序（使主线程退出 while 循环）
    threading.current_thread().do_run = False

def restart_program():
    """
    重启当前程序。
    """
    python = sys.executable
    os.execl(python, python, *sys.argv)

def create_tray_icon():
    """
    创建并运行托盘图标。包含“退出”和“重新启动”菜单项。
    同时启动 pynput 的鼠标监听器，用于捕捉鼠标中键点击。
    """
    icon_data = '''
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    '''
    # 确保 icon_data 不为空，并且是有效的 base64 编码
    if not icon_data.strip():
        raise ValueError("请在 icon_data 中填入有效的 base64 编码图标数据。")

    icon_image = Image.open(BytesIO(base64.b64decode(icon_data)))

    menu = (
        MenuItem('退出', on_quit),
        MenuItem('重新启动', restart_program)
    )
    icon = Icon("name", icon_image, "模拟输入", menu)

    # 启动 pynput 鼠标监听
    global mouse_listener
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

    # 运行托盘图标（阻塞当前函数，直到 icon.stop()）
    icon.run()

def main():
    # 后台线程运行托盘图标
    tray_thread = threading.Thread(target=create_tray_icon, daemon=True)
    tray_thread.start()

    # 主线程等待托盘线程结束
    while tray_thread.is_alive():
        tray_thread.join(1)

if __name__ == '__main__':
    main()