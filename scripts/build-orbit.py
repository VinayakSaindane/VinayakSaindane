#!/usr/bin/env python3

import argparse
from pathlib import Path

WIDTH = 1200
HEIGHT = 420

# One palette, shared with the snake and README badges
BG = "#0E1311"
SURFACE = "#151B18"
FG = "#E8EDE9"
MUTED = "#8A958F"
LINE = "#28312C"
ACCENT = "#7FD1AE"


def generate_svg():
    return f'''<svg xmlns="http://www.w3.org/2000/svg"
        width="{WIDTH}" height="{HEIGHT}"
        viewBox="0 0 {WIDTH} {HEIGHT}"
        role="img" aria-labelledby="title desc">

  <title id="title">Vinayak Saindane — Engineering</title>
  <desc id="desc">
    Full-stack engineering, AI systems, mobile development,
    interactive 3D and shipped products.
  </desc>

  <defs>
    <linearGradient id="background" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{SURFACE}"/>
      <stop offset="1" stop-color="{BG}"/>
    </linearGradient>

    <radialGradient id="glow" cx="0.18" cy="0.25" r="0.6">
      <stop offset="0" stop-color="{ACCENT}" stop-opacity="0.10"/>
      <stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{ACCENT}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{ACCENT}" stop-opacity="0.9"/>
      <stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/>
    </linearGradient>

    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none"
            stroke="#FFFFFF" stroke-opacity="0.03" stroke-width="1"/>
    </pattern>

    <clipPath id="frame">
      <rect width="{WIDTH}" height="{HEIGHT}" rx="10"/>
    </clipPath>
  </defs>

  <g clip-path="url(#frame)">
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#background)"/>
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#glow)"/>
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#grid)"/>
    <rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{HEIGHT - 1}" rx="10"
          fill="none" stroke="{LINE}"/>

    <!-- eyebrow -->
    <circle cx="56" cy="38" r="4" fill="{ACCENT}">
      <animate attributeName="opacity" values="1;0.35;1" dur="3s" repeatCount="indefinite"/>
    </circle>
    <text x="72" y="42" fill="{MUTED}"
          font-family="monospace" font-size="12"
          letter-spacing="2.5">INDEPENDENT ENGINEERING / 2026</text>

    <!-- name -->
    <text x="48" y="126" fill="{FG}"
          font-family="Arial, Helvetica, sans-serif"
          font-size="65" font-weight="700"
          letter-spacing="-2.5">VINAYAK</text>

    <text x="48" y="194" fill="{FG}"
          font-family="Arial, Helvetica, sans-serif"
          font-size="65" font-weight="700"
          letter-spacing="-2.5">SAINDANE<tspan fill="{ACCENT}">.</tspan></text>

    <rect x="48" y="222" width="44" height="3" rx="1.5" fill="{ACCENT}"/>

    <text x="48" y="259" fill="{FG}"
          font-family="Arial, Helvetica, sans-serif"
          font-size="19">I build the layer between an idea</text>
    <text x="48" y="286" fill="{FG}"
          font-family="Arial, Helvetica, sans-serif"
          font-size="19">and a shipped product.</text>

    <text x="48" y="341" fill="{MUTED}"
          font-family="monospace" font-size="12"
          letter-spacing="1.2">WEB  /  AI  /  MOBILE  /  3D + AR</text>

    <!-- divider -->
    <line x1="710" y1="68" x2="710" y2="350" stroke="{LINE}" stroke-width="1"/>

    <!-- method panel -->
    <text x="752" y="91" fill="{MUTED}"
          font-family="monospace" font-size="11"
          letter-spacing="2">THE WORKING METHOD</text>

    <text x="752" y="145" fill="{ACCENT}" font-family="monospace" font-size="13">01</text>
    <text x="798" y="145" fill="{FG}" font-family="Arial, Helvetica, sans-serif"
          font-size="23" font-weight="600">Understand</text>
    <text x="798" y="168" fill="{MUTED}" font-family="Arial, Helvetica, sans-serif"
          font-size="13">Start with the real problem.</text>

    <line x1="752" y1="192" x2="1128" y2="192" stroke="{LINE}" stroke-width="1"/>

    <text x="752" y="232" fill="{ACCENT}" font-family="monospace" font-size="13">02</text>
    <text x="798" y="232" fill="{FG}" font-family="Arial, Helvetica, sans-serif"
          font-size="23" font-weight="600">Engineer</text>
    <text x="798" y="255" fill="{MUTED}" font-family="Arial, Helvetica, sans-serif"
          font-size="13">Build with intent and precision.</text>

    <line x1="752" y1="279" x2="1128" y2="279" stroke="{LINE}" stroke-width="1"/>

    <text x="752" y="319" fill="{ACCENT}" font-family="monospace" font-size="13">03</text>
    <text x="798" y="319" fill="{FG}" font-family="Arial, Helvetica, sans-serif"
          font-size="23" font-weight="600">Ship</text>
    <text x="798" y="342" fill="{MUTED}" font-family="Arial, Helvetica, sans-serif"
          font-size="13">Deliver. Learn. Improve.</text>

    <!-- footer -->
    <line x1="48" y1="385" x2="1152" y2="385" stroke="{LINE}" stroke-width="1"/>

    <text x="48" y="405" fill="{MUTED}" font-family="monospace" font-size="10"
          letter-spacing="1.2">DESIGN WITH PURPOSE. ENGINEER FOR REALITY.</text>

    <text x="1152" y="405" fill="{ACCENT}" font-family="monospace" font-size="10"
          text-anchor="end">BUILD / SHIP / REPEAT</text>

    <rect x="-160" y="383" width="160" height="2" fill="url(#fade)">
      <animate attributeName="x" values="-160;1200" dur="7s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>
'''


def main():
    parser = argparse.ArgumentParser(description="Generate the GitHub profile banner.")
    parser.add_argument("--output", default="dist/build-orbit.svg", help="Output SVG path.")
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(generate_svg(), encoding="utf-8")
    print(f"Generated banner: {output.resolve()}")


if __name__ == "__main__":
    main()