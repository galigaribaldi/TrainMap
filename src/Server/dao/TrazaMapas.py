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

def trazaCompleto(lineaPrincipales, lineaAnillarInteior, lineaAnillarExterior):
    p = TrainMap()
    p.LineasPrincipales(lineaPrincipales)
    p.LineasAnillaresInteriores(lineaAnillarInteior)
    p.LineasAnillaresExteriores(lineaAnillarExterior)
    p.Escritura()