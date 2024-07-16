import os

# Specify the directory path where the files are located
directory = 'C:\Junaid\Final_Year_Project\Dataset\CNV_VIRUS'

# List all files in the directory
files = os.listdir(directory)

# Iterate through each file and rename it
for file_name in files:
    if file_name.startswith('sequences (') and file_name.endswith(').fasta'):
        # Extract the number from the file name
        number = file_name.split('(')[1].split(')')[0]
        
        # Construct the new file name
        new_name = f'sequence_{number}.fasta'
        
        # Full paths for the old and new file names
        old_path = os.path.join(directory, file_name)
        new_path = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)

print("Files renamed successfully.")
