from colorama import init as color_init
from platform import system as platform_system
import sys
import os
### 原项目自带 ###

### Ai 生成 ###


def ansi_support():  # Ai generated
    if platform_system() == "Windows":  # 用 platform.system() 判断系统
        try:
            os.system("")  # 调用 os.system 开启 ANSI 支持
        except Exception:
            print("开启 ANSI 支持失败")


def make_getch():

    def windows_get():
        import msvcrt
        return msvcrt.getch().decode('utf-8')

    def unix_linux_get():
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    if os.name == 'nt':
        return windows_get
    else:
        return unix_linux_get


### ###
def exit_program():
    pass


def init():
    color_init()
    ansi_support()


move_rel = lambda row, col=1: print(f"\033[{row};{col}H", end="", flush=True)
move_abs = lambda n: print(f"\033[{n}H", end="", flush=True)
### relative move ###
up = lambda n: print(f"\033[{n}A", end="", flush=True)
down = lambda n: print(f"\033[{n}B", end="", flush=True)
right = lambda n: print(f"\033[{n}C", end="", flush=True)
left = lambda n: print(f"\033[{n}D", end="", flush=True)
### clear hole screen or line ###
cls = lambda: (print("\033[2J\033[H", end="", flush=True))
cline = lambda: (print("\033[2K", end="", flush=True))


def make_refresh(o_c, o_r):  #origin column and row
    pass


getch = make_getch()
