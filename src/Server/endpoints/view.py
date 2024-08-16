from flask import Blueprint, render_template, request
import src.Server.dao.TrazaMapas as Dao

endP1 = Blueprint("endP1", __name__)

@endP1.route('/')
def home():
    return "Works!"

@endP1.route('/map')
@endP1.route('/map/')
@endP1.route('/map/completo')
@endP1.route('/map/Completo')
@endP1.route('/map/completo/')
@endP1.route('/map/Completo/')
def map():
    print("Completo")
    Dao.trazaCompleto(
        [1,2,3,4,5,6,7,8,9,10,11,12,81], ##metro
        [71,72,73,74], ##periferico interior
        [75,76,77,78], ##periferico exterior
        [801, 802, 803, 804], ## interurbano
        [910, 911, 920, 930, 940, 941, 942, 950, 960, 970, 971, 972, 980, 990, 991]
    )
    return render_template("mapa_base.html")


@endP1.route('/map/Principal')
@endP1.route('/map/principal')
@endP1.route('/map/principales')
def mapPrincipal():
    linea =[1,2,3,4,5,6,7,8,9,10,11,12,81]
    Dao.trazaPrincipales(linea)
    return render_template("principales.html")


@endP1.route('/map/AnillarI')
@endP1.route('/map/anillarI')
@endP1.route('/map/anillari')
def mapAnillarInterior():
    linea =[71,72,73,74]
    Dao.trazaAnillaresInteriores(linea)
    return render_template("anillaresInteriores.html")


@endP1.route('/map/AnillarE')
@endP1.route('/map/anillarE')
@endP1.route('/map/anillare')
def mapAnillarE():
    linea =[75,76,77,78]
    Dao.trazaAnillaresExteriores(linea)
    return render_template("anillaresExteriores.html")

@endP1.route('/map/InterUrbano')
@endP1.route('/map/Interurbano')
@endP1.route('/map/interUrbano')
def mapInterUrbano():
    linea =[801, 802, 803, 804]
    Dao.trazaInterUrbano(linea)
    return render_template("InterUrbano.html")

@endP1.route('/map/CableBus')
@endP1.route('/map/Cablebus')
@endP1.route('/map/cableBus')
@endP1.route('/map/cablebus')
def mapCableBus():
    linea =[
        910, 911,
        920,
        930,
        940, 941, 942,
        950,
        960,
        970, 971, 972,
        980,
        990, 991]
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