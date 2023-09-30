import folium as fl
from folium import plugins, FeatureGroup, LayerControl
from folium.plugins import GroupedLayerControl
##Modulos propios
from APIConsumo.getEstacions import getEstacion
from APIConsumo.getLines import getLinea
from Traza.LineasPrincipales import TrazaLineas

### LAtitud longitud
## MArcadores

mainMap = fl.Map(location =[19.434430271379885, -99.13309144564224], zoom_start=11.4)
##### Lineas principales
l1 = fl.FeatureGroup(name='Linea 1 (Observatorio Pantitlán)')
l2 = fl.FeatureGroup(name='Linea 2 (Cuatro Caminos – Tasqueña)')
l3 = fl.FeatureGroup(name='Línea 3: Verde Olivo (Indios Verdes – Universidad)')
l4 = fl.FeatureGroup(name='Línea 4: Cian (Martín Carrera – Santa Anita)')
l5 = fl.FeatureGroup(name='Línea 5: Amarillo (Politécnico – Pantitlán)')
l6 = fl.FeatureGroup(name='Línea 6: Rojo (El Rosario – Martín Carrera)')
l7 = fl.FeatureGroup(name='Línea 7: Naranja (El Rosario – Barranca del Muerto)')
l8 = fl.FeatureGroup(name='Línea 8: Verde (Garibaldi/Lagunilla – Constitución de 1917)')
l9 = fl.FeatureGroup(name='Línea 9: Café (Tacubaya – Pantitlán)')
lA = fl.FeatureGroup(name='Línea A: Morado (Pantitlán – La Paz)')
lB = fl.FeatureGroup(name='Línea B: Verde y gris (Ciudad Azteca – Buenavista)')
l12 = fl.FeatureGroup(name='Línea 12: Dorada (Mixcoac – Tláhuac)')
l81 = fl.FeatureGroup(name='Línea 81: Verde (Tasqueña - Milpa Alta)')
##### Lineas Anillares Interiores
l71 = fl.FeatureGroup(name='Linea 71 Anillar Sur')
l72 = fl.FeatureGroup(name='Linea 72 Anillar Poniente')
l73 = fl.FeatureGroup(name='Linea 73 Anillar Norte')
l74 = fl.FeatureGroup(name='Linea 74 Anillar Oriente')
##### Lineas Anillares Exteriores
l75 = fl.FeatureGroup(name='Linea 75 Anillar Exterior')

tl = TrazaLineas()
tl.foliums = fl

def principales(lineas =[1,2,3,4,5,6,7,8,9,10,11,12, 81]):
    if 1 in lineas:
        #Linea 1
        c = getEstacion(lineaId=1)
        tl.nom_grup=l1
        tl.trazaEstaciones(data=c, mapa = mainMap, color='pink', iconName='train', tipo=1)
        tl.trazaLinea(color='pink', mapa=mainMap, new="yes",tipo=1)
    if 2 in lineas:
        #Linea 2
        c = getEstacion(lineaId=2)
        tl.nom_grup=l2
        tl.trazaEstaciones(data=c, mapa = mainMap, color='darkblue', iconName='train', new="yes", tipo=1)
        tl.trazaLinea(color='darkblue', mapa=mainMap, new="yes", tipo=1)
    if 3 in lineas:
        #Linea 3
        c = getEstacion(lineaId=3)
        tl.nom_grup=l3
        tl.trazaEstaciones(data=c, mapa = mainMap, color='darkgreen', iconName='train', new="yes", tipo=1)
        tl.trazaLinea(color='darkgreen', mapa=mainMap, new="yes", tipo=1)
    if 4 in lineas:
        #Linea 4
        c = getEstacion(lineaId=4)
        tl.nom_grup=l4
        tl.trazaEstaciones(data=c, mapa = mainMap, color='lightblue', iconName='train', new="yes", tipo=1)
        tl.trazaLinea(color='lightblue', mapa=mainMap, new="yes", tipo=1)
    if 5 in lineas:
        #Linea 5
        tl.nom_grup=l5
        c = getEstacion(lineaId=5)
        tl.trazaEstaciones(data=c, mapa = mainMap, color='gray', iconName='train', new="yes", tipo=1)
        tl.trazaLinea(color='yellow', mapa=mainMap, new="yes", tipo=1)
    if 6 in lineas:
        #Linea 6
        tl.nom_grup=l6
        c = getEstacion(lineaId=6)
        tl.trazaEstaciones(data=c, mapa = mainMap, color='red', iconName='train', new="yes", tipo=1)
        tl.trazaLinea(color='red', mapa=mainMap, new="yes", tipo=1)
    if 7 in lineas:
        #Linea 7 (Corregir orden de los datos)
        c = getEstacion(lineaId=7)
        tl.nom_grup=l7
        tl.trazaEstaciones(data=c, mapa = mainMap, color='orange', iconName='train', new="yes", tipo=1)
        tl.trazaLinea(color='orange', mapa=mainMap, new="yes", tipo=1)
    if 8 in lineas:
        # Linea 8
        c = getEstacion(lineaId=8)
        tl.nom_grup=l8
        tl.trazaEstaciones(data=c, mapa = mainMap, color='green', iconName='train', new="yes", tipo=1)
        tl.trazaLinea(color='green', mapa=mainMap, new="yes", tipo=1)
    if 9 in lineas:
        # Linea 9
        c = getEstacion(lineaId=9)
        tl.nom_grup=l9
        tl.trazaEstaciones(data=c, mapa = mainMap, color='#3F2212', iconName='train', new="yes", tipo=1)
        tl.trazaLinea(color='#3F2212', mapa=mainMap, new="yes", tipo=1)
    if 10 in lineas:
        # Linea 10
        c = getEstacion(lineaId=10)
        tl.nom_grup=lA
        tl.trazaEstaciones(data=c, mapa = mainMap, color='purple', iconName='train', new="yes", tipo=1)
        tl.trazaLinea(color='purple', mapa=mainMap, new="yes", tipo=1)
    if 11 in lineas:
        # Linea 11
        c = getEstacion(lineaId=11)
        tl.nom_grup=lB
        tl.trazaEstaciones(data=c, mapa = mainMap, color='darkgreen', iconName='train', new="yes", tipo=1)
        tl.trazaLinea(color='darkgreen', mapa=mainMap, new="yes", tipo=1)
    if 12 in lineas:
        # Linea 12
        c = getEstacion(lineaId=12)
        tl.nom_grup=l12
        tl.trazaEstaciones(data=c, mapa = mainMap, color='gold', iconName='train', new="yes", tipo=1)
        tl.trazaLinea(color='gold', mapa=mainMap, new="yes", tipo=1)
    if 81 in lineas:
        # Linea 81
        c = getEstacion(lineaId=81)
        tl.nom_grup=l81
        tl.trazaEstaciones(data=c, mapa = mainMap, color='green', iconName='train', new="yes", tipo=1)
        tl.trazaLinea(color='green', mapa=mainMap, new="yes", tipo=1)        
    
def anilloInterior(lineas=[71,72,73,74]):
    if 71 in lineas:
        ###Linea 71 (Sur)
        c = getEstacion(lineaId=71)
        tl.nom_grup=l71
        tl.trazaEstaciones(data=c, mapa = mainMap, color='black', iconName='train', new="yes", tipo=2)
        tl.trazaLinea(color='black', mapa=mainMap, new="yes", tipo=2)
    if 72 in lineas:
        ###Linea 72 (Poniente)
        c = getEstacion(lineaId=72)
        tl.nom_grup=l72
        tl.trazaEstaciones(data=c, mapa = mainMap, color='gray', iconName='train', new="yes", tipo=2)
        tl.trazaLinea(color='gray', mapa=mainMap, new="yes", tipo=2)
    if 73 in lineas:
        ###Linea 73 (Norte)
        c = getEstacion(lineaId=73)
        tl.nom_grup=l73
        tl.trazaEstaciones(data=c, mapa = mainMap, color='darkred', iconName='train', new="yes", tipo=2)
        tl.trazaLinea(color='darkred', mapa=mainMap, new="yes", tipo=2)
    if 74 in lineas:
        ###Linea 74 (Oriente)
        c = getEstacion(lineaId=74)
        tl.nom_grup=l74
        tl.trazaEstaciones(data=c, mapa = mainMap, color='darkpurple', iconName='train', new="yes", tipo=2)
        tl.trazaLinea(color='purple', mapa=mainMap, new="yes", tipo=2)
    
def anilloExterior(lineas=[75,76,77,78]):
    if 75 in lineas:
        ###Linea 75 (Exterior Sur)
        c = getEstacion(lineaId=75)
        tl.nom_grup=l71
        tl.trazaEstaciones(data=c, mapa = mainMap, color='black', iconName='train', new="yes", tipo=2)
        tl.trazaLinea(color='black', mapa=mainMap, new="yes", tipo=2)
    if 76 in lineas:
        ###Linea 76 (Exterior Oriente)
        c = getEstacion(lineaId=76)
        tl.nom_grup=l72
        tl.trazaEstaciones(data=c, mapa = mainMap, color='darkpurple', iconName='train', new="yes", tipo=2)
        tl.trazaLinea(color='purple', mapa=mainMap, new="yes", tipo=2)
    if 77 in lineas:
        ###Linea 77 (Exterior Norte)
        c = getEstacion(lineaId=77)
        tl.nom_grup=l73
        tl.trazaEstaciones(data=c, mapa = mainMap, color='darkred', iconName='train', new="yes", tipo=2)
        tl.trazaLinea(color='darkred', mapa=mainMap, new="yes", tipo=2)
    if 78 in lineas:
        ###Linea 78 (Exterior Poniente)
        c = getEstacion(lineaId=78)
        tl.nom_grup=l74
        tl.trazaEstaciones(data=c, mapa = mainMap, color='gray', iconName='train', new="yes", tipo=2)
        tl.trazaLinea(color='gray', mapa=mainMap, new="yes", tipo=2)

#principales()
##
anilloExterior()
anilloInterior()
fl.LayerControl(collapsed=False).add_to(mainMap)
GroupedLayerControl(
    groups={'Líneas Principales': [l1, l2, l3, l4, 
                                   l5, l6, l7, l8, 
                                   l9, lA, lB, l12],
            'Líneas Anillares Interiores': [l71, l72, l73, l74],
            'Líneas Anillares Exteriores': [l75]},
).add_to(mainMap)
mainMap.save("mapa_base.html")


