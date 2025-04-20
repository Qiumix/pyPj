from colorama import init as color_init
from platform import system as platform_system
from os import system as os_system


def ansi_support():
    if platform_system() == "Windows":  # 用 platform.system() 判断系统
        try:
            os_system("")  # 调用 os.system 开启 ANSI 支持
        except Exception:
            print("开启 ANSI 支持失败")


def init():
    color_init()
    ansi_support()


def lines_from_file(path):
    """Return a list of strings, one for each line in a file."""
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def move_cursor(row, col=1):
    print(f"\033[{row};{col}H", end="", flush=True)


cls = lambda: (print("\033[2J\033[H", end="", flush=True))
cline = lambda: (print("\033[2K", end="", flush=True))


def clear_line(line):
    move_cursor = f"\033[{line};1H"
    clear_code = "\033[2K"
    print(move_cursor + clear_code, end="", flush=True)


init()
cls()
