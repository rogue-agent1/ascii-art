#!/usr/bin/env python3
"""ascii_art - Generate ASCII art text banners. Zero deps."""
import sys
FONT = {c: [f"{''.join('█' if (ord(c)*7+r*5+col) % 3 != 0 else ' ' for col in range(5))}" for r in range(7)] for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"}
# Simple block font
BLOCK = {
    'A': ["  █  ","█   █","█   █","█████","█   █","█   █","█   █"],
    'B': ["████ ","█   █","█   █","████ ","█   █","█   █","████ "],
    'C': [" ████","█    ","█    ","█    ","█    ","█    "," ████"],
    'D': ["████ ","█   █","█   █","█   █","█   █","█   █","████ "],
    'E': ["█████","█    ","█    ","████ ","█    ","█    ","█████"],
    'F': ["█████","█    ","█    ","████ ","█    ","█    ","█    "],
    'G': [" ████","█    ","█    ","█  ██","█   █","█   █"," ████"],
    'H': ["█   █","█   █","█   █","█████","█   █","█   █","█   █"],
    'I': ["█████","  █  ","  █  ","  █  ","  █  ","  █  ","█████"],
    'O': [" ███ ","█   █","█   █","█   █","█   █","█   █"," ███ "],
    'R': ["████ ","█   █","█   █","████ ","█ █  ","█  █ ","█   █"],
    ' ': ["     ","     ","     ","     ","     ","     ","     "],
}

def banner(text):
    text = text.upper()
    lines = [""] * 7
    for ch in text:
        glyph = BLOCK.get(ch, BLOCK.get(' '))
        for i in range(7):
            lines[i] += glyph[i] + " "
    return "\n".join(lines)

def box(text):
    w = len(text) + 4
    return f"┌{'─'*w}┐\n│  {text}  │\n└{'─'*w}┘"

def main():
    if len(sys.argv) < 2:
        print("Usage: ascii_art.py <text> [--box]"); sys.exit(1)
    text = " ".join(a for a in sys.argv[1:] if a != "--box")
    if "--box" in sys.argv:
        print(box(text))
    else:
        print(banner(text))

if __name__ == "__main__":
    main()
