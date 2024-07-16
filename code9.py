def read_segments(file_path):
    segments = []
    with open(file_path, 'r') as file:
        for line in file:
            start, end = map(int, line.strip().split())
            segments.append((start, end))
    return segments

def read_csv(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split(',')
            position = int(columns[0])
            nucleotide = columns[1]
            data[position] = nucleotide
    return data

def retrieve_sequences(segments, data):
    sequences = {}
    for start, end in segments:
        sequence = ''.join([data.get(coord, '') for coord in range(start, end + 1)])
        sequences[(start, end)] = sequence
    return sequences

# Replace 'CNV_segments_revised.txt' and 'test2.csv' with your actual file paths
segments_data = read_segments('cnv_segment_50.txt')
csv_data = read_csv('test2.csv')

result_sequences = retrieve_sequences(segments_data, csv_data)

# Write the result to a text file
with open('output_sequences_50.txt', 'w') as output_file:
    for segment, sequence in result_sequences.items():
        output_file.write(f"Segment {segment}: {sequence}\n")
