from Bio import SeqIO

fasta_path = 'sequences.fasta'

# Read and print each record in the FASTA file
for record in SeqIO.parse(fasta_path, 'fasta'):
    print(f'>{record.id}')
    #print(record.seq)
    print()
