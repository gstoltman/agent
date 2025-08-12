import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(abs_working_directory, directory)
    abs_full_path = os.path.abspath(full_path)
    
    if not abs_full_path.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    contents_list = os.listdir(full_path)

    if directory == ".":
        result_string = "Result for current directory"
    else:
        result_string = f"Result for '{directory}' directory"

    for content in contents_list:
        if content.startswith('__'):
            break
        content_path = os.path.join(full_path, content)
        file_size = os.path.getsize(content_path)
        is_dir = os.path.isdir(content_path)
        result_string += f"\n - {content}: file_size={file_size} bytes, is_dir={is_dir}"

    return result_string

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
