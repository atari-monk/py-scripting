from colorama import init, Back, Fore, Style

init()

def color_print(text, color=Fore.WHITE, bg=Back.BLACK, style=Style.NORMAL):
    print(style + color + bg + text + Style.RESET_ALL)