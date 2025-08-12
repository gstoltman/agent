import os
from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to file with content arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of of the Python file to write to",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file",
            ),
        },
    ),
)