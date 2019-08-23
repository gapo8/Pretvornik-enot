import bottle
import model

@bottle.get("/")
def pozdrav():
    return bottle.template("index.html")

@bottle.get("/masa/")
def masa():
    return bottle.template("pretvornik_masa.html", rezultat=None, napaka=None)

@bottle.post("/masa/")
def pretvori_maso():
    kolicina =  bottle.request.forms.getunicode("kolicina")
    stara_enota =  bottle.request.forms.getunicode("stara_enota")
    nova_enota =  bottle.request.forms.getunicode("nova_enota")
    if kolicina == "" or stara_enota == "" or nova_enota == "":
        return bottle.template("pretvornik_masa.html", napaka="Niste vpisali vseh enot", rezultat=None) 
    else:
        rezultat = model.pretvori_maso(kolicina, stara_enota, nova_enota)
        if rezultat == False:
            return bottle.template("pretvornik_masa.html", napaka="Neprepoznana enota. Prosim izberite enoto iz tabele.", rezultat=None)
        else:
            return bottle.template("pretvornik_masa.html", rezultat=rezultat, napaka=None)



@bottle.get("/dolzina/")
def dolzina():
    return bottle.template("pretvornik_dolzina.html", rezultat=None, napaka=None)

@bottle.post("/dolzina/")
def pretvori_dolzino():
    kolicina = bottle.request.forms.getunicode("kolicina")
    stara_enota = bottle.request.forms.getunicode("stara_enota")
    nova_enota = bottle.request.forms.getunicode("nova_enota")
    if kolicina == "" or stara_enota == "" or nova_enota == "":
        return bottle.template("pretvornik_dolzina.html", napaka="Niste vpisali vseh enot", rezultat=None)
    else:
        rezultat = model.pretvori_dolzino(kolicina, stara_enota, nova_enota)
        if rezultat == False:
            return bottle.template("pretvornik_dolzina.html", napaka="Neprepoznana enota. Prosim izberite enoto iz tabele.", rezultat=None)
        else:
            return bottle.template("pretvornik_dolzina.html", rezultat=rezultat, napaka=None)



@bottle.get("/volumen/")
def volumen():
    return bottle.template("pretvornik_volumen.html", enota="volumen", rezultat=None, napaka=None)

@bottle.post("/volumen/")
def pretvori_volumen():
    kolicina =  bottle.request.forms.getunicode("kolicina")
    stara_enota =  bottle.request.forms.getunicode("stara_enota")
    nova_enota =  bottle.request.forms.getunicode("nova_enota")
    if kolicina == "" or stara_enota == "" or nova_enota == "":
        return bottle.template("pretvornik_volumen.html", napaka="Niste vpisali vseh enot", rezultat=None)
    else:
        rezultat = model.pretvori_volumen(kolicina, stara_enota, nova_enota)
        if rezultat == False:
            return bottle.template("pretvornik_volumen.html", napaka="Neprepoznana enota. Prosim izberite enoto iz tabele.", rezultat=None)
        else:
            return bottle.template("pretvornik_volumen.html", rezultat=rezultat, napaka=None)

bottle.run(debug=True, realoader=True)