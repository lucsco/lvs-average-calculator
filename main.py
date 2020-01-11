from funcs import *
import time
import os

def moy(txt):
    text = ""
    lines = txt.split("\n")
    matieres = [
            "S.V.T.",
 	    "Mathématiques",
            "Physique-Chimie", 
 	    "Français", 
            "H.Géo", 
            "LV1 - Ecrit", 
	    "LV1 - Oral", 
	    "LV2 - Ecrit", 
	    "LV2 - Oral", 
	    "EPS",
            "Technologie"
	    ]
    metm = {}
    for line in lines:
        for matiere in matieres:
            if matiere in line:
                metm[line] = None 
    for x in metm:
        coeffs = []
        nts = []
        for a, line in enumerate(lines):
            if x in line:
                matiere = line
                notes = lines[a+1].split(" ")
                for b, mot in enumerate(notes):
                    if "coeff" in mot:
                        coeffs.append(coeff(notes[b+1]))
                        if note(notes[b+3]) == "what":
                            del coeffs[-1]
                        else:
                            nts.append(note(notes[b+3]))
        if "LV" and "Oral" in matiere:
            pass
        metm[matiere] = moyenne(nts, coeffs)
    if metm != {}:
    	metm["MOYENNE GÉNÉRALE (fausse)"] = moyenne_sc(metm.values())
    	return metm
    else:
    	return {"invalid" : "input"}
    
    print(metm)



