import os
from google.genai import types


def write_file(working_directory, file_path, content):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error:{file_path} is not in the working directory"

    parent_dir = os.path.dirname(abs_file_path)

    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f"could not create the parent dir: {parent_dir}, Error: {e}"

    if not os.path.isfile(abs_file_path):
        pass

    try:

        with open(abs_file_path, "w") as f:
            f.write(content)
        return f"successfully wrote to {file_path}, {len(content)} characters written"
    except Exception as e:
        return f"Could not write in file: {file_path}, Error:{e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to their working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory, if not provided, lists files in the working directory itself",
            ),
        },
        required=["directory"],
    ),
)
