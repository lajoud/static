import shutil
import os


def export_data(origin, destination):
    working_directory=os.getcwd()
    source=os.path.join(working_directory, origin)
    source= os.path.abspath(os.path.normpath(source))

    dest=os.path.join(working_directory, destination)
    dest= os.path.abspath(os.path.normpath(dest))

    shutil.copytree(
        source,
        dest,
        dirs_exist_ok=True,
        copy_function=shutil.copy2  # preserves metadata like cp -a
    )


def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        full_path = os.path.abspath(os.path.normpath(full_path))
        work_dir_path=os.path.abspath(working_directory)
        
        if os.path.commonpath([work_dir_path, full_path]) == work_dir_path:
            pass
        else:
            raise Exception(f"""Error: Cannot read "{file_path}" as it is outside the permitted working directory""")
        isfile = os.path.isfile(full_path)   
        if isfile:
            pass
        else:
            raise Exception(f"""Error: File not found or is not a regular file: {file_path}""")
        
        with open(full_path,"r") as f:
            content=f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            f.close()
        return content
    except Exception as e:
        return f"Error: {e}"
