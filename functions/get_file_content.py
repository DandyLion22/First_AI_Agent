import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    wd = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(wd, file_path))

    if not full_path.startswith(wd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS)
            has_more = f.read(1)  # returns '' if EOF
            if has_more:
                content += f'[...File "{file_path}" truncated at 10000 characters]'
            return content
    except Exception as e:
        return f'Error: {e}'
