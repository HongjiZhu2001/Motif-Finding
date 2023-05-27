# Motif-Finding

## Part1: Read peak.txt file and generate motif matrix
not finished yet

## Part2: Use motif matrix to generate the html report
Usage: python HTML_Report.py motif_matrix_file motif_length [optional]output_file_name(out.html if not specified)

i.e. python HTML_Report.py homerMotifs.motifs12.txt 12

with output file name: python HTML_Report.py homerMotifs.motifs8.txt 8 Oct4_len8


Currently the repository contain homerMotifs.motifs12.txt, and homerMotifs.motifs8.txt, which are the motif matrix of Oct4 in length 12 and length 8. Feel free to also try with other motif matrixs of other TFs.


Future work for this part: Currenly the motif patterns matches the Homer output, which means that the HTML_Report.py worked successfully, but the Homer output does not present all the motifs in the motif matrix file. Next step is to find what's the filtering requirements and also all more elements to the html output
