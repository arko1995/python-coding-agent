# from .functions.get_files_info import get_files_info
# from .functions.get_file_content import get_file_content
from .functions.write_file import write_file


def main():
    working_dir = "python_coding_agent/calculator"

    print(write_file(working_dir, "lorem.txt", "wait this isn't lorem text"))
    print(write_file(working_dir, "pkg/morelorem.txt", "This is more lorem ipsum text"))
    print(write_file(working_dir, "/tmp/temp.txt", "This should not be allowed"))


main()
