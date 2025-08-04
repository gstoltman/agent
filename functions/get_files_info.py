import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_path = os.path.abspath(directory)

    if not abs_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'

    contents_list = os.listdir(directory)

    result_text = ''

    for content in contents_list:
        file_size = os.path.isfile(content)
        is_dir = os.path.isdir(content)
        result_text.join(content, file_size, is_dir, '\n')

    return result_text
