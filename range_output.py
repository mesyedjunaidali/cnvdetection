# Open the input file 'cnv_segment_500_length.txt'
with open('cnv_segment_500_length.txt', 'r') as input_file:
    # Skip the header line
    next(input_file)

    # Initialize counters for each size range
    range_500_1000 = 0
    range_1001_200000 = 0
    range_200001_500000 = 0
    range_500001_1000000 = 0
    range_greater_than_1000000 = 0

    # Process each line in the input file
    for line in input_file:
        # Extract length from the third column
        length = int(line.strip().split()[2])

        # Count segments within the specified size ranges
        if 500 <= length <= 1000:
            range_500_1000 += 1
        elif 1001 <= length <= 200000:
            range_1001_200000 += 1
        elif 200001 <= length <= 500000:
            range_200001_500000 += 1
        elif 500001 <= length <= 1000000:
            range_500001_1000000 += 1
        else:
            range_greater_than_1000000 += 1

# Display the results
print("Number of segments in size range 500-1000:", range_500_1000)
print("Number of segments in size range 1001-200000:", range_1001_200000)
print("Number of segments in size range 200001-500000:", range_200001_500000)
print("Number of segments in size range 500001-1000000:", range_500001_1000000)
print("Number of segments with size greater than 1000000:", range_greater_than_1000000)
