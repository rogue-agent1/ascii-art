import argparse

FONT = {c: [
    " # " if c=="A" else "## " if c=="B" else " ##" if c=="C" else "## " if c=="D" else "###" if c=="E" else "###" if c=="F" else " ##" if c=="G" else "# #" if c=="H" else "###" if c=="I" else "  #" if c=="J" else "# #" if c=="K" else "#  " if c=="L" else "# #" if c=="M" else "# #" if c=="N" else " # " if c=="O" else "## " if c=="P" else " # " if c=="Q" else "## " if c=="R" else " ##" if c=="S" else "###" if c=="T" else "# #" if c=="U" else "# #" if c=="V" else "# #" if c=="W" else "# #" if c=="X" else "# #" if c=="Y" else "###" if c=="Z" else "   ",
    "# #" if c=="A" else "# #" if c=="B" else "#  " if c=="C" else "# #" if c=="D" else "#  " if c=="E" else "#  " if c=="F" else "#  " if c=="G" else "# #" if c=="H" else " # " if c=="I" else "  #" if c=="J" else "## " if c=="K" else "#  " if c=="L" else "###" if c=="M" else "###" if c=="N" else "# #" if c=="O" else "# #" if c=="P" else "# #" if c=="Q" else "# #" if c=="R" else "#  " if c=="S" else " # " if c=="T" else "# #" if c=="U" else "# #" if c=="V" else "# #" if c=="W" else "# #" if c=="X" else "# #" if c=="Y" else "  #" if c=="Z" else "   ",
    "###" if c=="A" else "## " if c=="B" else "#  " if c=="C" else "# #" if c=="D" else "## " if c=="E" else "## " if c=="F" else "# #" if c=="G" else "###" if c=="H" else " # " if c=="I" else "  #" if c=="J" else "#  " if c=="K" else "#  " if c=="L" else "# #" if c=="M" else "# #" if c=="N" else "# #" if c=="O" else "## " if c=="P" else "# #" if c=="Q" else "## " if c=="R" else " # " if c=="S" else " # " if c=="T" else "# #" if c=="U" else "# #" if c=="V" else "###" if c=="W" else " # " if c=="X" else " # " if c=="Y" else " # " if c=="Z" else "   ",
    "# #" if c=="A" else "# #" if c=="B" else "#  " if c=="C" else "# #" if c=="D" else "#  " if c=="E" else "#  " if c=="F" else "# #" if c=="G" else "# #" if c=="H" else " # " if c=="I" else "# #" if c=="J" else "## " if c=="K" else "#  " if c=="L" else "# #" if c=="M" else "# #" if c=="N" else "# #" if c=="O" else "#  " if c=="P" else "## " if c=="Q" else "# #" if c=="R" else "  #" if c=="S" else " # " if c=="T" else "# #" if c=="U" else " # " if c=="V" else "# #" if c=="W" else "# #" if c=="X" else " # " if c=="Y" else "#  " if c=="Z" else "   ",
    "# #" if c=="A" else "## " if c=="B" else " ##" if c=="C" else "## " if c=="D" else "###" if c=="E" else "#  " if c=="F" else " ##" if c=="G" else "# #" if c=="H" else "###" if c=="I" else " # " if c=="J" else "# #" if c=="K" else "###" if c=="L" else "# #" if c=="M" else "# #" if c=="N" else " # " if c=="O" else "#  " if c=="P" else " ##" if c=="Q" else "# #" if c=="R" else "## " if c=="S" else " # " if c=="T" else " # " if c=="U" else " # " if c=="V" else "# #" if c=="W" else "# #" if c=="X" else " # " if c=="Y" else "###" if c=="Z" else "   ",
] for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ "}

def banner(text, char="#"):
    text = text.upper()
    rows = [""] * 5
    for c in text:
        glyph = FONT.get(c, ["   "]*5)
        for i in range(5):
            rows[i] += glyph[i].replace("#", char) + " "
    return "\n".join(rows)

def main():
    p = argparse.ArgumentParser(description="ASCII art text banner")
    p.add_argument("text", nargs="+")
    p.add_argument("-c", "--char", default="#")
    args = p.parse_args()
    print(banner(" ".join(args.text), args.char))

if __name__ == "__main__":
    main()
