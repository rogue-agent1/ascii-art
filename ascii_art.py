#!/usr/bin/env python3
"""ascii_art - Convert images (PPM) to ASCII art."""
import argparse, sys

CHARS = " .:-=+*#%@"

def read_ppm(path):
    with open(path, 'rb') as f:
        magic = f.readline().strip()
        line = f.readline().strip()
        while line.startswith(b'#'): line = f.readline().strip()
        w, h = map(int, line.split())
        maxval = int(f.readline().strip())
        data = f.read()
    return w, h, data

def to_ascii(w, h, data, out_width=80):
    scale = w / out_width
    out_height = int(h / scale / 2)
    lines = []
    for y in range(out_height):
        line = ""
        for x in range(out_width):
            px, py = int(x * scale), int(y * scale * 2)
            if py >= h or px >= w: line += " "; continue
            i = (py * w + px) * 3
            if i + 2 < len(data):
                brightness = (data[i] * 299 + data[i+1] * 587 + data[i+2] * 114) / 1000
                idx = int(brightness / 256 * len(CHARS))
                line += CHARS[min(idx, len(CHARS) - 1)]
            else:
                line += " "
        lines.append(line.rstrip())
    return "\n".join(lines)

def main():
    p = argparse.ArgumentParser(description="Image to ASCII art")
    p.add_argument("input", help="PPM image")
    p.add_argument("-w", "--width", type=int, default=80)
    p.add_argument("-i", "--invert", action="store_true")
    p.add_argument("-o", "--output")
    args = p.parse_args()
    w, h, data = read_ppm(args.input)
    if args.invert:
        global CHARS; CHARS = CHARS[::-1]
    art = to_ascii(w, h, data, args.width)
    if args.output: open(args.output, 'w').write(art); print(f"Saved to {args.output}")
    else: print(art)

if __name__ == "__main__":
    main()
