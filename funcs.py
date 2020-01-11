def coeff(nb):
    c = nb.replace(")","")
    c = float(c.replace(",","."))
    return c

def note(nb):
    if not "/20" in nb:
        return "what"
    c = nb.replace("/20","")
    c = float(c.replace(",","."))
    return c


def moyenne(ntsf, cfsf):
    if len(ntsf) != len(cfsf):
        return "what"
    a = []
    for g, note in enumerate(ntsf):
        a.append(note * cfsf[g])
    moy = sum(a) / sum(cfsf)
    return moy

def moyenne_sc(ntes):
    return sum(ntes) / len(ntes)

def lv_moy(matiere, ecrit, oral):
    pass
