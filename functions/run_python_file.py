import os
import subprocess


def run_python_file(working_directory, file_path):
    try:
        if os.path.exists(working_directory) and os.path.isdir(working_directory):
            abs_path_work_dir = os.path.abspath(working_directory)

        abs_file_path = os.path.abspath(os.path.join(abs_path_work_dir, file_path))
        
        if not abs_file_path.startswith(abs_path_work_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(abs_file_path) or not os.path.isfile(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        
        if os.path.splitext(abs_file_path)[1] != '.py':
            return f'Error: "{file_path}" is not a Python file.'
        
        running_file = subprocess.run(["python3", abs_file_path], capture_output=True, timeout=30, cwd=abs_path_work_dir, check=True, encoding='utf-8')

        output = ""

        if running_file.stdout:
            output += f"STDOUT: {running_file.stdout}\n"

        if running_file.stderr:
            output += f"STDERR: {running_file.stderr}\n"

        if running_file.returncode != 0:
            output += f"Process exited with code {running_file.returncode}"

        if not output:
            return "No output produced"
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    return output
    
