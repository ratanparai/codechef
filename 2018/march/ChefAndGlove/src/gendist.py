import glob
import os


def all_in_one():
    print("Starting processing the source code...")
    delete_old_dist_file()

    cpp_file_path_glob = os.path.dirname(os.path.abspath(__file__)) + "/*.cpp"
    all_code_files = glob.glob(cpp_file_path_glob)

    all_lines = []

    includes = []
    usings = []
    main_method = []
    other_method = []

    all_lines, includes = extracts_includes(all_code_files, all_lines, includes, usings)

    extract_main_method(all_lines, main_method)

    all_header_lines = []
    methods_from_header_files = []

    extract_other_method_signature_from_header_file(all_header_lines, methods_from_header_files)
    extract_other_methods(all_lines, methods_from_header_files, other_method)

    # write_file_path = os.path.dirname(os.path.abspath(__file__)) + "/dist.c"
    # write_to_dist_file(includes, main_method, other_method, usings, write_file_path)
    #
    # write_to_dist_file(includes, main_method, other_method, usings, "src/dist.c")
    write_to_dist_file(includes, main_method, other_method, usings, "dist.cpp")


def extract_main_method(all_lines, main_method):
    inside_main_method = False
    # TODO: extract main method
    for line in all_lines:
        if line.startswith("int main("):
            inside_main_method = True

        if inside_main_method:
            main_method.append(line)
            if line.startswith("}"):
                break


def extracts_includes(all_code_files, all_lines, includes, usings):
    for files in all_code_files:
        with open(files) as f:
            all_lines += f.readlines()
    for line in all_lines:
        if line.startswith("#include") and line.count("src/") == 0:
            includes.append(line)
        if line.startswith("using"):
            usings.append(line)
    includes = list(set(includes))
    print(includes)
    return all_lines, includes


def extract_other_method_signature_from_header_file(all_header_lines,methods_from_header_files):
    header_file_glob = os.path.dirname(os.path.abspath(__file__)) + "/*.h"
    print(header_file_glob)
    header_files = glob.glob(header_file_glob)
    for h_file in header_files:
        with open(h_file) as f:
            all_header_lines += f.readlines()
    # extracts methods
    for line in all_header_lines:
        line = line.strip()
        if not line.startswith("#") and not line.startswith("//") and not line == "":
            methods_from_header_files.append(line[:-1])
    print(methods_from_header_files)


def extract_other_methods(all_lines, methods_from_header_files, other_method):
    # searching methods in cpp files
    inside_other_method = False
    for method in methods_from_header_files:
        print("Checking for method " + method)
        for line in all_lines:
            if line.startswith(method):
                print("found other method" + method)
                inside_other_method = True

            if inside_other_method:
                other_method.append(line)
                if line.startswith("}"):
                    inside_other_method = False
                    break


def write_to_dist_file(includes, main_method, other_method, usings, write_file_path):
    print("generating new dist.cpp file")
    with open(write_file_path, "w") as f:
        f.writelines(includes)
        f.writelines(usings)
        f.writelines(other_method)
        f.writelines("\n")
        f.writelines(main_method)


def delete_old_dist_file():
    dist_file_path = os.path.dirname(os.path.abspath(__file__)) + "/dist.cpp"
    if os.path.isfile(dist_file_path):
        try:
            print("file found. now deleting..")
            os.remove("dist.cpp")
        except:  ## if failed, report it back to the user ##
            print ("File can not be deleted")


if __name__ == '__main__':
    all_in_one()
