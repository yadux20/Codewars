def DNA_strand(dna):
    res = ""
    for i in dna:
        if i == "A": res += "T"
        elif i == "T": res+="A"
        elif i == "G": res+="C"
        elif i == "C": res+="G"
    return res