import os


def rename_files(directory_path):
    # Get the list of files in the directory
    files = os.listdir(directory_path)

    # Sort the files by length
    files.sort(key=len)


    readme = open("./README.md", "w")
    readme.write(f"# There is {len(files)} wallpaper\n\n\n")
    readme.close()

    # Iterate through the sorted files and rename them
    for index, filename in enumerate(files):
        # Construct the new filename with index
        new_filename = f"{index+1}_lala.{filename.split('.')[1]}"

        # Build the full path for the old and new filenames
        old_path = os.path.join(directory_path, filename)
        new_path = os.path.join(directory_path, new_filename)
        
        f = open("./README.md", "a")
        f.write(f'\n{index+1}.\n<div align="center"><img src="{new_path}" height="360" width="640" /></div>')
        f.close()

        # Check if the new filename already exists
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)

    print(f"There is {len(files)} images")

# Replace 'your_directory_path' with the actual path of the directory containing the files
directory_path = './images/'

# Call the function to rename files in the specified directory
rename_files(directory_path)

