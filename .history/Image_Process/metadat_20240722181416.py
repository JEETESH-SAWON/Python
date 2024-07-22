import subprocess

# Define the file path
file_path = "image/test.jpg"

# Run hachoir-metadata and capture the output
process = subprocess.Popen(['hachoir-metadata', file_path],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           universal_newlines=True)

stdout, stderr = process.communicate()

# Print the output
print(stdout)
if stderr:
    print("Errors:", stderr)