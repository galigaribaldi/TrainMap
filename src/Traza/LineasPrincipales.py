from src.CONSTANTS import TRANSPORTES

class TrazaLineas():
    
    latlong_origin = []
    foliums = None
    subGroup = None
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
                print("Nombre de Feature Group:",  TRANSPORTES[i['linea_id']]['NOMBRE'],TRANSPORTES[i['linea_id']]['TIPO'])
            self.foliums.Marker(
                location=[i['latitud'], i['longitud']],
                icon = self.foliums.Icon(
                    color = TRANSPORTES[i['linea_id']]['COLOR'], 
                    icon = TRANSPORTES[i['linea_id']]['ICON'],prefix='fa'),
                popup = i['nombre']
            ).add_to(self.nomGroup)
            self.latlong_origin.append([i['latitud'], i['longitud']])
            mapa.add_child(self.nomGroup)
            cont = cont +1

    def trazaLinea(self, mapa, new="no", id=1):
        if new == "yes":
            print("Reinicio de la lista de ubicaciones")
            print(self.latlong_origin)
        self.foliums.PolyLine(self.latlong_origin, color = TRANSPORTES[id]['COLOR'], weight=6).add_to(self.nomGroup)
        mapa.add_child(self.nomGroup)