import os

def write_file(working_directory, file_path, content):
    try:
        if os.path.exists(working_directory) and os.path.isdir(working_directory):
            abs_path_work_dir = os.path.abspath(working_directory)

        abs_file_path = os.path.join(abs_path_work_dir, file_path)
        
        if not abs_file_path.startswith(abs_path_work_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f"Error: {e}"

