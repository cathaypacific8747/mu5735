import pandas
from fastkml import kml
from fastkml.geometry import Geometry
from fastkml.styles import LineStyle
from shapely.geometry import Point, LineString

k = kml.KML()
d = kml.Document()
line = []

df = pandas.read_csv('combined.csv')
df_s = [(i.lng, i.lat, i.altitude * 0.3048) for i in df.itertuples()]

for j in range(len(df_s)-1):
    p = kml.Placemark()
    p.geometry = Geometry(geometry=LineString([
        Point(*df_s[j]),
        Point(*df_s[j+1]),
    ]), altitude_mode="absolute")

    d.append(p)

k.append(d)

with open('out.kml', 'w+', encoding='utf-8') as f:
    f.write(k.to_string(prettyprint=True))