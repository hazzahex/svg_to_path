from svgpathtools import svg2paths

paths, attributes = svg2paths('svg/hollow_glyph_000.svg')

print(f'Paths: {paths}')
print(f"Attributes: {attributes}")