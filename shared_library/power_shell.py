def ps_color_print(text, color="White"):
    print(f"$Host.UI.Write('{color}', '{text}')")