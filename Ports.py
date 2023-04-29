import os
import zipfile

# Set the directory where the zip files are located
directory = '/bbh/tmp_work/UMDCTF/ports/'

# Iterate through all the files in the directory
for filename in os.listdir(directory):
    # Check if the file is a zip file with the correct naming pattern
    if filename.endswith(".txt.zip") and filename.startswith("port-"):
        # Get the code for the password from the filename
        code = filename.split('-')[1].split('.')[0]

        # Construct the password
        password = bytes(code, 'utf-8')

        # Create the full file path
        file_path = os.path.join(directory, filename)

        # Open and extract the zip file using the password
        with zipfile.ZipFile(file_path) as zf:
            try:
                zf.extractall(path=directory, pwd=password)
                print(f"Successfully extracted {filename}")
            except RuntimeError as e:
                print(f"Error extracting {filename}: {e}")

print("Finished extracting all files.")