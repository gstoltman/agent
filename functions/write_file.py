import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(abs_working_directory, file_path)

    if not full_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        try:
            with open(full_path, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except:
            return "Error: Issues creating file"
    else:
        try:
            with open(full_path, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except:
            return "Error: Issues writing to file"