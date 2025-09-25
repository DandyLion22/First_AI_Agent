import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    wd = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(wd, file_path))

    if os.path.commonpath([wd, full_path]) != wd:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        cp_object = subprocess.run(["python", full_path] + args, timeout=30, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=wd)

        output_lines = []
        decoded_stdout = cp_object.stdout.decode("utf-8").strip()
        decoded_stderr = cp_object.stderr.decode("utf-8").strip()

        if not decoded_stdout and not decoded_stderr:
            return "No output produced"
        if decoded_stdout:
            output_lines.append("STDOUT: " + decoded_stdout)
        if decoded_stderr:
            output_lines.append("STDERR: " + decoded_stderr)
        if cp_object.returncode != 0:
            output_lines.append(f"Process exited with code {cp_object.returncode}")
        
        return "\n".join(output_lines)
        
    except Exception as e:
        return f"Error: executing Python file {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)