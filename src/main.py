import folium as fl
from folium.plugins import GroupedLayerControl
##Modulos propios
from src.APIConsumo.getEstacions import getEstacion
from src.APIConsumo.getLines import getLinea
from src.Traza.LineasPrincipales import TrazaLineas
from src.CONSTANTS import TRANSPORTES

class TrainMap():
    
    mainMap = None
    tl = None
    
    def __init__(self):
        self.mainMap = fl.Map(location =[19.434430271379885, -99.13309144564224], zoom_start=11.4)
        self.tl = TrazaLineas(fl)
        
    def LineasPrincipales(self, lineas =[]):
        lineasPrincipales = []
        genericLine = fl.FeatureGroup(name = 'Principales')
        if len(lineas) >0:
            for i in lineas:
                c = getEstacion(lineaId= i)
                self.tl.trazaEstaciones(data=c, mapa=self.mainMap, new='yes')
                self.tl.trazaLinea(mapa=self.mainMap, id=i, new='yes')
                self.tl.tpgroup = genericLine 
                lineasPrincipales.append(genericLine)
        return lineasPrincipales
    
    def LineasAnillaresInteriores(self, lineas =[]):
        lineasAnillaresInteriores = []
        genericLine = fl.FeatureGroup(name = 'Anillares Interiores')
        if len(lineas) >0:
            for i in lineas:
                c = getEstacion(lineaId= i)
                self.tl.trazaEstaciones(data=c, mapa=self.mainMap, new='yes')
                self.tl.trazaLinea(mapa=self.mainMap, id=i, new='yes')
                self.tl.tpgroup = genericLine 
                lineasAnillaresInteriores.append(genericLine)
        return lineasAnillaresInteriores
    
    def LineasAnillaresExteriores(self, lineas = []):
        lineasAnillaresExteriores = []
        genericLine = fl.FeatureGroup(name = 'Anillares Exteriores')
        if len(lineas) >0:
            for i in lineas:
                c = getEstacion(lineaId= i)
                self.tl.trazaEstaciones(data=c, mapa=self.mainMap, new='yes')
                self.tl.trazaLinea(mapa=self.mainMap, id=i, new='yes')
                self.tl.tpgroup = genericLine 
                lineasAnillaresExteriores.append(genericLine)        
        return lineasAnillaresExteriores
    
    def LineasMetrobus(self):
        lineasMetrobus = []
        return lineasMetrobus
    def LineasCablebus(self):
        lineasCablebus = []
        return lineasCablebus
    
    def LineasTrenInterUrbano(self):
        lineasInterurbanas = []
        return lineasInterurbanas
    
    def Escritura(self, nombre='mapa_base'):
        self.LineasPrincipales()
        self.LineasAnillaresInteriores()
        self.LineasAnillaresExteriores()
        self.LineasTrenInterUrbano()
        self.LineasMetrobus()
        self.LineasCablebus()
        
        fl.LayerControl(collapsed=False).add_to(self.mainMap)
        GroupedLayerControl(
            groups=
            {
                'Líneas Principales': self.LineasPrincipales(),
                'Líneas Anillares Interiores': self.LineasAnillaresInteriores(),
                'Líneas Inter-Urbanas': self.LineasTrenInterUrbano(),
                'Líneas Metrobus': self.LineasMetrobus(),
                'Líneas Cabelbus': self.LineasCablebus(),
            },
        ).add_to(self.mainMap)
        self.mainMap.save("src/Server/templates/" + nombre +".html")

#prueba = TrainMap()
#prueba.LineasPrincipales(lineas=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12, 81])
#prueba.LineasAnillaresInteriores(lineas=[71,72, 73, 74])
#prueba.LineasAnillaresExteriores(lineas=[75,76, 77, 78])
#prueba.Escritura()