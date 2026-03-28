#!/usr/bin/env python3
"""ASCII art — banners, borders, patterns, art text."""
import sys
def banner(text, char="#"):
    w=len(text)+4
    print(char*w); print(f"{char} {text} {char}"); print(char*w)
def bubble(text):
    w=len(text)+2
    print(f" {'_'*w}"); print(f"( {text} )"); print(f" {'‾'*w}")
def cowsay(text):
    w=len(text)+2
    print(f" {'_'*w}"); print(f"< {text} >"); print(f" {'‾'*w}")
    print("        \   ^__^"); print("         \  (oo)\_______")
    print("            (__)\       )\/\"); print("                ||----w |"); print("                ||     ||")
def wave(text):
    import math
    for i,c in enumerate(text):
        offset=int(math.sin(i*0.5)*3)+4
        print(" "*offset+c)
def matrix(w=60,h=15):
    import random
    chars="ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ012345789:.<>"
    for _ in range(h):
        print("".join(random.choice(chars) if random.random()<0.3 else " " for _ in range(w)))
def cli():
    if len(sys.argv)<2: print("Usage: ascii_art banner|bubble|cowsay|wave|matrix <text>"); sys.exit(1)
    cmd=sys.argv[1]; text=" ".join(sys.argv[2:]) or "Hello World"
    {"banner":banner,"bubble":bubble,"cowsay":cowsay,"wave":wave,"matrix":lambda t:matrix()}.get(cmd,banner)(text)
if __name__=="__main__": cli()
