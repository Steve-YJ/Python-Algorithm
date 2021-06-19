def DNA_strand(dna):
    # code here
    dic = {"A" : "T",
          "T" : "A",
          "C" : "G",
          "G" : "C"}
    
    return "".join(dic[d] for d in dna)