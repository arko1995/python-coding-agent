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


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the contents passed in the CLI into the file designated at the file path, If there is existing content in the file it will replace the content, if the directory does not exist, it will create the directory. If the file does not exist, it will create the file and then write the content into it,constrained to their working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file that gets written into, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that gets written into the file as a string",
            ),
        },
        required=["file_path"],
    ),
)
