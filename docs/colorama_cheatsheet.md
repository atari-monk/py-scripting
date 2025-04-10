# Colorama Documentation (Basic Usage)

**Colorama** is a Python library for cross-platform colored terminal text. It works on Windows, Linux, and macOS.

## Installation

```bash
pip install colorama
```

## Basic Usage

```python
from colorama import Fore, Back, Style, init

# Initialize (required for Windows)
init()

# Colored foreground text
print(Fore.RED + "Red text" + Style.RESET_ALL)
print(Fore.GREEN + "Green text" + Style.RESET_ALL)

# Colored background
print(Back.YELLOW + "Yellow background" + Style.RESET_ALL)

# Combined foreground + background
print(Fore.BLUE + Back.WHITE + "Blue on white" + Style.RESET_ALL)

# Bright style
print(Style.BRIGHT + "Bright text" + Style.RESET_ALL)
```

## Available Colors

### Foreground (`Fore`)

- BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

### Background (`Back`)

- Same colors as `Fore`

### Styles (`Style`)

- DIM, NORMAL, BRIGHT, RESET_ALL

## Important Notes

1. Always use `Style.RESET_ALL` to avoid color bleeding.
2. Call `init()` at the start (especially on Windows).
3. Works in most terminals (CMD, PowerShell, bash, etc.).

## Example Function

```python
def color_print(text, color=Fore.WHITE, bg=Back.BLACK, style=Style.NORMAL):
    print(style + color + bg + text + Style.RESET_ALL)

color_print("Warning!", Fore.RED, style=Style.BRIGHT)
```

## Init

To use it in powershell it needs to run this function:

```python
from colorama import init

init()
```
