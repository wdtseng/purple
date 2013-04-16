#!/usr/bin/python
import glob
import os
import sys
import argparse
import unittest

SVG_DIR = "src/svg/"
SVG_TEMPLATE ="""<!-- GENERATED BY gen_arrows.py; DO NOT EDIT. -->
<svg xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:svg="http://www.w3.org/2000/svg"
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  width="100%"
  height="100%"
  viewBox="0 0 8 8"
  preserveAspectRatio="none"
  >
  <polyline points="{}"
    stroke="#ff3333"
    stroke-width="1"
    vector-effect="non-scaling-stroke"
    fill="none"/>
</svg>
"""

# -----------------
# | 5 | 6 | 7 | 8 |
# -----------------
# | 4 |       | 9 |
# -----      ------
# | 3 |       |10 |
# -----------------
# | 2 | 1 | 0 |11 |
# -----------------
POSITIONS = [(5, 7), (3, 7), (1, 7),
             (1, 5), (1, 3), (1, 1),
             (3, 1), (5, 1), (7, 1),
             (7, 3), (7, 5), (7, 7),
            ]

def write_svg(svg_file, index):
    points = [POSITIONS[(index + offset) % 12] for offset in [0, 4, 8, 0, 6]]
    points_string = " ".join([",".join(map(str, point)) for point in points])
    svg_file.write(SVG_TEMPLATE.format(points_string))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Generate the arrow svg files.
        Must be run from the project root directory.
        """,
    )
    args = parser.parse_args()
    assert os.path.exists(SVG_DIR) and os.path.isdir(SVG_DIR), (
        "%s does not exist" % SVG_DIR)
    for index in xrange(12):
        svg_file = open(SVG_DIR + "arrow" + str(index) + ".svg", "w")
        write_svg(svg_file, index)
        svg_file.close()

