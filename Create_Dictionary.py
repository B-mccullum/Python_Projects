import os

def generate_file_list(path="."):
    file_list = []  # Initialize an empty list to store file dictionaries
    for root, dirs, files in os.walk(path):
        # os.walk() traverses the directory tree and yields root, dirs, and files for each directory visited
        for file in files:
            # Iterate over the files in the current directory
            file_path = os.path.join(root, file)  # Get the complete file path
            file_dict = {
                "file_name": file,
                "file_path": file_path,
                "file_size": os.path.getsize(file_path)  # Get the file size using os.path.getsize()
            }
            file_list.append(file_dict)  # Append the file dictionary to the file list
    return file_list  # Return the list of file dictionaries

if __name__ == "__main__":
    # If the script is being run directly as the main program
    files = generate_file_list()  # Generate the list of file dictionaries using the default path
    for file in files:
        # Iterate over the file dictionaries
        print(file)  # Print each file dictionary
