import requests
import src.VARS as VARS

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

def getEstacion(nombre=None, anio=None, anio_antes=None, anio_despues=None, ciudad=None, alacaldiaMunicipio=None, lineaId=None, colorEsp=None, colorEn=None):
    print("GET")
    data_send = {}
    if nombre!=None:
        data_send["nombre"] = str(nombre)
    if anio!=None:
        data_send["anio"] = str(anio)
    if anio_antes!=None:
        data_send["anio_antes"] = str(anio_antes)
    if anio_despues!=None:
        data_send["anio_despues"] = str(anio_despues)
    if ciudad!=None:
        data_send["ciudad"] = str(ciudad)
    if alacaldiaMunicipio!=None:
        data_send["alacaldia_municipio"] = str(alacaldiaMunicipio)
    if lineaId!=None:
        data_send["linea_id"] = str(lineaId)
    if colorEsp!=None:
        data_send["color_esp"] = str(colorEsp)
    if colorEn!=None:
        data_send["color_en"] = str(colorEn)
        
    if len(data_send) > 0:
        print("Send Response: ", data_send)
        response = requests.request("GET", VARS.Developer.HOST+"/stc/estacion", headers=headers,params = data_send)
    else:
        response = requests.request("GET", VARS.Developer.HOST+"/stc/estacion", headers=headers)
    return response.json()
#c = getEstacion(lineaId=2)
#print(c)