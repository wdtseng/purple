#!/usr/bin/python
import glob
import os
import sys
import argparse
import base64

CSS_DIR = "src/css/"
SVG_TEMPLATE = """<svg xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:svg="http://www.w3.org/2000/svg"
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  width="100%"
  height="100%"
  viewBox="0 0 8 8"
  preserveAspectRatio="none"
  >
  <polyline points="{points}"
    stroke="#ff3333"
    stroke-width="1"
    vector-effect="non-scaling-stroke"
    fill="none"/>
</svg>
"""

CSS_TEMPLATE = """.arrow{index} {{
  background-image: url(data:image/svg+xml;base64,{base64_svg});
}}
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

def get_svg_arrow(index):
    """Return an image of "the arrow" anchored at grid index, in svg/xml format."""
    points = [POSITIONS[(index + offset) % 12] for offset in [0, 4, 8, 0, 6]]
    points_string = " ".join([",".join(map(str, point)) for point in points])
    return SVG_TEMPLATE.format(points=points_string)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Generate the arrow svg files.
        Must be run from the project root directory.
        """,
    )
    args = parser.parse_args()
    assert os.path.exists(CSS_DIR) and os.path.isdir(CSS_DIR), (
        "CSS directory %s does not exist" % CSS_DIR)
    css_file = open(CSS_DIR + "arrows.css", "w")
    for index in xrange(12):
        svg_arrow = get_svg_arrow(index)
        css_rule = CSS_TEMPLATE.format(
            index=index,
            base64_svg=base64.b64encode(svg_arrow.encode('utf8')))
        css_file.write(css_rule)
    css_file.close()
