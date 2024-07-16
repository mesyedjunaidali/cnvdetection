def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split(',')
            data.append((int(columns[0]), int(columns[1]), int(columns[2]), columns[3]))
    return data

def write_fasta(output_file, data):
    with open(output_file, 'w') as file:
        file.write('>human\n')  # Header for the entire sequence
        sequence = ''.join([nucleotide for _, _, _, nucleotide in data])
        file.write(sequence + '\n')

# Replace 'test1.csv' and 'output.fasta' with your actual file paths
csv_data = read_csv('test1.csv')
write_fasta('output.fasta', csv_data)

