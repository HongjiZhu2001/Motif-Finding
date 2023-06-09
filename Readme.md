# Motif-Finding
The goal for this project is to implement the findMotifsGenome.pl from Homer in python.
The project seprates into two parts 
<br/><br/>


## Set up
``` pip install -r requirement.txt```

If you encounter any errors with seqlogo, you may also need to install Ghostscript: https://ghostscript.com/releases/gsdnld.html

## Part1: Read peak.txt & reference genome files to generate motif matrix


## Part2: Use motif matrix to generate the html report
Usage: python HTML_Report.py -f motif_matrix_file -l motif_length [optional]-o output_file_name(out.html if not specified)

e.g. python HTML_Report.py -f homerMotifs.motifs12.txt -l 12

or with output file name: python HTML_Report.py -f homerMotifs.motifs8.txt -l 8 -o Oct4_len8
<br/><br/>

Currently the repository contains homerMotifs.motifs12.txt, and homerMotifs.motifs8.txt, which are the motif matrix of Oct4 in length 12 and length 8. Oct4_len12.html and Oct4_len8.html are the example output of these two motif matrix file. Feel free to also try with other motif matrices of other TFs.
<br/><br/>

Future work for this part: Currenly the motif patterns matches the Homer output, which means that the HTML_Report.py worked successfully, but the Homer output does not present all the motifs in the motif matrix file. Next step is to find what's the filtering requirements and also add more elements and information to the html output
