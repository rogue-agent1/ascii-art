#!/usr/bin/env python3
"""ASCII art text renderer."""

FONT = {c: [
    "###" if c != " " else "   ",
    "# #" if c in "ABDEFGHKMNOPQRUVWXY0234568" else ("  #" if c in "17" else ("###" if c in "CIJLSTZ9" else "   ")),
    "###" if c in "ABEFGHPS2568" else ("# #" if c in "DKMNOQUVWXY034" else ("  #" if c in "179" else ("   " if c == " " else "#  " if c in "CJLT" else "###"))),
    "# #" if c in "ADGHKMNOQUVWXY04689" else ("  #" if c in "179" else ("#  " if c in "BCEJLPS" else ("###" if c in "FT" else "   "))),
    "###" if c in "BCDEGJOQSUZ02356890" else ("# #" if c in "AHKMNVWXY4" else ("  #" if c in "179" else ("#  " if c in "FLP" else "   "))),
] for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "}

def render(text: str, char: str = "#") -> str:
    text = text.upper()
    lines = [""] * 5
    for c in text:
        glyph = FONT.get(c, FONT[" "])
        for i in range(5):
            lines[i] += glyph[i].replace("#", char) + " "
    return "\n".join(lines)

def box(text: str, padding: int = 1) -> str:
    lines = text.split("\n")
    w = max(len(l) for l in lines) + padding * 2
    border = "+" + "-" * (w + 2) + "+"
    result = [border]
    for _ in range(padding):
        result.append("|" + " " * (w + 2) + "|")
    for line in lines:
        result.append("| " + " " * padding + line.ljust(w - padding) + "|")
    for _ in range(padding):
        result.append("|" + " " * (w + 2) + "|")
    result.append(border)
    return "\n".join(result)

if __name__ == "__main__":
    import sys
    text = " ".join(sys.argv[1:]) or "HELLO"
    print(render(text))

def test():
    r = render("AB")
    lines = r.strip().split("\n")
    assert len(lines) == 5
    assert all(len(l) > 0 for l in lines)
    # Box
    b = box("hello")
    assert b.startswith("+")
    assert b.endswith("+")
    assert "hello" in b
    # Custom char
    r2 = render("X", char="*")
    assert "*" in r2
    assert "#" not in r2
    # Space
    r3 = render(" ")
    assert all(c in " \n" for c in r3)
    print("  ascii_art: ALL TESTS PASSED")
