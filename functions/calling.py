def call_function(function_call_part, verbose=False):
    if if "--verbose" in args:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    if response.function_calls is not None:
        # We are building these
        if function_call_part.name == 'get_files_info':
        if function_call_part.name == 'get_file_content'
        if function_call_part.name == 'run_python_file'
        if function_call_part.name == 'write_file'
    else:
        result = response.text
    return result