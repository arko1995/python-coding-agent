import os
import subprocess
from google.genai import types


def run_python_file(working_directory: str, file_path: str, args=[]):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: The {file_path} is not in the working directory"

    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} is not a file"
    if not file_path.endswith(".py"):
        return f"Error: '{file_path}' is not a python file"

    try:

        final_args = ["python3", file_path]
        final_args.extend(args)
        output = subprocess.run(
            final_args, timeout=30, capture_output=True, cwd=abs_working_dir
        )

        final_string = f""""
        STDOUT: {output.stdout},
        STDERR: {output.stderr}
        """

        if output.stdout == "" and output.stderr == "":
            final_string = "No Output Produced. \n"

        if output.returncode != 0:
            final_string += f"Process exited with exit code:{output.returncode}"

        return final_string

    except Exception as e:
        return f"Error running python fille, Error:{e}"


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
