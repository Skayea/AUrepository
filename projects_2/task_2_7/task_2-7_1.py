files = ["seq1", "seq2", "seq3", "seq4"]
date = "_12_12_2026"

for name in files:
   new_name = name + date + ".fasta"
   print(f"{new_name}")