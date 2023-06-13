import folium as fl
from folium.plugins import MiniMap
from folium.plugins import FloatImage
##Modulos propios
from APIConsumo.getEstacions import getEstacion
from APIConsumo.getLines import getLinea
from Traza.LineasPrincipales import TrazaLineas

### LAtitud longitud
## MArcadores

mainMap = fl.Map(location =[19.434430271379885, -99.13309144564224], zoom_start=12)
#fl.Circle(location=[19.434430271379885, -99.13309144564224],
#          color = "orange", fill_color = "purple", weight = 4, radius=50, fill_opacity = 0.4).add_to(mainMap)

#Linea 1
c = getEstacion(lineaId=1)
tl = TrazaLineas()
tl.trazaEstaciones(data=c, folio =fl, mapa = mainMap, color='pink', iconName='train')
tl.trazaLinea(folio=fl, color='pink', mapa=mainMap)
#Linea 2
c = getEstacion(lineaId=2)
tl.trazaEstaciones(data=c, folio =fl, mapa = mainMap, color='darkblue', iconName='train', new="yes")
tl.trazaLinea(folio=fl, color='darkblue', mapa=mainMap, new="yes")
#Linea 3
c = getEstacion(lineaId=3)
tl.trazaEstaciones(data=c, folio =fl, mapa = mainMap, color='darkgreen', iconName='train', new="yes")
tl.trazaLinea(folio=fl, color='darkgreen', mapa=mainMap, new="yes")
#Linea 4
c = getEstacion(lineaId=4)
tl.trazaEstaciones(data=c, folio =fl, mapa = mainMap, color='lightblue', iconName='train', new="yes")
tl.trazaLinea(folio=fl, color='lightblue', mapa=mainMap, new="yes")
#Linea 5
c = getEstacion(lineaId=5)
tl.trazaEstaciones(data=c, folio =fl, mapa = mainMap, color='gray', iconName='train', new="yes")
tl.trazaLinea(folio=fl, color='yellow', mapa=mainMap, new="yes")
#Linea 6
c = getEstacion(lineaId=6)
tl.trazaEstaciones(data=c, folio =fl, mapa = mainMap, color='red', iconName='train', new="yes")
tl.trazaLinea(folio=fl, color='red', mapa=mainMap, new="yes")
#Linea 7 (Corregir orden de los datos)
c = getEstacion(lineaId=7)
tl.trazaEstaciones(data=c, folio =fl, mapa = mainMap, color='orange', iconName='train', new="yes")
tl.trazaLinea(folio=fl, color='orange', mapa=mainMap, new="yes")
# Linea 8
c = getEstacion(lineaId=8)
tl.trazaEstaciones(data=c, folio =fl, mapa = mainMap, color='green', iconName='train', new="yes")
tl.trazaLinea(folio=fl, color='green', mapa=mainMap, new="yes")
# Linea 9
c = getEstacion(lineaId=9)
tl.trazaEstaciones(data=c, folio =fl, mapa = mainMap, color='#3F2212', iconName='train', new="yes")
tl.trazaLinea(folio=fl, color='#3F2212', mapa=mainMap, new="yes")

# Linea 10
c = getEstacion(lineaId=10)
tl.trazaEstaciones(data=c, folio =fl, mapa = mainMap, color='purple', iconName='train', new="yes")
tl.trazaLinea(folio=fl, color='purple', mapa=mainMap, new="yes")

# Linea 11
c = getEstacion(lineaId=11)
tl.trazaEstaciones(data=c, folio =fl, mapa = mainMap, color='darkgreen', iconName='train', new="yes")
tl.trazaLinea(folio=fl, color='darkgreen', mapa=mainMap, new="yes")

# Linea 12
c = getEstacion(lineaId=12)
tl.trazaEstaciones(data=c, folio =fl, mapa = mainMap, color='gold', iconName='train', new="yes")
tl.trazaLinea(folio=fl, color='gold', mapa=mainMap, new="yes")

###Linea 71
"""
place_lat = [19.2848434,19.28377762,19.2824815,19.28269024,19.28386287,19.28551719,19.28909804,19.29157937,19.2947326,19.29670861,19.29863753,19.30103758,19.30171161,19.3021048,19.30251047,19.30302652,19.30338573,19.30317461,19.30315993,19.30268413,19.30183038,19.30276546,19.30424767,19.30484569,19.3058182,19.3060761,19.30717705,19.30756965,19.31299057,19.31575293,19.31865535,19.32092595,19.32264393,19.32406231,19.32634054,19.32861069,19.33067079,19.33429706,19.33615225]
place_lng = [-99.12632019,-99.1306431,-99.13562659,-99.14130952,-99.14444784,-99.14715343,-99.15040235,-99.15225573,-99.15463807,-99.15629506,-99.15768599,-99.16059582,-99.16318963,-99.16556443,-99.16885499,-99.17280623,-99.17703293,-99.18140653,-99.18585975,-99.19030013,-99.19485957,-99.19809339,-99.19975578,-99.20261565,-99.20475732,-99.20867639,-99.21254606,-99.21583091,-99.21991935,-99.22116102,-99.22167384,-99.22032864,-99.21880695,-99.21566038,-99.21355064,-99.21204835,-99.21096592,-99.20899431,-99.20654837]

points = []
for i in range(len(place_lat)):
    points.append([place_lat[i], place_lng[i]])
print(points)
fl.PolyLine(points, color='black', weigth=7).add_to(mainMap)
"""
mainMap.save("mapa_base.html")


