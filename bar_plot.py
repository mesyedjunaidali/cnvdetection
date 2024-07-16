import matplotlib.pyplot as plt

# Results from the previous code
range_500_1000 = 2299
range_1001_200000 = 1995
range_200001_500000 = 11
range_500001_1000000 = 2
range_greater_than_1000000 = 1

# Categories and corresponding counts
categories = ['.5-1kb', '2-200kb', '201-500kb', '.5-1Mb', '>1Mb']
counts = [range_500_1000, range_1001_200000, range_200001_500000, range_500001_1000000, range_greater_than_1000000]

# Create a bar graph with thinner bars
plt.figure(figsize=(10, 6))
plt.bar(categories, counts, color='gray', width=0.25)  # Adjust the width as needed
plt.title('Number of Segments in Size Ranges')
plt.xlabel('Size Ranges')
plt.ylabel('Number of Segments')

# Save the plot as an image
plt.savefig('segment_size_bar_graph.png')

# Display the plot
plt.show()
