import CONSTANTS
class TrazaLineas():
    latlong_origin = []
    tipo_transporte = CONSTANTS.tipo_transporte
    foliums = None
    nom_grup = None
    
    def trazaEstaciones(self, data, mapa, color, iconName, new = "no", tipo=0):
        tpgroup= self.foliums.FeatureGroup(name=self.tipo_transporte[tipo])
        if new == "yes":
            print("Reinicio de la lista de ubicaciones")
            self.latlong_origin=[]        
        for i in data:
            self.foliums.Marker(location=[i['latitud'], i['longitud']],
                        icon = self.foliums.Icon(color = color, icon = iconName,prefix='fa'),
                        popup = i['nombre']
                        ).add_to(self.nom_grup)
            self.foliums.Marker(location=[i['latitud'], i['longitud']],
                        icon = self.foliums.Icon(color = color, icon = iconName,prefix='fa'),
                        popup = i['nombre']
                        ).add_to(tpgroup)
            self.latlong_origin.append([i['latitud'], i['longitud']])
            mapa.add_child(tpgroup)
            mapa.add_child(self.nom_grup)
            #self.nom_grup.add_to(mapa)
            #tpgroup.add_to(mapa)
            #mapa.add_child(self.linea_familia)
        
    def trazaLinea(self,color, mapa, new="no", tipo=0):
        tpgroup= self.foliums.FeatureGroup(name=self.tipo_transporte[tipo])
        if new == "yes":
            print("Reinicio de la lista de ubicaciones")
            print(self.latlong_origin)
        self.foliums.PolyLine(self.latlong_origin, color = color, weight=7).add_to(self.nom_grup)
        self.foliums.PolyLine(self.latlong_origin, color = color, weight=7).add_to(tpgroup)
        mapa.add_child(tpgroup)
        mapa.add_child(self.nom_grup)        
        #self.nom_grup.add_to(mapa)
        #tpgroup.add_to(mapa)
        #mapa.add_child(self.linea_familia)
        ###687194