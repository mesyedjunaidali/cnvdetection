import pysam

def retrieve_sequence_from_bam(bam_file, chromosome, start, end):
    samfile = pysam.AlignmentFile(bam_file, "rb")
    sequence = ""

    # Fetch the reference sequence
    ref_sequence = samfile.fetch(chromosome, start, end)

    for pos, ref_base in enumerate(ref_sequence):
        base_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        
        for pileupcolumn in samfile.pileup(chromosome, start + pos, start + pos + 1):
            for pileupread in pileupcolumn.pileups:
                if not pileupread.is_del and not pileupread.is_refskip:
                    observed_base = pileupread.alignment.query_sequence[pileupread.query_position]
                    
                    # Exclude 'N' bases from consideration
                    if observed_base != 'N':
                        base_counts[observed_base] += 1

        # Find the most frequent base
        major_base = max(base_counts, key=base_counts.get)
        sequence += major_base

    samfile.close()
    return sequence

# Read CNV segment coordinates from the file
cnv_segments_file = 'output_cnv_segments.txt'  # Replace with your file path
with open(cnv_segments_file, 'r') as file:
    cnv_segments = [list(map(int, line.split())) for line in file]

# Example Usage:
bam_file = "sorted22.bam"  # Replace with the path to your BAM file
output_file = "cnv_sequences.txt"  # Output file for sequences and details

with open(output_file, 'w') as output:
    # Iterate through your CNV segments and retrieve sequences
    for segment in cnv_segments:
        start, end, _ = segment
        start += 16050000
        end += 16050000
        sequence = retrieve_sequence_from_bam(bam_file, "22", start, end)
        length = end - start + 1
        output.write(f"CNV Segment {start}-{end} (Length: {length}) Sequence: {sequence}\n")
