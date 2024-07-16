def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split(',')
            data.append((int(columns[0]), int(columns[1]), int(columns[2]), columns[3]))
    return data

def read_segments(file_path):
    segments = []
    with open(file_path, 'r') as file:
        for line in file:
            start, end = map(int, line.strip().split())
            segments.append((start, end))
    return segments

def extract_sequence(data, segments):
    result = {}
    for start, end in segments:
        sequence = ""
        for position, nucleotide in data:
            if start <= position <= end:
                sequence += nucleotide
        result[(start, end)] = sequence
    return result

# Replace 'test1.csv' and 'CNV_segments_revised.txt' with your actual file paths
csv_data = read_csv('test1.csv')
segments_data = read_segments('CNV_segments_revised.txt')
result_sequence = extract_sequence(csv_data, segments_data)

# Print the result
for segment, sequence in result_sequence.items():
    print(f"Segment {segment}: {sequence}")
