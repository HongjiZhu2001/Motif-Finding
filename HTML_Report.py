#Run with python HTML_Report.py motif_matrix_file motif_length [optional]output_file_name(out.html if not specified)
#i.e. python HTML_Report.py homerMotifs.motifs12.txt 12
#with output file name: python HTML_Report.py homerMotifs.motifs8.txt 8 Oct4_len8


import numpy as np
import seqlogo
import pandas as pd
import base64
import sys


motifFile = sys.argv[1]
motif_lenth = int(sys.argv[2])
out_name = "no input"
try:
    out_name = sys.argv[3]
except:
    pass


f = open(motifFile,  "r")
lines = f.readlines()
f.close()

motifs = []
pvals = []
sequences = []
for idx, line in enumerate(lines):
    if line.startswith(">"):
        currMatrixLines = lines[idx+1 : idx+1+motif_lenth]
        currMatrix = []
        for i in currMatrixLines:
            i = i.removesuffix("\n")
            elements = i.split("\t")
            elements = [ float(x) for x in elements ]
            currMatrix.append(elements)
        currMatrix = np.array(currMatrix)
        motifs.append(currMatrix)
        
        #for p-value
        idx1 = line.find("P:")
        idx2 = line.find("\t", idx1)
        curr_p_val = line[idx1 + 2: idx2]
        pvals.append(curr_p_val)
        
        #motif sequence
        currSeq = line[1: 1+motif_lenth]
        sequences.append(currSeq)
        
df = pd.DataFrame(columns=["motif", "image", "pval"])
        
for idx, motif in enumerate(motifs):
    
    pfm = pd.DataFrame(motif * 1000)

    seq_pfm = seqlogo.Pfm(pfm / np.sum(motif, 0)[0])
    seq_ppm = seqlogo.Ppm(seqlogo.pfm2ppm(seq_pfm))

    img_path = "seq_logo.png"
    seqlogo.seqlogo(seq_ppm, ic_scale=True, format='png', size='medium', filename=img_path)

    with open(img_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    image_html = f'<img src="data:image/png;base64,{encoded_image}" />'

    curr = [sequences[idx], image_html, pvals[idx]]
    df.loc[len(df)] = curr

if out_name != "no input":
    df.to_html(out_name+".html", index=False, escape=False)
else:
    df.to_html("out.html", index=False, escape=False)