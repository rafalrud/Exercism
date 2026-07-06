def to_rna(dna_strand):
    dna = "GCTA"
    rna = "CGAU"
    result = ""
    for char in dna_strand:
        if char.isalpha():
            index = dna.find(char)
            result += rna[index]
        else:
            result += char
    return result