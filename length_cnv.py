# Open the input file 'cnv_segment.txt' and the output file 'cnv_segment_length.txt'
with open('cnv_segment_500.txt', 'r') as input_file, open('cnv_segment_500_length.txt', 'w') as output_file:
    # Write the header to the output file
    output_file.write("Start\tEnd\tLength\n")

    # Process each line in the input file
    for line in input_file:
        # Extract start and end coordinates from each line
        start, end = map(int, line.strip().split())

        # Calculate the length of the CNV segment
        length = end - start + 1

        # Write the information to the output file
        output_file.write(f"{start}\t{end}\t{length}\n")

print("CNV segment lengths have been calculated and saved to 'cnv_segment_50_length.txt'.")
