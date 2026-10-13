#!/usr/bin/env python3

"""Generate an editorial engineering banner for Vinayak Saindane."""

import argparse
from html import escape
from pathlib import Path

WIDTH = 1200
HEIGHT = 420

BG = "#101210"
FG = "#F0F0E9"
MUTED = "#969B91"
ACCENT = "#C7FF62"
RULE = "#343831"


def generate_svg():
    parts = [
        f'''<svg xmlns="http://www.w3.org/2000/svg"
  width="{WIDTH}" height="{HEIGHT}"
  viewBox="0 0 {WIDTH} {HEIGHT}"
  role="img" aria-labelledby="title desc">

<title id="title">Vinayak Saindane — Engineering Field Note</title>
<desc id="desc">
An editorial engineering identity banner featuring typography,
a build sequence, and a subtle animated signal.
</desc>

<defs>
  <linearGradient id="background" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{BG}"/>
    <stop offset="100%" stop-color="#171A15"/>
  </linearGradient>

  <linearGradient id="signal" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{ACCENT}" stop-opacity="0"/>
    <stop offset="50%" stop-color="{ACCENT}"/>
    <stop offset="100%" stop-color="{ACCENT}" stop-opacity="0"/>
  </linearGradient>

  <clipPath id="frame">
    <rect width="1200" height="420" rx="12"/>
  </clipPath>
</defs>

<g clip-path="url(#frame)">
  <rect width="1200" height="420" fill="url(#background)"/>

  <!-- Editorial frame -->
  <path d="M40 34 H1160" stroke="{RULE}" stroke-width="1"/>
  <path d="M40 386 H1160" stroke="{RULE}" stroke-width="1"/>
  <path d="M810 62 V358" stroke="{RULE}" stroke-width="1"/>

  <!-- Small, quiet identity label -->
  <g font-family="SFMono-Regular, Consolas, monospace">
    <text x="42" y="23" fill="{MUTED}" font-size="10"
      letter-spacing="1.8">INDEPENDENT ENGINEERING / PROFILE 001</text>

    <text x="1158" y="23" fill="{MUTED}" font-size="10"
      text-anchor="end">MUMBAI, IN</text>
  </g>

  <!-- Large typographic identity -->
  <g font-family="Inter, Helvetica Neue, Arial, sans-serif">
    <text x="42" y="116" fill="{FG}" font-size="74"
      font-weight="750" letter-spacing="-4">VINAYAK</text>

    <text x="42" y="190" fill="{FG}" font-size="74"
      font-weight="750" letter-spacing="-4">SAINDANE</text>

    <rect x="43" y="211" width="54" height="4" fill="{ACCENT}"/>

    <text x="42" y="250" fill="{FG}" font-size="19"
      font-weight="500" letter-spacing="-0.2">
      I build the layer between
    </text>

    <text x="42" y="276" fill="{FG}" font-size="19"
      font-weight="500" letter-spacing="-0.2">
      an idea and a shipped product.
    </text>

    <text x="42" y="316" fill="{MUTED}" font-size="12">
      FULL-STACK  /  AI SYSTEMS  /  MOBILE  /  3D + AR  /  RUST
    </text>
  </g>

  <!-- Engineering sequence: a deliberate editorial index -->
  <g font-family="SFMono-Regular, Consolas, monospace">
    <text x="846" y="78" fill="{MUTED}" font-size="10"
      letter-spacing="1.8">THE WORKING METHOD</text>

    <path d="M854 111 V300" stroke="{RULE}" stroke-width="1.5"/>

    <circle cx="854" cy="126" r="4" fill="{ACCENT}"/>
    <circle cx="854" cy="208" r="3" fill="{MUTED}"/>
    <circle cx="854" cy="290" r="3" fill="{MUTED}"/>

    <text x="876" y="121" fill="{ACCENT}" font-size="10">
      01 / UNDERSTAND
    </text>
    <text x="876" y="143" fill="{FG}" font-size="16"
      font-family="Inter, Helvetica Neue, Arial, sans-serif">
      Find the real problem.
    </text>

    <text x="876" y="203" fill="{MUTED}" font-size="10">
      02 / ENGINEER
    </text>
    <text x="876" y="225" fill="{FG}" font-size="16"
      font-family="Inter, Helvetica Neue, Arial, sans-serif">
      Build the right system.
    </text>

    <text x="876" y="285" fill="{MUTED}" font-size="10">
      03 / SHIP
    </text>
    <text x="876" y="307" fill="{FG}" font-size="16"
      font-family="Inter, Helvetica Neue, Arial, sans-serif">
      Make it work in reality.
    </text>
  </g>

  <!-- Animated signal: one intentional motion, not decoration everywhere -->
  <path d="M42 352 H1158"
    stroke="{RULE}" stroke-width="1"/>

  <path d="M42 352 H1158"
    stroke="url(#signal)" stroke-width="2"
    stroke-dasharray="100 1016">
    <animate attributeName="stroke-dashoffset"
      from="1116" to="-1116"
      dur="7s" repeatCount="indefinite"/>
  </path>

  <g font-family="SFMono-Regular, Consolas, monospace">
    <text x="42" y="376" fill="{MUTED}" font-size="10">
      BUILD WITH INTENT.
    </text>
    <text x="600" y="376" fill="{MUTED}" font-size="10"
      text-anchor="middle">SHIP WITH CARE.</text>
    <text x="1158" y="376" fill="{ACCENT}" font-size="10"
      text-anchor="end">ITERATE / REPEAT</text>
  </g>
</g>
</svg>'''
    ]

    return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(
        description="Generate the Engineering Field Note SVG."
    )
    parser.add_argument(
        "--output",
        default="dist/build-orbit.svg",
        help="Output path for the SVG banner.",
    )
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(generate_svg(), encoding="utf-8")

    print(f"Generated: {output}")


if __name__ == "__main__":
    main()