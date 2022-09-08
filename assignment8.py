#Assignment 8
import csv
import re

def translate(dna):
    aminos = []
    if not re.search("^([CAGT]{3})+$", dna):
        return None
    for i in range(0, len(dna), 3):
        chunk = dna[i:i+3]
        amino = CODON_TABLE[chunk]
        aminos.append(amino)
    return(",".join(aminos))


CODON_TABLE = {
  "TTT":"Phenylalanine",
  "TTC":"Phenylalanine",
  "TTA":"Leucine",
  "TTG":"Leucine",
  "CTT":"Leucine",
  "CTC":"Leucine",
  "CTA":"Leucine",
  "CTG":"Leucine",
  "ATT":"Isoleucine",
  "ATC":"Isoleucine",
  "ATA":"Isoleucine",
  "ATG":"Methionine",
  "GTT":"Valine",
  "GTC":"Valine",
  "GTA":"Valine",
  "GTG":"Valine",
  "TCT":"Serine",
  "TCC":"Serine",
  "TCA":"Serine",
  "TCG":"Serine",
  "CCT":"Proline",
  "CCC":"Proline",
  "CCA":"Proline",
  "CCG":"Proline",
  "ACT":"Threonine",
  "ACC":"Threonine",
  "ACA":"Threonine",
  "ACG":"Threonine",
  "GCT":"Alanine",
  "GCC":"Alanine",
  "GCA":"Alanine",
  "GCG":"Alanine",
  "TAT":"Tyrosine",
  "TAC":"Tyrosine",
  "TAA":".",
  "TAG":".",
  "CAT":"Histidine",
  "CAC":"Histidine",
  "CAA":"Glutamine",
  "CAG":"Glutamine",
  "AAT":"Asparagine",
  "AAC":"Asparagine",
  "AAA":"Lysine",
  "AAG":"Lysine",
  "GAT":"Aspartic acid",
  "GAC":"Aspartic acid",
  "GAA":"Glutamic acid",
  "GAG":"Glutamic acid",
  "TGT":"Cysteine",
  "TGC":"Cysteine",
  "TGA":".",
  "TGG":"Tryptophan",
  "CGT":"Arginine",
  "CGC":"Arginine",
  "CGA":"Arginine",
  "CGG":"Arginine",
  "AGT":"Serine",
  "AGC":"Serine",
  "AGA":"Arginine",
  "AGG":"Arginine",
  "GGT":"Glycine",
  "GGC":"Glycine",
  "GGA":"Glycine",
  "GGG":"Glycine"
}   

print("Enter amino acid sequence")
query = input()

with open('samples.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_data = list(csv_reader)
    
    for patient in range(1, len(csv_data)):
        row = csv_data[patient]
        name = row[0]
        seq = row[1]
        amino_seq = translate(seq)
        if query in amino_seq:
            print(name)

