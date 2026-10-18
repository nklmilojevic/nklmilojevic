# /// script
# requires-python = ">=3.11"
# dependencies = ["fonttools[woff]>=4.50"]
# ///
"""Render the profile README and its enamel-plate SVGs from live GitHub data."""

import base64
import io
import json
import os
import sys
import urllib.request
from datetime import datetime
from html import escape
from pathlib import Path

from fontTools.subset import Options, Subsetter
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "scripts" / "fonts"
ASSETS = ROOT / "assets"
OWNER = "nklmilojevic"

ENAMEL = "#1b4592"
INK = "#f5f7fa"
THEMES = {
    "light": {"shadow": "#0e2657", "shadow_opacity": 0.28},
    "dark": {"shadow": "#000000", "shadow_opacity": 0.55},
}

PROJECTS = [
    {
        "repo": "sofka",
        "cyrillic": "СОФКА",
        "latin": "Sofka",
        "district": "KUBERNETES TUI · RUST",
        "alt": "Kubernetes TUI in Rust",
        "href": "https://sofka.rs",
    },
    {
        "repo": "thurm",
        "cyrillic": "ТУРМ",
        "latin": "Thurm",
        "district": "TERMINAL FOR MACOS · APPLE SILICON",
        "alt": "native macOS terminal for Apple silicon",
        "href": "https://github.com/nklmilojevic/thurm",
    },
]


def fetch_release(repo):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{OWNER}/{repo}/releases/latest",
        headers={"Accept": "application/vnd.github+json"},
    )
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.load(resp)
    published = datetime.fromisoformat(data["published_at"].replace("Z", "+00:00"))
    return data["tag_name"].removeprefix("v"), published


class Face:
    def __init__(self, name, family):
        self.family = family
        self.path = FONTS / f"{name}.ttf"
        self.font = TTFont(self.path)
        self.cmap = self.font.getBestCmap()
        self.hmtx = self.font["hmtx"]
        self.upm = self.font["head"].unitsPerEm
        self.used = set()

    def width(self, text, size, tracking=0.0):
        self.used.update(text)
        units = sum(self.hmtx[self.cmap[ord(c)]][0] for c in text)
        return units / self.upm * size + tracking * size * max(len(text) - 1, 0)

    def fit(self, text, size, max_width, tracking=0.0):
        while self.width(text, size, tracking) > max_width and size > 8:
            size -= 1
        return size

    def data_uri(self):
        options = Options()
        options.flavor = "woff2"
        options.layout_features = ["kern", "tnum", "locl"]
        subsetter = Subsetter(options)
        subsetter.populate(text="".join(sorted(self.used)))
        font = TTFont(self.path, recalcTimestamp=False)
        subsetter.subset(font)
        buf = io.BytesIO()
        font.flavor = "woff2"
        font.save(buf)
        return "data:font/woff2;base64," + base64.b64encode(buf.getvalue()).decode()


def style(faces, extra=""):
    rules = "".join(
        f"@font-face{{font-family:'{face.family}';src:url({face.data_uri()}) format('woff2');}}"
        for face in faces
    )
    return f"<style>{rules}{extra}</style>"


def plate(x, y, w, h, theme):
    t = THEMES[theme]
    return (
        f'<rect x="{x}" y="{y + 3}" width="{w}" height="{h}" rx="14" fill="{t["shadow"]}" '
        f'opacity="{t["shadow_opacity"]}" filter="url(#soft)"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{ENAMEL}"/>'
        f'<rect x="{x + 11}" y="{y + 11}" width="{w - 22}" height="{h - 22}" rx="7" '
        f'fill="none" stroke="{INK}" stroke-width="4"/>'
    )


def svg(width, height, body, head):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img">'
        f'<defs><filter id="soft" x="-5%" y="-20%" width="110%" height="140%">'
        f'<feGaussianBlur stdDeviation="3"/></filter></defs>'
        f"{head}{body}</svg>\n"
    )


def text(x, y, value, face, size, tracking=0.0, anchor="start", cls=""):
    face.used.update(value)
    attrs = f' class="{cls}"' if cls else ""
    return (
        f'<text x="{x}" y="{y}" font-family="\'{face.family}\'" font-size="{size}" '
        f'letter-spacing="{tracking * size:.2f}" text-anchor="{anchor}" fill="{INK}"{attrs}>'
        f"{escape(value)}</text>"
    )


def name_plate(theme):
    bold, semi = Face("FiraSansCondensed-Bold", "Plate Bold"), Face("FiraSansCondensed-SemiBold", "Plate")
    W, H, pad = 860, 268, 4
    inner = W - 2 * pad - 2 * 44
    cyr = "НИКОЛА МИЛОЈЕВИЋ"
    cyr_size = bold.fit(cyr, 84, inner, 0.01)
    lat_size = semi.fit("Nikola Milojević", 46, inner)
    district = "BEOGRAD · CTO @ MAILERLITE"
    d_size = semi.fit(district, 30, inner, 0.08)
    body = (
        plate(pad, pad, W - 2 * pad, H - 2 * pad - 4, theme)
        + text(48, 108, cyr, bold, cyr_size, 0.01)
        + text(48, 160, "Nikola Milojević", semi, lat_size)
        + f'<rect x="48" y="184" width="{W - 96}" height="3" fill="{INK}"/>'
        + text(48, 230, district, semi, d_size, 0.08)
    )
    return svg(W, H, body, style([bold, semi]))


def project_plate(project, tag, published, theme):
    bold, semi = Face("FiraSansCondensed-Bold", "Plate Bold"), Face("FiraSansCondensed-SemiBold", "Plate")
    W, H, pad, gap = 860, 196, 4, 16
    house_w = 268
    street_w = W - 2 * pad - gap - house_w
    hx = pad + street_w + gap
    tag_size = bold.fit(tag, 62, house_w - 56)
    date = f"{published.day}. {published.month}. {published.year}."
    house_cx = hx + house_w / 2
    date_size = semi.fit(date, 32, house_w - 56, 0.02)
    motion = (
        ".tag{animation:roll 1.1s .3s;}"
        "@keyframes roll{"
        "0%{transform:none;animation-timing-function:cubic-bezier(.7,0,.84,0);}"
        "40%{transform:translateY(-70px);}"
        "40.01%{transform:translateY(70px);animation-timing-function:cubic-bezier(.16,1,.3,1);}"
        "100%{transform:none;}}"
        "@media (prefers-reduced-motion:reduce){.tag{animation:none;}}"
        ".tnum{font-variant-numeric:tabular-nums;}"
    )
    body = (
        plate(pad, pad, street_w, H - 2 * pad - 4, theme)
        + text(38, 98, project["cyrillic"], bold, 74, 0.02)
        + text(40, 146, project["latin"], semi, 40)
        + plate(hx, pad, house_w, H - 2 * pad - 4, theme)
        + f'<clipPath id="win"><rect x="{hx + 18}" y="30" width="{house_w - 36}" height="88"/></clipPath>'
        + f'<g clip-path="url(#win)">'
        + text(house_cx, 94, tag, bold, tag_size, 0.0, "middle", "tag tnum")
        + "</g>"
        + text(house_cx, 142, date, semi, date_size, 0.02, "middle", "tnum")
    )
    return svg(W, H, body, style([bold, semi], motion))


def picture(href, name, alt):
    return (
        f'<a href="{href}"><picture>\n'
        f'  <source media="(prefers-color-scheme: dark)" srcset="assets/{name}-dark.svg">\n'
        f'  <img src="assets/{name}-light.svg" width="100%" alt="{escape(alt)}">\n'
        f"</picture></a>"
    )


def main():
    releases = {p["repo"]: fetch_release(p["repo"]) for p in PROJECTS}
    for theme in THEMES:
        (ASSETS / f"name-{theme}.svg").write_text(name_plate(theme))
        for p in PROJECTS:
            tag, published = releases[p["repo"]]
            (ASSETS / f"{p['repo']}-{theme}.svg").write_text(project_plate(p, tag, published, theme))

    values = {"name": picture("https://nikola.milojevic.me", "name", "Nikola Milojević, Belgrade, CTO at MailerLite")}
    for p in PROJECTS:
        tag, published = releases[p["repo"]]
        alt = f"{p['latin']}, {p['alt']}. Latest release {tag}, {published:%-d %B %Y}."
        values[p["repo"]] = picture(p["href"], p["repo"], alt)

    template = (ROOT / "scripts" / "README.md.tmpl").read_text()
    (ROOT / "README.md").write_text(template.format(**values))
    print(json.dumps({k: v[0] for k, v in releases.items()}), file=sys.stderr)


if __name__ == "__main__":
    main()
