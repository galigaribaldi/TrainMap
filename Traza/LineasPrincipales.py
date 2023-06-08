class TrazaLineas():
    
    latlong_origin = []
    
    def trazaEstaciones(self, data, folio, mapa, color, iconName, new = "no"):
        if new == "yes":
            print("REinicio de la lista de ubicaciones")
            self.latlong_origin=[]        
        for i in data:
            folio.Marker(location=[i['latitud'], i['longitud']],
                        icon = folio.Icon(color = color, icon = iconName,prefix='fa'),
                        popup = "<h3>"+ i['nombre']+"</h3>"
                        ).add_to(mapa)
            self.latlong_origin.append([i['latitud'], i['longitud']])
        
    def trazaLinea(self, folio,color, mapa, new="no"):
        if new == "yes":
            print("REinicio de la lista de ubicaciones")
            print(self.latlong_origin)
        folio.PolyLine(self.latlong_origin, color = color, weight=7).add_to(mapa)