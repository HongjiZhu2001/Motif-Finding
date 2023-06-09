import itertools
import sys

peak_file = sys.argv[1]
genome_file = sys.argv[2]
output_file = sys.argv[3]
custom_motif = "no input"
try:
    custom_motif = sys.argv[4]
except:
    pass

def get_sequence_variables(sequence):
    nucleotides = {
        'A': ['A'],
        'C': ['C'],
        'G': ['G'],
        'T': ['T'],
        'U': ['U'],
        'R': ['G', 'A'],
        'Y': ['C', 'T'],
        'K': ['G', 'T'],
        'M': ['A', 'C'],
        'S': ['G', 'C'],
        'W': ['A', 'T'],
        'B': ['G', 'T', 'C'],
        'D': ['G', 'A', 'T'],
        'H': ['A', 'C', 'T'],
        'V': ['G', 'C', 'A'],
        'N': ['A', 'G', 'C', 'T']
    }

    sequences = []
    options = [nucleotides.get(base, [base]) for base in sequence]
    for combination in itertools.product(*options):
        sequences.append(''.join(combination))

    return sequences

def extract_peak_fragments(peak_file, genome_file):
    fragments = []

    with open(peak_file, 'r') as peak, open(genome_file, 'r') as genome:
        genome_sequence = genome.read().replace('\n', '')  

        # Skip header lines in the peak file
        for line in peak:
            if line.startswith("#"):
                continue
            else:
                break

        # Process peak lines
        for line in peak:
            fields = line.strip().split("\t")
            if fields[0] != "chr17":
                continue  

            start = int(fields[1]) 
            end = int(fields[2])  

            sequence = genome_sequence[start:end]
            fragments.append(sequence)

    return fragments

#peak_file = './Tfs/preiPSC1_cMyc.peaks.bed'
#genome_file = './GRCm38.chr17.fa'
fragments = extract_peak_fragments(peak_file, genome_file)


def extract_motifs_from_file(file_path):
    motifs = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Iterate over the lines and extract motifs
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('>'):
            motif_sequence = line.split()[0][1:]  
            motif_name = line.split()[1]
            motif_probability_matrix = []
            i += 1
            while i < len(lines) and not lines[i].startswith('>'):
                probabilities = list(map(float, lines[i].strip().split()))
                motif_probability_matrix.append(probabilities)
                i += 1
            motifs.append((motif_sequence,motif_name, motif_probability_matrix))

            variables = get_sequence_variables(motif_sequence)
            for j in variables:
                motifs.append((j,motif_name, motif_probability_matrix))
        else:
            i += 1

    return motifs



def search_motifs(fragments, known_motifs, output_file):
    motifs_found = {}

    with open(output_file, 'w') as file:
        for fragment in fragments:
            if len(fragment) >0:
                sequence= fragment

                for motif_sequence,motif_name, motif_probability_matrix in known_motifs:
                    if motif_sequence in sequence:
                        if motif_sequence in motifs_found:
                            motifs_found[motif_sequence] = motif_name
                        else:
                            motifs_found[motif_sequence] = motif_name

        for motif_sequence, name in motifs_found.items():
            file.write(f">{motif_sequence}     {name}\n")
            motif_probability_matrix = next(
                (matrix for sequence, name, matrix in known_motifs if sequence == motif_sequence), None)
            if motif_probability_matrix:
                for probabilities in motif_probability_matrix:
                    file.write(' '.join(map(str, probabilities)) + '\n')


#output_file = 'motifs_output_cMyc.txt'
if custom_motif != "no input":
    known_motifs = extract_motifs_from_file(custom_motif)
else:
    known_motifs = extract_motifs_from_file("./Homer_motifs.txt")
search_motifs(fragments, known_motifs, output_file)
