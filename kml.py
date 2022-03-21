import pandas
from fastkml import kml
from fastkml.geometry import Geometry
from shapely.geometry import Point, LineString

k = kml.KML()
d = kml.Document()
line = []

df = pandas.read_csv('combined.csv')
for i in df.itertuples():
    line.append(Point(i.lng, i.lat, i.altitude * 0.3048))

p = kml.Placemark()
p.geometry = Geometry(geometry=LineString(line), altitude_mode="absolute")

d.append(p)
k.append(d)

with open('out.kml', 'w+', encoding='utf-8') as f:
    f.write(k.to_string(prettyprint=True))