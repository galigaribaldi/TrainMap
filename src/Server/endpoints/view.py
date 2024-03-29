from flask import Blueprint, render_template, request
import src.Server.dao.TrazaMapas as Dao

endP1 = Blueprint("endP1", __name__)

@endP1.route('/')
def home():
    return "Works!"

@endP1.route('/map')
def map():
    Dao.trazaCompleto([1,2,3,4,5,6,7,8,9,10,11,12,81], [71,72,73,74], [75,76,77,78])
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

