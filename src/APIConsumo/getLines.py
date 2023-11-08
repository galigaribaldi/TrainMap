import requests
import src.VARS as VARS
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

def getLinea(idLine=None, colorEsp=None):
    data_send = {}
    if idLine!=None:
        data_send["idLine"] = str(idLine)
    if colorEsp!=None:
        data_send["color_esp"] = str(colorEsp)
    if len(data_send) > 0:
        print("Send Response: ", data_send)
        response = requests.request("GET", VARS.Production.HOST+"/stc/linea", headers=headers,params = data_send)
    else:
        response = requests.request("GET", VARS.Production.HOST+"/stc/linea", headers=headers)
    return response.json()
    