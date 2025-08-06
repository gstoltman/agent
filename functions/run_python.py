import os

def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(abs_working_directory, file_path)

    if not full_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path[-3] == ".py":
        return f'Error: "{file_path}" is not a Python file.'