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
        self.mainMap = fl.Map(titles = 'Map',location =[19.434430271379885, -99.13309144564224], zoom_start=11.4)
        self.tl = TrazaLineas(fl)
        
    def LineasPrincipales(self, lineas =[]):
        lineasPrincipales = []
        genericLine = fl.FeatureGroup(name = 'Principales', control=True, show=True)
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
        genericLine = fl.FeatureGroup(name = 'Anillares Interiores', control=True, show=True)
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
        genericLine = fl.FeatureGroup(name = 'Anillares Exteriores', control=True, show=True)
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
        genericLine = fl.FeatureGroup(name = 'Metrobus', control=True, show=True)
        self.tl.tpgroup = genericLine
        lineasMetrobus.append(genericLine)
        return lineasMetrobus
    
    def LineasCablebus(self, lineas=[]):
        print("Lineas Cablebus")
        lineasCablebus = []
        genericLine = fl.FeatureGroup(name = 'Cablebus', control=True, show=True)
        if len(lineas) >0:
            for i in lineas:
                c = getEstacion(lineaId= i)
                self.tl.trazaEstaciones(data=c, mapa=self.mainMap, new='yes')
                self.tl.trazaLinea(mapa=self.mainMap, id=i, new='yes')
                self.tl.tpgroup = genericLine 
                lineasCablebus.append(genericLine)
        return lineasCablebus
    
    def LineasTrenInterUrbano(self, lineas = []):
        lineasInterurbanas = []
        genericLine = fl.FeatureGroup(name = 'InterUrbano', control=True, show=True)
        if len(lineas) >0:
            print("Lineas: ", lineas)
            for i in lineas:
                print("Lineas: ", i)
                c = getEstacion(lineaId= i)
                print("Estaciones: ", c)
                self.tl.trazaEstaciones(data=c, mapa=self.mainMap, new='yes')
                self.tl.trazaLinea(mapa=self.mainMap, id=i, new='yes')
                self.tl.tpgroup = genericLine 
                lineasInterurbanas.append(genericLine)
        return lineasInterurbanas
    
    def Escritura(self, nombre='mapa', lineaPrincipal=[]):
        fl.LayerControl(collapsed=True).add_to(self.mainMap)
        self.mainMap.save("src/Server/templates/" + nombre +".html")
