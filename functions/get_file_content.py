import os
from config import CHAR_LIMIT

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(abs_working_directory, file_path)

    if not full_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(CHAR_LIMIT)
    except:
        return 'Error: Invalid start byte'

    return file_content_string