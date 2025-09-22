import os

def get_files_info(working_directory, directory="."):
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(os.path.join(abs_work, directory))

    if not (abs_full == abs_work or abs_full.startswith(abs_work + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_full):
        return f'Error: "{directory}" is not a directory'
    else:
        try:
            entries = sorted(os.listdir(abs_full))
            lines = []
            for name in entries:
                item_path = os.path.join(abs_full, name)
                size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
            return "\n".join(lines)
        except Exception as e:
            return f"Error listing files: {e}"
        

