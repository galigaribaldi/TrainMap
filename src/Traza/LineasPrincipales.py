from src.CONSTANTS import TRANSPORTES

class TrazaLineas():
    
    latlong_origin = []
    foliums = None
    tpgroup = None
    nomGroup = None
    
    def __init__(self, fl):
        self.foliums = fl
    
    def trazaEstaciones(self,data, mapa, new = "no"):
        if new == "yes":
            print("Reinicio de la lista de ubicaciones")
            print(self.latlong_origin)
            self.latlong_origin=[]
        cont = 0
        for i in data:
            if cont <1:
                self.nomGroup = self.foliums.FeatureGroup(name = TRANSPORTES[i['linea_id']]['NOMBRE'], control=True)
                print("Nombre de Feature Group:",  TRANSPORTES[i['linea_id']]['NOMBRE'])
            #self.tpgroup= self.foliums.FeatureGroup(name=TRANSPORTES[i['linea_id']]['TIPO'], control=True)
            
            self.foliums.Marker(
                location=[i['latitud'], i['longitud']],
                icon = self.foliums.Icon(
                    color = TRANSPORTES[i['linea_id']]['COLOR'], 
                    icon = TRANSPORTES[i['linea_id']]['ICON'],prefix='fa'),
                popup = i['nombre']
            ).add_to(self.nomGroup)
            """
            self.foliums.Marker(
                location=[i['latitud'], i['longitud']],
                icon = self.foliums.Icon(
                    color = TRANSPORTES[i['linea_id']]['COLOR'], 
                    icon = TRANSPORTES[i['linea_id']]['ICON'],prefix='fa'),
                popup = i['nombre']
            ).add_to(self.tpgroup)
            """
            self.latlong_origin.append([i['latitud'], i['longitud']])
            mapa.add_child(self.nomGroup)
            #mapa.add_child(self.tpgroup)
            cont = cont +1
    def trazaLinea(self, mapa, new="no", id=1):
        #self.tpgroup= self.foliums.FeatureGroup(name=TRANSPORTES[id]['TIPO'], control=True)
        if new == "yes":
            print("Reinicio de la lista de ubicaciones")
            print(self.latlong_origin)
        self.foliums.PolyLine(self.latlong_origin, color = TRANSPORTES[id]['COLOR'], weight=7).add_to(self.nomGroup)
        #self.foliums.PolyLine(self.latlong_origin, color = TRANSPORTES[id]['COLOR'], weight=7).add_to(self.tpgroup)
        #mapa.add_child(self.tpgroup)
        mapa.add_child(self.nomGroup)