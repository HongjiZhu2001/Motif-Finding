import numpy as np
import seqlogo
import pandas as pd
import base64
import sys


motifFile = sys.argv[1]
out_name = "no input"
try:
    out_name = sys.argv[2]
except:
    pass


f = open(motifFile,  "r")
lines = f.readlines()
f.close()

motifs = []

sequences = []
names = []
for idx, line in enumerate(lines):
    if line.startswith(">"):
        start = idx
        curr = line
        curr_idx = idx
        out = False
        while out == False:
            if curr_idx == len(lines)-1:
                out = True
            else:
                curr_idx+=1
                curr = lines[curr_idx]
                if curr.startswith(">"):
                    out = True
        end = curr_idx
        currMatrixLines = lines[start+1 : end]
        currMatrix = []
        for i in currMatrixLines:
            i = i.removesuffix("\n")
            elements = i.split()
            elements = [ float(x) for x in elements ]
            currMatrix.append(elements)
        currMatrix = np.array(currMatrix)
        motifs.append(currMatrix)
        
        
        #motif sequence
        currSeq = line[1: (end-start)]
        sequences.append(currSeq)

        #name
        names.append(line.split()[1])
        
df = pd.DataFrame(columns=["motif", "image", "name"])
        
for idx, motif in enumerate(motifs):
    
    pfm = pd.DataFrame(motif * 1000)

    seq_pfm = seqlogo.Pfm(pfm / np.sum(motif, 0)[0])
    seq_ppm = seqlogo.Ppm(seqlogo.pfm2ppm(seq_pfm))

    img_path = "seq_logo.png"
    seqlogo.seqlogo(seq_ppm, ic_scale=True, format='png', size='large', filename=img_path)

    with open(img_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    image_html = f'<img src="data:image/png;base64,{encoded_image}" />'

    curr = [sequences[idx], image_html, names[idx]]
    df.loc[len(df)] = curr

if out_name != "no input":
    df.to_html(out_name+".html", index=False, escape=False)
else:
    df.to_html("out.html", index=False, escape=False)