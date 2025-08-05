import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    print(f"abs_working_directory is {abs_working_directory}")
    print(f"abs_full_path is {os.path.abspath(full_path)}")
    
    if os.path.commonpath([abs_working_directory, full_path]) != abs_working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    contents_list = os.listdir(full_path)

    result_text = ''

    for content in contents_list:
        content_path = os.path.join(full_path, content)
        file_size = os.path.getsize(content_path)
        is_dir = os.path.isdir(content_path)
        result_text.join(f"{content} | File Size: {file_size} | Directory: {is_dir}")

    return result_text
