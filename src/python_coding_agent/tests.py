from .functions.get_files_info import get_files_info


def main():
    working_dir = "python_coding_agent/calculator"
    root_contents = get_files_info(working_dir)
    print(root_contents)
    pkg_contents = get_files_info(working_dir, "pkg")
    print(pkg_contents)
    bin_contents = get_files_info(working_dir, "/bin")
    print(bin_contents)


main()
