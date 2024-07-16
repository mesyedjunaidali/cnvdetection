import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('test1.csv')

# Extract data from the DataFrame
genomic_coordinates = df.iloc[:, 0]
coverage_values = df.iloc[:, 1]
quantification_values = df.iloc[:, 2]

# Create a box plot
plt.figure(figsize=(10, 6))
plt.boxplot([coverage_values, quantification_values], labels=['Coverage', 'Quantification'])
plt.title('Box Plot of Coverage and Quantification for NA12878 Genome Sample')
plt.xlabel('Data Type')
plt.ylabel('Values')
plt.savefig('box_plot.png')
plt.show()
