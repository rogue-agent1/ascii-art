#!/usr/bin/env python3
"""ascii_art - ASCII art text renderer with multiple fonts."""
import sys

FONTS = {
    "banner": {
        "A": ["  #  ","  #  "," # # ","#####","#   #"],
        "B": ["#### ","#   #","#### ","#   #","#### "],
        "C": [" ####","#    ","#    ","#    "," ####"],
        "D": ["#### ","#   #","#   #","#   #","#### "],
        "E": ["#####","#    ","###  ","#    ","#####"],
        "F": ["#####","#    ","###  ","#    ","#    "],
        "G": [" ####","#    ","# ###","#   #"," ### "],
        "H": ["#   #","#   #","#####","#   #","#   #"],
        "I": ["#####","  #  ","  #  ","  #  ","#####"],
        "L": ["#    ","#    ","#    ","#    ","#####"],
        "M": ["#   #","## ##","# # #","#   #","#   #"],
        "N": ["#   #","##  #","# # #","#  ##","#   #"],
        "O": [" ### ","#   #","#   #","#   #"," ### "],
        "P": ["#### ","#   #","#### ","#    ","#    "],
        "R": ["#### ","#   #","#### ","#  # ","#   #"],
        "S": [" ####","#    "," ### ","    #","#### "],
        "T": ["#####","  #  ","  #  ","  #  ","  #  "],
        "U": ["#   #","#   #","#   #","#   #"," ### "],
        "W": ["#   #","#   #","# # #","## ##","#   #"],
        "X": ["#   #"," # # ","  #  "," # # ","#   #"],
        "Y": ["#   #"," # # ","  #  ","  #  ","  #  "],
        "Z": ["#####","   # ","  #  "," #   ","#####"],
        " ": ["     ","     ","     ","     ","     "],
        "!": ["  #  ","  #  ","  #  ","     ","  #  "],
        "0": [" ### ","#  ##","# # #","##  #"," ### "],
        "1": ["  #  "," ##  ","  #  ","  #  ","#####"],
    },
}

def render(text, font="banner", char="#"):
    text = text.upper()
    font_data = FONTS.get(font, FONTS["banner"])
    height = 5
    lines = [""] * height
    for c in text:
        glyph = font_data.get(c, font_data.get(" "))
        if glyph:
            for i in range(height):
                row = glyph[i] if i < len(glyph) else " " * 5
                if char != "#":
                    row = row.replace("#", char)
                lines[i] += row + " "
    return "\n".join(lines)

def box(text, style="single"):
    chars = {"single": "┌─┐│└─┘", "double": "╔═╗║╚═╝", "ascii": "+-+|+-+"}
    c = chars.get(style, chars["single"])
    w = len(text) + 2
    return f"{c[0]}{c[1]*w}{c[2]}\n{c[3]} {text} {c[3]}\n{c[4]}{c[5]*w}{c[6]}"

def table(headers, rows, align="left"):
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(widths):
                widths[i] = max(widths[i], len(str(cell)))
    
    def fmt_row(cells):
        parts = []
        for i, cell in enumerate(cells):
            w = widths[i] if i < len(widths) else len(str(cell))
            s = str(cell)
            if align == "right":
                parts.append(s.rjust(w))
            elif align == "center":
                parts.append(s.center(w))
            else:
                parts.append(s.ljust(w))
        return "│ " + " │ ".join(parts) + " │"
    
    sep = "├─" + "─┼─".join("─" * w for w in widths) + "─┤"
    top = "┌─" + "─┬─".join("─" * w for w in widths) + "─┐"
    bot = "└─" + "─┴─".join("─" * w for w in widths) + "─┘"
    
    lines = [top, fmt_row(headers), sep]
    for row in rows:
        lines.append(fmt_row(row))
    lines.append(bot)
    return "\n".join(lines)

def test():
    # Render
    art = render("HI")
    assert "#" in art
    lines = art.split("\n")
    assert len(lines) == 5
    
    # Box
    b = box("Hello")
    assert "Hello" in b
    assert "┌" in b
    
    # Table
    t = table(["Name", "Age"], [["Alice", "30"], ["Bob", "25"]])
    assert "Alice" in t
    assert "┌" in t
    
    # Custom char
    art2 = render("A", char="*")
    assert "*" in art2
    assert "#" not in art2
    
    print(render("TEST"))
    print(box("All tests passed!"))
    print("All tests passed!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    elif len(sys.argv) > 1:
        print(render(" ".join(sys.argv[1:])))
    else:
        print("Usage: ascii_art.py <text>")
