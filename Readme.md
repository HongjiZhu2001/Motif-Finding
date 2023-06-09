# Motif-Finding
The goal for this project is to implement the known motif finding part of findMotifsGenome.pl from Homer in python.

More about the Homer motif analysis: http://homer.ucsd.edu/homer/motif/index.html

The project seprates into two parts: Part1: Read peak.txt & reference genome files to generate motif matrix and Part2: Use motif matrix to generate the html report.
<br/><br/>


## Set up
``` pip install -r requirements.txt```

If you encounter any errors with using seqlogo, you may also need to install Ghostscript: https://ghostscript.com/releases/gsdnld.html
<br/><br/>
## Part1: Read peak file, reference genome files, and motif library to generate motif matrix
Usage: ```python Known_Motif_Search.py peak_file genome_file output_file [optional]custom_motif_library```

Example Usage:

```python Known_Motif_Search.py peaks_Oct4.txt GRCm38.chr17.fa Oct4_known_motifs.txt```

```python Known_Motif_Search.py peaks_Sox2.txt GRCm38.chr17.fa Sox2_known_motifs.txt```

```python Known_Motif_Search.py peaks_Klf4.txt GRCm38.chr17.fa Klf4_known_motifs.txt Homer_motifs.txt```

This repository contains the Homer motif library Homer_motifs.txt, from http://homer.ucsd.edu/homer/custom.motifs.

This repository also contains some example peak files of transcription factors: Oct4, Sox2, and Klf4: peaks_Oct4.txt, peaks_Sox2.txt, peaks_Klf4.txt

If no custom_motif_library is specified, the tool will use Homer_motifs.txt by default.

If you plan to use a custom_motif_library, please make sure it's in the same format as Homer_motifs.txt

Output: a motif_matrix_file containing the motifs found in the peak regions.
<br/><br/>

## Part2: Use motif matrix to generate the html report
Usage: ```python HTML_Report.py motif_matrix_file [optional]output_file_name(out.html if not specified)```

Example Usage:

```python HTML_Report.py Oct4_known_motifs.txt Oct4_report```

```python HTML_Report.py Sox2_known_motifs.txt Sox2_report```

```python HTML_Report.py Klf4_known_motifs.txt Klf4_report```

Output: a .html output containing the motif sequence found with the logo showing the probability of nucleotides. 
<br/><br/>

### For running data in More_Data folder:
Usage: 
```python Known_Motif_Search_Modified.py ./More_Data/.peak.bed_file GRCm38.chr17.fa output_file```
```python HTML_Report_Modified.py motif_matrix_file(from previous step) output_file```
       
Example Usage: 
```python Known_Motif_Search_Modified.py ./More_Data/ESC_Esrrb.peaks.bed GRCm38.chr17.fa Esrrb_known_motifs.txt```
```python HTML_Report_Modified.py Esrrb_known_motifs.txt Esrrb_report```
<br/><br/>
## References
Data used for example usages:

https://www.ncbi.nlm.nih.gov/pubmed/28111071

https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90895 
