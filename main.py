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

mainMap.save("mapa_base.html")


