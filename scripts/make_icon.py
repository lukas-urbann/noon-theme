"""Draws the extension icon (images/icon.png, 256x256): a red sun on a dark rounded square.

Usage: python3 scripts/make_icon.py   (no dependencies)
"""
import os, struct, zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIZE, SS = 256, 4  # output size, supersampling factor
BG, SUN, GLOW = (34, 36, 42), (207, 74, 74), (207, 74, 74)


def coverage(x, y):
    """Returns (r, g, b, a) for a point in 0..1 space."""
    # rounded square
    r = 0.18
    dx, dy = abs(x - 0.5) - (0.5 - r), abs(y - 0.5) - (0.5 - r)
    if max(dx, 0) ** 2 + max(dy, 0) ** 2 > r * r:
        return (0, 0, 0, 0)
    d = ((x - 0.5) ** 2 + (y - 0.5) ** 2) ** 0.5
    if d < 0.26:
        return SUN + (255,)
    if d < 0.36:  # soft halo
        t = (0.36 - d) / 0.10
        a = t * t * 0.35
        return tuple(round(BG[i] + (GLOW[i] - BG[i]) * a) for i in range(3)) + (255,)
    return BG + (255,)


def main():
    rows = []
    n = SIZE * SS
    for py in range(SIZE):
        row = bytearray([0])
        for px in range(SIZE):
            acc = [0, 0, 0, 0]
            for sy in range(SS):
                for sx in range(SS):
                    r, g, b, a = coverage((px * SS + sx + 0.5) / n, (py * SS + sy + 0.5) / n)
                    acc[0] += r * a; acc[1] += g * a; acc[2] += b * a; acc[3] += a
            a = acc[3]
            if a:
                row += bytes([round(acc[0] / a), round(acc[1] / a), round(acc[2] / a), round(a / (SS * SS))])
            else:
                row += bytes(4)
        rows.append(bytes(row))
    raw = b"".join(rows)

    def chunk(tag, data):
        c = struct.pack(">I", len(data)) + tag + data
        return c + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    png = (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", SIZE, SIZE, 8, 6, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))
    out = os.path.join(ROOT, "images", "icon.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "wb") as f:
        f.write(png)
    print("wrote", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
