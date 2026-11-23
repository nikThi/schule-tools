import sys, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

FONT = TTFont(sys.argv[1])
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
gs = FONT.getGlyphSet()
cmap = FONT.getBestCmap()
UPM = FONT["head"].unitsPerEm

NAVY, AMBER, TEAL, TEAL_D, LIGHT, WHITE = "#17233B", "#F2A93B", "#2F8F83", "#23766C", "#DCE6F2", "#FFFFFF"


def text_runs(runs, size, tracking):
    """runs: [(text, color)]. Returns list of (path_d, color), total width, bbox (in px, baseline y=0)."""
    s = size / UPM
    x = 0.0
    out = []
    bp = BoundsPen(gs)
    for text, color in runs:
        pen = SVGPathPen(gs)
        for ch in text:
            g = cmap[ord(ch)]
            tp = TransformPen(pen, (s, 0, 0, -s, x, 0))
            gs[g].draw(tp)
            tb = TransformPen(bp, (s, 0, 0, -s, x, 0))
            gs[g].draw(tb)
            x += gs[g].width * s + tracking
        out.append((pen.getCommands(), color))
    x -= tracking
    return out, x, bp.bounds  # bounds: xmin,ymin,xmax,ymax


ICONS = {
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "branch": '<path d="M3 12h5c3 0 3-6 6-6h7M8 12h13M8 12c3 0 3 6 6 6h7"/>',
    "book": '<path d="M3 5h6a3 3 0 0 1 3 3v12a2 2 0 0 0-2-2H3z"/><path d="M21 5h-6a3 3 0 0 0-3 3v12a2 2 0 0 1 2-2h7z"/>',
}


def chip(x, y, bg, fg, icon):
    w = 68
    d = (f"M{x+18},{y} h{w-36} a18,18 0 0 1 18,18 v{w-24} a6,6 0 0 1 -6,6 h{-(w-12)} "
         f"a6,6 0 0 1 -6,-6 v{-(w-24)} a18,18 0 0 1 18,-18 z")
    k = 34 / 24
    return (f'<path d="{d}" fill="{bg}"/>'
            f'<g transform="translate({x+17},{y+17}) scale({k:.4f})" fill="none" stroke="{fg}" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</g>')


def logo(text_col, de_col, bar_col, bg=None, name="logo"):
    runs, tw, (bx0, by0, bx1, by1) = text_runs([("schule-tools", text_col), (".de", de_col)], 84, -2.5)
    pad = 24
    W = max(tw, 300) + 2 * pad
    # chip row + bar centred
    row_w = 3 * 68 + 2 * 14
    cx = W / 2
    top = pad
    parts = []
    if bg:
        parts.append(f'<rect width="100%" height="100%" fill="{bg}"/>')
    x0 = cx - row_w / 2
    for i, (b, f, ic) in enumerate([(AMBER, NAVY, "clock"), (TEAL, WHITE, "branch"), (LIGHT, NAVY, "book")]):
        parts.append(chip(x0 + i * 82, top, b, f, ic))
    bar_y = top + 68
    parts.append(f'<rect x="{cx-150}" y="{bar_y}" width="300" height="10" rx="5" fill="{bar_col}"/>')
    text_top = bar_y + 10 + 36
    base = text_top - by1 * -1 if False else text_top + (-by0 if False else 0)
    # place so that the highest glyph point (by1, y-up) sits at text_top
    baseline = text_top - by0
    tx = cx - tw / 2
    for d, col in runs:
        parts.append(f'<path transform="translate({tx:.2f},{baseline:.2f})" d="{d}" fill="{col}"/>')
    H = baseline + by1 + pad
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}" '
           f'role="img" aria-label="schule-tools.de"><title>schule-tools.de</title>' + "".join(parts) + "</svg>\n")
    open(os.path.join(OUT, name + ".svg"), "w").write(svg)


def monogram(size, radius, name, full_bleed=False):
    runs, tw, (bx0, by0, bx1, by1) = text_runs([("s", WHITE), ("t", AMBER)], size * 0.5, -size * 0.015)
    gh = by1 - by0
    tx = (size - (bx1 - bx0)) / 2 - bx0
    baseline = (size + gh) / 2 + by0 * 0 - (-by0) * 0
    baseline = (size - gh) / 2 - by0
    rx = 0 if full_bleed else radius
    parts = [f'<rect width="{size}" height="{size}" rx="{rx}" fill="{NAVY}"/>']
    for d, col in runs:
        parts.append(f'<path transform="translate({tx:.2f},{baseline:.2f})" d="{d}" fill="{col}"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}">'
           + "".join(parts) + "</svg>\n")
    open(os.path.join(OUT, name + ".svg"), "w").write(svg)


logo(WHITE, AMBER, WHITE, name="logo-dark")              # for dark backgrounds (transparent)
logo(NAVY, TEAL_D, NAVY, name="logo-light")               # for light backgrounds (transparent)
monogram(128, 30, "favicon")
monogram(180, 0, "apple-touch-icon", full_bleed=True)
print("ok")
