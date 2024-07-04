from src.main import TrainMap

def trazaPrincipales(linea):
    p = TrainMap()
    p.LineasPrincipales(linea)
    p.Escritura("principales")

def trazaAnillaresInteriores(linea):
    p = TrainMap()
    p.LineasAnillaresInteriores(linea)
    p.Escritura("anillaresInteriores")
    
def trazaAnillaresExteriores(linea):
    p = TrainMap()
    p.LineasAnillaresExteriores(linea)
    p.Escritura("anillaresExteriores")

def trazaInterUrbano(linea):
    p = TrainMap()
    p.LineasTrenInterUrbano(linea)
    p.Escritura("InterUrbano")

def trazaCablebus(linea):
    p = TrainMap()
    p.LineasCablebus(linea)
    p.Escritura("Cablebus")

def trazaMetrobus(linea):
    p = TrainMap()
    p.LineasMetrobus(linea)
    p.Escritura("Metrobus")    

def trazaCompleto(lineaPrincipales, lineaAnillarInteior, lineaAnillarExterior, lineaInterUrbano, lineasCablebus):
    p = TrainMap()
    p.LineasPrincipales(lineaPrincipales)
    p.LineasAnillaresInteriores(lineaAnillarInteior)
    p.LineasAnillaresExteriores(lineaAnillarExterior)
    p.LineasTrenInterUrbano(lineaInterUrbano)
    p.LineasCablebus(lineasCablebus)
    p.Escritura()