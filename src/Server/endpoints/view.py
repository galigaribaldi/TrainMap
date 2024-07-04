from flask import Blueprint, render_template, request
import src.Server.dao.TrazaMapas as Dao

endP1 = Blueprint("endP1", __name__)

@endP1.route('/')
def home():
    return "Works!"

@endP1.route('/map')
def map():
    Dao.trazaCompleto
    (
        [1,2,3,4,5,6,7,8,9,10,11,12,81], ##metro
        [71,72,73,74], ##periferico interior
        [75,76,77,78], ##periferico exterior
        [801, 802, 803, 804], ## interirbano
        [910, 911]
        )
    return render_template("mapa_base.html")

@endP1.route('/map/principal')
def mapPrincipal():
    linea =[1,2,3,4,5,6,7,8,9,10,11,12,81]
    Dao.trazaPrincipales(linea)
    return render_template("principales.html")

@endP1.route('/map/anillarI')
def mapAnillarInterior():
    linea =[71,72,73,74]
    Dao.trazaAnillaresInteriores(linea)
    return render_template("anillaresInteriores.html")


@endP1.route('/map/anillarE')
def mapAnillarE():
    linea =[75,76,77,78]
    Dao.trazaAnillaresExteriores(linea)
    return render_template("anillaresExteriores.html")

@endP1.route('/map/InterUrbano')
def mapInterUrbano():
    linea =[801, 802, 803, 804]
    Dao.trazaInterUrbano(linea)
    return render_template("InterUrbano.html")

@endP1.route('/map/CableBus')
def mapCableBus():
    linea =[910, 911]
    Dao.trazaCablebus(linea)
    return render_template("Cablebus.html")

@endP1.route('/map/Metrobus')
def mapMetrobus():
    linea =[]
    Dao.trazaMetrobus(linea)
    return render_template("Metrobus.html")

@endP1.route('/map/proof/<int:linea_id>/<int:linea_id2>')
def mapproof(linea_id=12, linea_id2=0):
    if linea_id2 != 0:
        linea =[linea_id, linea_id2]
    else:
        linea =[linea_id]
    Dao.trazaInterUrbano(linea)
    return render_template("InterUrbano.html")