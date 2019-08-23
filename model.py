def pretvori_maso(kolicina, stara_enota, nova_enota):
    kolicina = float(kolicina)
    vse_enote = {"g":1, "dag":10, "kg":1000, "t":1000000, "mg":0.001, "lbs":453.5923}
    if stara_enota.lower() not in vse_enote or nova_enota.lower() not in vse_enote:
        return False
    else:
        kolicina *= vse_enote[stara_enota.lower()]
        kolicina /= vse_enote[nova_enota.lower()]
        return kolicina

def pretvori_dolzino(kolicina, stara_enota, nova_enota):
    kolicina = float(kolicina)
    vse_enote = {"m":1, "dm":0.1, "cm":0.01, "mm":0.001, "km":1000, "milja":1609.3445, "morska milja":1851.9993} 
    if stara_enota.lower() not in vse_enote or nova_enota.lower() not in vse_enote:
        return False
    else:
        kolicina *= vse_enote[stara_enota.lower()]
        kolicina /= vse_enote[nova_enota.lower()]
        return kolicina

def pretvori_volumen(kolicina, stara_enota, nova_enota):
    kolicina = float(kolicina)
    vse_enote = {"l":1, "dl":0.1, "cl":0.01, "ml":0.001, "us gal":3.7850} 
    if stara_enota.lower() not in vse_enote or nova_enota.lower() not in vse_enote:
        return False
    else:
        kolicina *= vse_enote[stara_enota.lower()]
        kolicina /= vse_enote[nova_enota.lower()]
        return kolicina
