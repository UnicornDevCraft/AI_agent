import os

"""
Well I overdone it a bit to check the contents of the folder in recursive manner, I am not going to delete it.
but still the simplier way should be choosen
 
def get_contents_relative_path(working_directory, filename):
    file_paths = []
    try:
        rel_file_path = os.path.join(working_directory, filename)
        if os.path.exists(rel_file_path) and os.path.isfile(rel_file_path):
            file_paths.append(filename)
            return file_paths   
        else:
            folder_contents = os.listdir(rel_file_path)
            for file in folder_contents:
                new_filename = get_contents_relative_path(rel_file_path, file)
                new_file_path = [os.path.join(filename, new_filename_file) for new_filename_file in new_filename]
                file_paths.extend(new_file_path)
    except Exception as e:
        return f"Error: {e}"
    
    return file_paths

def gather_rel_path(working_directory, file_path):
    list_files, contents = [], []
    abs_work_dir_path = os.path.abspath(working_directory)
    try:
        if os.path.exists(abs_work_dir_path) and os.path.isdir(abs_work_dir_path):
            contents = os.listdir(abs_work_dir_path)
    
        abs_file_path = os.path.join(abs_work_dir_path, file_path)

        if os.path.exists(abs_file_path) and os.path.isfile(abs_file_path):
            for file in contents:
                list_files.extend(get_contents_relative_path(working_directory, file))
    except Exception as e:
        return f"Error: {e}"
    
    return list_files"""


def get_file_content(working_directory, file_path):
    try:
        if os.path.exists(working_directory) and os.path.isdir(working_directory):
            abs_path_work_dir = os.path.abspath(working_directory)

        abs_file_path = os.path.join(abs_path_work_dir, file_path)

        if not os.path.exists(abs_file_path) or not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        if not abs_file_path.startswith(abs_path_work_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        MAX_CHARS = 10_000

        with open(abs_file_path) as f:
            file_content = f.read(10_001)
            if len(file_content) > MAX_CHARS:
                new_file_content = f'{file_content[:MAX_CHARS]} [...File "{file_path}" truncated at 10000 characters]' 
                file_content = new_file_content
        
    except Exception as e:
        return f"Error: {e}"
    
    return file_content