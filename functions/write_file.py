import os

def write_file(working_directory, file_path, content):
    wd = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(wd, file_path))

    if os.path.commonpath([wd, full_path]) != wd:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'

    
    




#os.path.exists: Check if a path exists
#os.makedirs: Create a directory and all its parents
#os.path.dirname: Return the directory name