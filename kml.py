import pandas
from fastkml import kml
from fastkml.geometry import Geometry
from fastkml.styles import Style, LineStyle
from shapely.geometry import Point, LineString
from colour import Color

colours = list(Color("#ff0000").range_to(Color("#00ffff"), 256))

k = kml.KML()
d = kml.Document()

df = pandas.read_csv('combined.csv')
df_s = [(i.lng, i.lat, i.altitude * 0.3048) for i in df.itertuples()]
min_alt, max_alt = min(j[-1] for j in df_s), max(j[-1] for j in df_s)

for j in range(len(df_s)-1):
    this_alt = (df_s[j][-1] + df_s[j+1][-1]) / 2
    this_colour = colours[int((this_alt-min_alt)/(max_alt-min_alt)*255)].hex_l

    p = kml.Placemark(styles=[Style(styles=[LineStyle(
        color=f'ff{this_colour[5:7]}{this_colour[3:5]}{this_colour[1:3]}',
        width=2
    )])])
    p.geometry = Geometry(geometry=LineString([
        Point(*df_s[j]),
        Point(*df_s[j+1]),
    ]), altitude_mode="absolute")

    d.append(p)

k.append(d)

with open('out.kml', 'w+', encoding='utf-8') as f:
    f.write(k.to_string(prettyprint=True))