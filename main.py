from tileset_object import TileSet
from atlas_object import Atlas
from sys import getsizeof

atlas1 = Atlas()
NatureTileSet = TileSet()
NatureTileSet.append("tree", "$")
NatureTileSet.append("water", "~")

CityTileSet = TileSet()
CityTileSet.append("road", "*")

atlas1.append("Nature", NatureTileSet)
atlas1.append("City", CityTileSet)
atlas1.append("SomeOne", 1)

atlas1.display()
