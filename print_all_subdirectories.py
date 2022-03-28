import os

def print_subdirectories(dir_path):
    entries = os.scandir(dir_path)
    for e in entries:
        if e.is_dir():
            print(e.name)
            print_subdirectories(e.path)


path = os.chdir("E:/")
dirs = print_subdirectories(path)

print(f"Dir: ", dirs)
            


