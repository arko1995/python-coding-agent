import os

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: The {file_path} is not in the working directory"

    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} is not a file"

    with open(abs_file_path) as f:
        file_content_string = f.read(MAX_CHARS)
