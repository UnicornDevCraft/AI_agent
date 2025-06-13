import os


def get_files_info(working_directory, directory=None):
    try:
        if os.path.exists(working_directory) and os.path.isdir(working_directory):
            abs_path_work_dir = os.path.abspath(working_directory)
            abs_path_dir = abs_path_work_dir

        if directory:
            abs_path_dir = os.path.abspath(os.path.join(working_directory, directory))

        if not os.path.isdir(abs_path_dir):
            return f'Error: "{directory}" is not a directory'
        
        if not abs_path_dir.startswith(abs_path_work_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        output = []
        for file in os.listdir(abs_path_dir):
            abs_file_path = os.path.join(abs_path_dir, file) 
            output.append(f"- {file}: file_size={os.path.getsize(abs_file_path)} bytes, is_dir={os.path.isdir(abs_file_path)}")
        result = "\n".join(output)
    except Exception as e:
        return f"Error: {e}"
    
    return result
